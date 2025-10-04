import asyncio
import json
from typing import List, Optional, Tuple

import aiohttp
import requests

from constants import ENV
from local_types import (
    ErrorType,
    InstrumentHistoricalPrices,
    InstrumentNews,
    InstrumentsHistoricalPrices,
    InstrumentsLatestTick,
    InstrumentsMetadata,
    InstrumentsNews,
)
from utils import logger


class CoindeskService:
    @staticmethod
    async def get_instruments_news(
        search_strings: list[str],
        limit: Optional[int] = 2,
        lang: str = "EN",
        source_key: Optional[str] = "coindesk",
    ) -> InstrumentsNews | None:
        async def fetch_news(
            session: aiohttp.ClientSession, search_string: str
        ) -> Tuple[str, List[InstrumentNews]]:
            url = f"{ENV['COINDESK_BASE_URL']}/news/v1/search"

            params = {
                "search_string": search_string,
                "limit": limit,
                "lang": lang,
                "source_key": source_key,
            }

            headers = {
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Apikey {ENV['COINDESK_API_KEY']}",
            }

            try:
                async with session.get(
                    url, params=params, headers=headers, timeout=15
                ) as response:
                    response.raise_for_status()

                    data = await response.json()

                    news = [
                        {"title": item.get("TITLE"), "body": item.get("BODY")}
                        for item in data.get("Data", [])
                    ]

                    return search_string, news

            except Exception:
                return search_string, []

        results_dict: InstrumentsNews = {}

        try:
            async with aiohttp.ClientSession() as session:
                tasks = [fetch_news(session, string) for string in search_strings]

                results = await asyncio.gather(*tasks, return_exceptions=True)

                for result in results:
                    if isinstance(result, Exception):
                        continue

                    string, news_items = result

                    results_dict[string] = news_items

            return results_dict

        except Exception as exc:
            logger.error(f"{ErrorType.COINDESK_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    async def get_instruments_metadata(
        instruments: list[str],
        market: Optional[str] = "binance",
    ) -> InstrumentsMetadata | None:
        try:
            url = f"{ENV['COINDESK_BASE_URL']}/spot/v1/latest/instrument/metadata"

            params = {
                "instruments": ",".join(instruments),
                "market": market,
            }

            headers = {
                "Content-type": "application/json; charset=UTF-8",
                "authorization": f"Apikey {ENV['COINDESK_API_KEY']}",
            }

            response = requests.get(
                url=url,
                params=params,
                headers=headers,
            )

            data = response.json()

            results_dict = {}

            def get_filter(filters: list[dict], filter_type: str) -> dict:
                """Safely extract filter dict by type, return empty dict if missing."""
                return next(
                    (f for f in filters if f.get("filterType") == filter_type), {}
                )

            for _, item in data.get("Data", {}).items():
                external_data = json.loads(item.get("INSTRUMENT_EXTERNAL_DATA", "{}"))
                filters = external_data.get("filters", [])

                price_filter = get_filter(filters, "PRICE_FILTER")
                lot_filter = get_filter(filters, "LOT_SIZE")
                notional_filter = get_filter(filters, "NOTIONAL")

                filtered = {
                    "instrument": item.get("INSTRUMENT"),
                    "status": item.get("INSTRUMENT_STATUS"),
                    "base": item.get("INSTRUMENT_MAPPING", {}).get("BASE"),
                    "quote": item.get("INSTRUMENT_MAPPING", {}).get("QUOTE"),
                    "filters": {
                        "price": {
                            "min": price_filter.get("minPrice"),
                            "max": price_filter.get("maxPrice"),
                            "tickSize": price_filter.get("tickSize"),
                        },
                        "lot": {
                            "minQty": lot_filter.get("minQty"),
                            "maxQty": lot_filter.get("maxQty"),
                            "stepSize": lot_filter.get("stepSize"),
                        },
                        "notional": {
                            "minNotional": notional_filter.get("minNotional"),
                            "maxNotional": notional_filter.get("maxNotional"),
                        },
                    },
                    "timestamps": {
                        "firstSeen": item.get("FIRST_SEEN_ON_POLLING_TS"),
                        "lastSeen": item.get("LAST_SEEN_ON_POLLING_TS"),
                    },
                }

                results_dict[filtered["instrument"]] = filtered

            return results_dict

        except Exception as exc:
            logger.error(f"{ErrorType.COINDESK_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    async def get_instruments_latest_tick(
        instruments: list[str],
        market: Optional[str] = "binance",
    ) -> InstrumentsLatestTick | None:
        try:
            url = f"{ENV['COINDESK_BASE_URL']}/spot/v1/latest/tick"

            params = {
                "instruments": ",".join(instruments),
                "market": market,
            }

            headers = {
                "Content-type": "application/json; charset=UTF-8",
                "authorization": f"Apikey {ENV['COINDESK_API_KEY']}",
            }

            response = requests.get(
                url=url,
                params=params,
                headers=headers,
            )

            data = response.json()

            results_dict = {}

            for _, item in data.get("Data", {}).items():
                filtered = {
                    "instrument": item.get("INSTRUMENT"),
                    "market": item.get("MARKET"),
                    "price": item.get("PRICE"),
                    "price_last_update_ts": item.get("PRICE_LAST_UPDATE_TS"),
                    "best_bid": item.get("BEST_BID"),
                    "best_ask": item.get("BEST_ASK"),
                }

                results_dict[filtered["instrument"]] = filtered

            return results_dict

        except Exception as exc:
            logger.error(f"{ErrorType.COINDESK_SERVICE_ERROR.value}: {str(exc)}")

            return None

    @staticmethod
    async def get_instruments_historical_prices(
        instruments: list[str],
        limit: int = 7,
        market: Optional[str] = "binance",
    ) -> InstrumentsHistoricalPrices | None:
        async def fetch_instrument(
            session: aiohttp.ClientSession, instrument: str
        ) -> Tuple[str, List[InstrumentHistoricalPrices]]:
            url = f"{ENV['COINDESK_BASE_URL']}/spot/v1/historical/days"

            params = {"instrument": instrument, "limit": limit, "market": market}

            headers = {
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": f"Apikey {ENV['COINDESK_API_KEY']}",
            }

            try:
                async with session.get(
                    url, params=params, headers=headers, timeout=15
                ) as response:
                    response.raise_for_status()

                    data = await response.json()

                    historical_prices = [
                        {
                            "timestamp": item.get("TIMESTAMP"),
                            "open": item.get("OPEN"),
                            "high": item.get("HIGH"),
                            "low": item.get("LOW"),
                            "close": item.get("CLOSE"),
                            "volume": item.get("VOLUME"),
                        }
                        for item in data.get("Data", [])
                    ]

                    key = data.get("INSTRUMENT", instrument)

                    return key, historical_prices

            except Exception:
                return instrument, []

        results_dict: InstrumentsHistoricalPrices = {}

        try:
            async with aiohttp.ClientSession() as session:
                tasks = [fetch_instrument(session, inst) for inst in instruments]

                results = await asyncio.gather(*tasks, return_exceptions=True)

                for result in results:
                    if isinstance(result, Exception):
                        continue

                    instrument_name, historical_prices = result

                    results_dict[instrument_name] = historical_prices

            return results_dict
        except Exception as exc:
            logger.error(f"{ErrorType.COINDESK_SERVICE_ERROR.value}: {str(exc)}")

            return None
