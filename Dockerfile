FROM node:20-alpine as client-build

WORKDIR /app
COPY client/package.json client/package-lock.json ./
RUN npm config set fetch-retry-mintimeout 100000 && npm config set fetch-retries 3 && npm config set fetch-retry-maxtimeout 600000
RUN npm ci --prefer-offline

COPY client/public ./public
COPY client/src ./src
COPY client/index.html client/vite.config.js ./

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

RUN apt-get update && \
    apt-get -y install --no-install-recommends pandoc texlive texlive-latex-extra texlive-latex-recommended texlive-extra-utils fonts-noto fonts-roboto fonts-font-awesome texlive-bibtex-extra biber latexmk make git procps locales curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    CLIENT_BUILD=/app/dist

COPY --from=client-build ${CLIENT_BUILD} ${CLIENT_BUILD}

COPY --from=server-build ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY server/data ./data

COPY server/resume_generator ./resume_generator

EXPOSE 8000

CMD ["python", "-m", "resume_generator.main"]
