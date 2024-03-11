from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.schema_models import CreateUserRequest, CreateUserResponse
from app.service import UserService
from app.lib.custom_exceptions import DuplicateRecordError, CreateRecordException, DBFetchFailureException
from uuid import UUID

user_router = APIRouter()


@user_router.post('/register', response_model=CreateUserResponse, status_code=status.HTTP_201_CREATED)
async def register(register_data: CreateUserRequest):
    try:
        user_details = UserService.register_user(register_data)

    except DuplicateRecordError as ex:
        return JSONResponse(content={'error': str(ex)}, status_code=status.HTTP_409_CONFLICT)

    except CreateRecordException as ex:
        return JSONResponse(content={'error': str(ex)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except DBFetchFailureException as ex:
        return JSONResponse(content={'error': str(ex)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as ex:
        return JSONResponse(content={'error': 'An error has occured while processing your request'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return user_details


@user_router.get('/get/{user_id}', response_model=CreateUserResponse, status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: UUID):
    try:
        user_details = UserService.get_user_by_id(user_id)

    except DBFetchFailureException as ex:
        return JSONResponse(content={'error': str(ex)},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as ex:
        return JSONResponse(content={'error': 'An error has occured while processing your request'},
                            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return user_details


@user_router.get('/get/{email_id}', response_model=CreateUserResponse, status_code=status.HTTP_200_OK)
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
