from app.api.user import user_router

API_ROUTERS = [
    (user_router, {'prefix': '/user'}),
]
