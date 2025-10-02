from local_types import NewsItem


def format_coin_news(coin: str, news: list[NewsItem]) -> str:
    formatted = [
        f"{i + 1}. {item['title']}\n\n{item['body']}" for i, item in enumerate(news)
    ]

    return f"# {coin}\n\n" + "\n\n".join(formatted)


def format_news_context(news_results) -> str:
    return "\n\n".join(format_coin_news(coin, news) for coin, news in news_results)
