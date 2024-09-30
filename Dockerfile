FROM python:3.8.10

WORKDIR /app/agent_mgt-inference_connector

COPY . .

RUN apt-get update \
    && apt-get install -y libpq-dev \
    && pip install -r /app/agent_mgt-inference_connector/requirements/local.txt