from local_types import LlmConfig

LLM: LlmConfig = {
    "image": {
        "model": "dall-e-3",
        "size": "1024x1024",
        "quality": "standard",
    },
    "text": {"model": "gpt-4o", "temperature": 0.7},
}
