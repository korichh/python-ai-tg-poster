from ai.prompts import (
    analytics_image_prompt,
    analytics_text_prompt,
    meme_image_prompt,
    meme_text_prompt,
    news_image_prompt,
    news_text_prompt,
)
from local_types import LlmConfig, PostConfig

llmConfig: LlmConfig = {
    "image": {
        "model": "dall-e-3",
        "size": "1024x1024",
        "quality": "standard",
    },
    "text": {"model": "gpt-4o", "temperature": 0.7},
}


postConfig: PostConfig = {
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
