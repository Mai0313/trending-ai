ARG PYTHON_VERSION=3.10
FROM nikolaik/python-nodejs:python${PYTHON_VERSION}-nodejs20 AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

LABEL maintainer="Wei Lee <mai@mai0313.com>" \
    org.label-schema.name="trending_ai" \
    org.label-schema.vendor="Wei Lee" \
    org.label-schema.schema-version="1.0" \
    com.centurylinklabs.watchtower.stop-signal="SIGINT"

# Install python packages
COPY ./docker/mirror/pip.conf /root/.pip/pip.conf
RUN git config --global http.sslVerify false && \
    python -m pip install --upgrade pip

########################################################################################

FROM builder AS base
WORKDIR /base
COPY ./pyproject.toml ./pyproject.toml
# RUN uv sync --frozen --no-dev && uv cache clean
RUN uv export --no-dev --no-hashes --output-file ./requirements.lock && \
    uv pip install --system -r requirements.lock && \
    uv cache clean

FROM builder AS dev
WORKDIR /base
COPY ./pyproject.toml ./pyproject.toml
# RUN uv sync --frozen && uv cache clean
RUN uv export --no-hashes --group docs --output-file ./requirements-dev.lock && \
    uv pip install --system -r ./requirements-dev.lock && \
    uv cache clean

########################################################################################

FROM base AS prod
WORKDIR /app
COPY . .

FROM dev AS docs
WORKDIR /app
COPY . .
RUN make gen-docs
