FROM node:24-alpine

RUN apk add --no-cache \
    python3 py3-pip \
    gcc musl-dev python3-dev \
    libffi-dev openssl-dev \
    su-exec tini tzdata

RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel \
    && /opt/venv/bin/pip install --no-cache-dir prefect

RUN npm install -g n8n@latest

RUN mkdir -p /home/node/.n8n /scripts \
    && chown -R node:node /home/node/.n8n /scripts

ENV PATH="/opt/venv/bin:$PATH"

USER node
WORKDIR /home/node
EXPOSE 5678

ENTRYPOINT ["tini", "--", "n8n"]