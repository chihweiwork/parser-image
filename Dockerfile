from python:3.10

WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && pip install --upgrade pip \
    && poetry install --no-dev

COPY . /code/

CMD ["ls"]
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--conf", "gunicorn_conf.py", "--bind", "0.0.0.0:80", "code.app:app"]
