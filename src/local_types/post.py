from typing import Dict, Literal, TypedDict

PostTopic = Literal["analytics", "news", "meme"]


class TopicConfig(TypedDict):
    text: str
    image: str


PostConfig = Dict[PostTopic, TopicConfig]


class Post(TypedDict):
    text: str
    photo_id: str
