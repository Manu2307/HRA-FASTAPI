from fastapi import APIRouter, status
from app.schema_models import CreateCombinationResponse
from app.lib.exception_handler import error_handler
from app.schema_models import (CreateCombinationRequest, CreateBunchCombinationRequest,
                               CreateBunchCombinationResponse)
from fastapi.logger import logger
from app.service.result_service import ResultService
from uuid import UUID


result_router = APIRouter()


@result_router.post('/create/combination', response_model=CreateCombinationResponse,
                    status_code=status.HTTP_201_CREATED, tags=['Conclusion'])
@error_handler
async def create_conclusion(create_data: CreateCombinationRequest):
    logger.info('API called - /result/create/combination')
    response = ResultService.create_combination(create_data)

    return response


@result_router.post('/create/combination/bunch', response_model=CreateBunchCombinationResponse,
                    status_code=status.HTTP_201_CREATED, tags=['Conclusion'])
@error_handler
async def create_bunch_combinations(create_data: CreateBunchCombinationRequest):
    logger.info('API called - /result/create/combination/bunch')
    response = ResultService.create_bunch_combinations(create_data.data)

    return {'response': response}


@result_router.get('/get/conclusion', status_code=status.HTTP_200_OK, tags=['Conclusion'])
@error_handler
async def get_conclusion(user_id: UUID):
    logger.info("API called - conclusion/get/result")
    response = ResultService.get_conclusion(user_id)

    return response
