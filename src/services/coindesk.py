from typing import Optional

import requests

from constants import ENV
from local_types import ErrorType, NewsItem
from utils import logger


class CoindeskService:
    @staticmethod
    async def search_news(
        search_string: str,
        limit: Optional[int] = 5,
        lang: str = "EN",
        source_key: Optional[str] = "coindesk",
    ) -> list[NewsItem] | None:
        try:
            params = {
                "search_string": search_string,
                "limit": limit,
                "lang": lang,
                "source_key": source_key,
            }
            url = f"{ENV['COINDESK_BASE_URL']}/news/v1/search"

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

            news: NewsItem = [
                {"title": item["TITLE"], "body": item["BODY"]} for item in data["Data"]
            ]

            return news

        except Exception as exc:
            logger.error(f"{ErrorType.COINDESK_SERVICE_ERROR.value}: {str(exc)}")

            return None
