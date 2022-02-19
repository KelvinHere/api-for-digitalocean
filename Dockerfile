FROM python:3.11.0a5-alpine3.15

RUN pip3 install --upgrade pip

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt \
    && pip3 install djangorestframework

COPY ./myapp /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]