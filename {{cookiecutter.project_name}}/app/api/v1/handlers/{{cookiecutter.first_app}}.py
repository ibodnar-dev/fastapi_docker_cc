from fastapi import APIRouter


router = APIRouter()


@router.get('/')
def handler():
    return {'response': '{{cookiecutter.first_app}}'}
