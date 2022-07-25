from fastapi import APIRouter


router = APIRouter()


@router.get('/{{cookiecutter.first_app}}/')
def handler():
    return {'response': '{{cookiecutter.first_app}}'}
