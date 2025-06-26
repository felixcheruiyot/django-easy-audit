import logging
from easyaudit.models import RequestEvent, CRUDEvent, LoginEvent

logger = logging.getLogger(__name__)


class ModelBackend:

    def request(self, request_info):
        try:
            return RequestEvent.objects.create(**request_info)
        except Exception as e:
            logger.error(f"Error creating RequestEvent: {e}")
            return None

    def crud(self, crud_info):
        try:
            return CRUDEvent.objects.create(**crud_info)
        except Exception as e:
            logger.error(f"Error creating CRUDEvent: {e}")
            return None

    def login(self, login_info):
        try:
            return LoginEvent.objects.create(**login_info)
        except Exception as e:
            logger.error(f"Error creating LoginEvent: {e}")
            return None