from fastapi import APIRouter, status
from app.lib.exception_handler import error_handler
from app.schema_models import (CreateQuestionRequest, CreateQuestionResponse, CreateQuestionsRequest,
                               UpdateQuestionRequest, CreateQuestionsResponse)
from fastapi.logger import logger
from app.service import QuestionService
from fastapi import Path
from typing import List
from uuid import UUID


question_router = APIRouter()


@question_router.post('/create', response_model=CreateQuestionResponse, status_code=status.HTTP_201_CREATED,
                      tags=['Questions'])
@error_handler
async def create_question(question_data: CreateQuestionRequest):
    response = QuestionService.create_question(question_data)

    return response


@question_router.post('/create/bunch', response_model=CreateQuestionsResponse, status_code=status.HTTP_201_CREATED,
                      tags=['Questions'])
@error_handler
async def create_bunch_of_question(questions: CreateQuestionsRequest):
    logger.info("API called - question/create/bunch")
    response = QuestionService.create_bunch_of_questions(questions.data)

    return {"response": response}


@question_router.get('/get_by_id/{question_id}', response_model=CreateQuestionResponse,
                     status_code=status.HTTP_200_OK, tags=['Questions'])
@error_handler
async def get_questions_by_id(question_id: UUID = Path(..., example="123e4567-e89b-12d3-a456-426614174000")):
    response = QuestionService.get_question_by_id(question_id)

    return response


@question_router.get('/get_by_type/{question_type}', response_model=List[CreateQuestionResponse] ,
                     status_code=status.HTTP_200_OK, tags=['Questions'])
@error_handler
async def get_questions_by_type(question_type: str = Path(..., min_length=3, max_length=55,
                                                          example="Nutrition")):
    response = QuestionService.get_questions_by_type(question_type)

    return response


@question_router.put('/update/{question_id}', response_model=CreateQuestionResponse,
                     status_code=status.HTTP_200_OK, tags=['Questions'])
@error_handler
async def update_question(update_data: UpdateQuestionRequest, question_id: UUID = Path(...)):
    response = QuestionService.update_question(update_data, question_id)

    return response
