alias ds := dev-server
alias dc := dev-client

dev-server:
    cd server && poetry run python -m resume_generator.dev

dev-client:
    cd client && npm run dev

test: test-server

test-client:
    cd client && npm run test

test-server:
    cd server && poetry run pytest

test-server-debug:
    cd server && poetry run py.test --pdb

build:
    docker build --target=server --tag resgen_server .

install-dev:
    pip install -r requirements-dev.txt
    pre-commit install
    cd client && npm install
    cd server && poetry install
