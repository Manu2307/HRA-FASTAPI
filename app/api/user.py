from fastapi import APIRouter, status
from uuid import UUID
from fastapi.responses import JSONResponse
from app.schema_models import RegisterUserRequest, CreateUserResponse
from app.service import UserService
from app.lib.custom_exceptions import DBFetchFailureException
from app.lib.exception_handler import error_handler
from fastapi.logger import logger


user_router = APIRouter()


@user_router.post('/register', response_model=CreateUserResponse, status_code=status.HTTP_201_CREATED,
                  tags=['User'])
@error_handler
async def register(register_data: RegisterUserRequest):
    logger.info("API Called - /user/register")
    user_details = UserService.register_user(register_data)

    return user_details


@user_router.get('/get_by_id/{user_id}', response_model=CreateUserResponse, status_code=status.HTTP_200_OK,
                 tags=['User'])
async def get_user_by_id(user_id: UUID):
    try:
        user_details = UserService.get_user_by_id(user_id)

    except DBFetchFailureException as ex:
        return JSONResponse(content={'error': str(ex)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as ex:
        return JSONResponse(content={'error': 'An error has occured while processing your request'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # return JSONResponse(content={'data': user_details}, status_code=status.HTTP_200_OK)
    return user_details


@user_router.get('/get_by_email/{email_id}', response_model=CreateUserResponse, status_code=status.HTTP_200_OK,
                 tags=['User'])
async def get_user_by_email_id(email_id: str):
    try:
        user_details = UserService.get_user_by_email_id(email_id)

    except DBFetchFailureException as ex:
        return JSONResponse(content={'error': str(ex)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as ex:
        return JSONResponse(content={'error': 'An error has occured while processing your request'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return user_details
