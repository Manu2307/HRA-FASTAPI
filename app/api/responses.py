from fastapi import APIRouter, status
from app.schema_models import CreateResponseRequest
from app.lib.exception_handler import error_handler
from app.service import ResponseService
from app.schema_models.response_schema import CreateResponseResponse
from fastapi.logger import logger


response_router = APIRouter()


@response_router.post('/create', response_model=CreateResponseResponse, status_code=status.HTTP_201_CREATED,
                      tags=['Responses'])
@error_handler
async def create_user_responses(user_data: CreateResponseRequest):
    logger.info("API called - /responses/create")
    response = ResponseService.create_user_responses(user_data)

    return {"response": response}


