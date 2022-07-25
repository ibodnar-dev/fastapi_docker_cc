FROM python:3.10.5-slim

WORKDIR /code

# TODO manage prod case
COPY ./infra/requirements/base.txt /code/base.txt
COPY ./infra/requirements/dev.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt && \
    adduser --disabled-password --no-create-home app-user

COPY ./app /code/app

USER app-user

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
