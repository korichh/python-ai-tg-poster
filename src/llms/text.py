from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI

from config import LLM
from constants import ENV
from local_types import ErrorType
from prompts import text_llm_human_message, text_llm_system_message
from utils import logger


class TextLlm:
    config = LLM["text"]

    llm = ChatOpenAI(
        model=config["model"],
        temperature=config["temperature"],
        api_key=ENV["openai_api_key"],
    )
    prompt = ChatPromptTemplate.from_messages(
        [("system", text_llm_system_message), ("human", text_llm_human_message)]
    )
    chain = prompt | llm

    @staticmethod
    def invoke(context: str, topic_text: str) -> str | None:
        try:
            base_message = TextLlm.chain.invoke(
                {"context": context, "topic_text": topic_text}
            )

            return base_message.content

        except Exception as exc:
            logger.error(f"{ErrorType.TEXT_LLM_ERROR}: {str(exc)}")

            return None
