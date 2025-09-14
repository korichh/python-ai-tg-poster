from typing import TypedDict


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
