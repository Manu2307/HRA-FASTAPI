import json
import logging

from fastapi import Request
from fastapi import Response, status
from fastapi.responses import JSONResponse

request_logger = logging.getLogger("RequestLogger")


async def logging_middleware(request: Request, call_next):
    log_params = {
        "path": request.url.path,
        "method": request.method,
    }
    # TODO: Add query params and path params

    request_logger.debug(json.dumps(log_params))
    try:
        response: Response = await call_next(request)
    except Exception as ex:
        response = JSONResponse(
            content={"Error": str(ex)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    # Do something with response here
    return response
