from fastapi import APIRouter

from .handlers import {{cookiecutter.first_app}}_router


api_router = APIRouter()

api_router.include_router({{cookiecutter.first_app}}_router, tags={'{{cookiecutter.first_app}}'})
