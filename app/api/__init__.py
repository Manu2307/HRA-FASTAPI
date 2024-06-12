from app.api.user import user_router
from app.api.questions import question_router
from app.api.responses import response_router
from app.api.result import result_router


API_ROUTERS = [
    (user_router, {'prefix': '/user'}),
    (question_router, {'prefix': '/question'}),
    (response_router, {'prefix': '/responses'}),
    (result_router, {'prefix': '/result'})
]
