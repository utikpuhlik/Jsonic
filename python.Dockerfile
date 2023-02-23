FROM python:3.10

WORKDIR /opt/app

ADD pyproject.toml /opt/app

# Poetry
ENV PATH="${PATH}:/root/.poetry/bin"

RUN : \
&& pip install poetry \
&& POETRY_VIRTUALENVS_CREATE=false poetry install \
&& poetry install \
&& :

# To COPY the remote files at working directory in container
COPY ./api /opt/app/api
COPY ./poetry.lock /opt/app
COPY ./pyproject.toml /opt/app

# Now the structure looks like this '/opt/app/app.py'
CMD ["python", "api/app.py"]