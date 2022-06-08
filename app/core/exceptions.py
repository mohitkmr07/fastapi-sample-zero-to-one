from http import HTTPStatus
from typing import Optional

from starlette.responses import JSONResponse


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class RequestError(Error):
    def __init__(self, status_code: int, error_code: str, error_msg: Optional[str] = None):
        self.status_code = HTTPStatus(status_code)
        self.error_code = error_code
        self.error_msg = error_msg


ERROR = "error"
TYPE = "type"
CODE = "code"
ERROR_CODE = "error_code"
MESSAGE = "message"
STATUS_CODE = "status_code"
HTTP_STATUS_CODE = "http_status_code"
REQUEST_ID = "request_id"
MSG = "msg"
LOC = "loc"
BODY = "body"
QUERY = 'query'
INVALID_REQUEST = "invalid request"
PERMITTED = "permitted: "
INVALID_LIST = "not a valid list"
FIELD_REQUIRED = "field required"
AT_LEAST_1 = "at least 1"

# error_status_type = {
#     HTTPStatus.BAD_REQUEST: ErrorStatus.INVALID_REQUEST_PARAMETERS,
#     HTTPStatus.NOT_FOUND: ErrorStatus.RECORD_NOT_FOUND,
#     HTTPStatus.UNAUTHORIZED: ErrorStatus.UNAUTHORIZED_REQUEST,
#     HTTPStatus.FORBIDDEN: ErrorStatus.FORBIDDEN_REQUEST,
#     HTTPStatus.TOO_MANY_REQUESTS: ErrorStatus.RATE_LIMIT
# }


class RequestErrorHandler:
    def __init__(self, exc: RequestError):
        self.error_code = exc.error_code
        self.status_code = exc.status_code
        self.error_msg = exc.error_msg
        # self.request_id = get_correlation_id()

    def process_message(self):
        return JSONResponse(
            status_code=self.status_code,
            content={
                # TODO: Remove CODE and STATUS_CODE in release v1.11.0
                ERROR: {
                    TYPE: self.status_code,
                    CODE: self.error_code,
                    ERROR_CODE: self.error_code,
                    MESSAGE: self.error_msg,
                    STATUS_CODE: self.status_code,
                    HTTP_STATUS_CODE: self.status_code,
                    # REQUEST_ID: self.request_id
                }
            }
        )
