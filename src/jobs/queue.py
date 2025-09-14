from local_types import ErrorType
from utils import logger


class QueueJob:
    @staticmethod
    def publish_queue_post() -> None:
        try:
            print(1)
            pass

        except Exception as exc:
            logger.error(f"{ErrorType.QUEUE_JOB_ERROR}: {str(exc)}")

            return None
