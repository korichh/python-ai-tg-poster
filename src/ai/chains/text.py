from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI

from ai.prompts import text_llm_human_message, text_llm_system_message
from config import llmConfig
from constants import ENV
from local_types import ErrorType
from utils import logger


class TextChain:
    config = llmConfig["text"]

    llm = ChatOpenAI(
        model=config["model"],
        temperature=config["temperature"],
        api_key=ENV["OPENAI_API_KEY"],
    )

    prompt = ChatPromptTemplate.from_messages(
        [("system", text_llm_system_message), ("human", text_llm_human_message)]
    )

    chain = prompt | llm

    @staticmethod
    def invoke(context: str, instruction: str) -> str | None:
        try:
            base_message = TextChain.chain.invoke(
                {"context": context, "instruction": instruction}
            )

            return base_message.content

        except Exception as exc:
            logger.error(f"{ErrorType.TEXT_LLM_ERROR.value}: {str(exc)}")

            return None
