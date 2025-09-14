from local_types import PostConfig
from prompts import (
    analytics_image_prompt,
    analytics_text_prompt,
    meme_image_prompt,
    meme_text_prompt,
    news_image_prompt,
    news_text_prompt,
)

POST: PostConfig = {
    "analytics": {
        "text": analytics_text_prompt,
        "image": analytics_image_prompt,
    },
    "news": {
        "text": news_text_prompt,
        "image": news_image_prompt,
    },
    "meme": {
        "text": meme_text_prompt,
        "image": meme_image_prompt,
    },
}

# {
#     "type": "web_search_preview",
#     "search_context_size": "medium",
#     "user_location": {
#         "type": "approximate",
#         "city": null,
#         "country": "US",
#         "region": null,
#         "timezone": null,
#     },
# }
