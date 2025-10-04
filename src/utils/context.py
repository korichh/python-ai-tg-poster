import json
from typing import List

from local_types import (
    InstrumentNews,
    InstrumentsHistoricalPrices,
    InstrumentsLatestTick,
    InstrumentsMetadata,
    InstrumentsNews,
)


def format_coin_news(coin: str, news: List[InstrumentNews]) -> str:
    if not news:
        return f"# {coin}\n\nNo news available.\n"

    formatted = [
        f"{i + 1}. {item['title']}\n\n{item['body']}" for i, item in enumerate(news)
    ]

    return f"# {coin}\n\n" + "\n\n".join(formatted)


def format_news_context(news: InstrumentsNews) -> str:
    if not news:
        return "No news available."

    return "\n\n".join(format_coin_news(coin, news) for coin, news in news.items())


def format_analytics_context(
    coins: List[str],
    metadata: InstrumentsMetadata,
    latest_tick: InstrumentsLatestTick,
    historical_prices: InstrumentsHistoricalPrices,
) -> str:
    sections: List[str] = []

    for coin in coins:
        coin_metadata = metadata.get(coin, {})
        coin_tick = latest_tick.get(coin, {})
        coin_history = historical_prices.get(coin, [])

        formatted_section = (
            f"# {coin}\n\n"
            f"## Metadata\n"
            f"{json.dumps(coin_metadata)}\n\n"
            f"## Latest Tick\n"
            f"{json.dumps(coin_tick)}\n\n"
            f"## Historical Prices\n"
            f"{json.dumps(coin_history)}"
        )

        sections.append(formatted_section)

    return "\n\n".join(sections) if sections else "No analytics data available."
