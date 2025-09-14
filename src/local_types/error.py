from enum import Enum


class ErrorType(Enum):
    MAIN_ERROR = "main_error"

    START_COMMAND_ERROR = "start_command_error"
    POST_COMMAND_ERROR = "post_command_error"
    POST_MESSAGE_ERROR = "post_message_error"

    IMAGE_LLM_ERROR = "image_llm_error"
    TEXT_LLM_ERROR = "text_llm_error"

    POST_SERVICE_ERROR = "post_service_error"
    QUEUE_SERVICE_ERROR = "queue_service_error"

    POST_JOB_ERROR = "post_job_error"
    QUEUE_JOB_ERROR = "queue_job_error"

    POST_UTILS_ERROR = "post_utils_error"
    IMAGE_UTILS_ERROR = "image_utils_error"
