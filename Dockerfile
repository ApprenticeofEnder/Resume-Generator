FROM node:18-alpine as client-build

WORKDIR /app
COPY client/package.json client/package-lock.json ./
# RUN npm config set fetch-retry-mintimeout 100000 && npm config set fetch-retries 3 && npm config set fetch-retry-maxtimeout 600000 && npm config set cache-min 3600

RUN npm ci

RUN npm run build

FROM python:3.11-bookworm as server-build

RUN pip install poetry==1.6.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY server/pyproject.toml server/poetry.lock ./

RUN touch README.md

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

FROM python:3.11-slim-bookworm as server

WORKDIR /tmp

RUN apt update && apt install wget

RUN wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz

RUN zcat < install-tl-unx.tar.gz | tar xf -

RUN cd install-tl-*

RUN perl ./install-tl --no-interaction

RUN apk add font-awesome

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    CLIENT_BUILD=/app/build

COPY --from=client-build ${CLIENT_BUILD} ${CLIENT_BUILD}

COPY --from=server-build ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY server/resume_generator ./resume_generator

RUN ["python", "-m", "resume_generator"]

