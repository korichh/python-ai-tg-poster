from typing import Dict, Literal, TypedDict


class ImageConfig(TypedDict):
    model: str
    size: str
    quality: str


class TextConfig(TypedDict):
    model: str
    temperature: float


class LlmConfig(TypedDict):
    image: ImageConfig
    text: TextConfig


PostTopic = Literal["analytics", "news", "meme"]


class TopicConfig(TypedDict):
    text: str
    image: str


PostConfig = Dict[PostTopic, TopicConfig]
