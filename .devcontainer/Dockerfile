FROM python:3.11-alpine

ENV DEBIAN_FRONTEND=noninteractive

RUN apk add --no-cache \
    git \
    build-base \
    && rm -rf /var/cache/apk/*

RUN pip install uv

WORKDIR /workspaces/mon-projet-uv

RUN uv venv

ENV PATH="/usr/local/bin:$PATH"