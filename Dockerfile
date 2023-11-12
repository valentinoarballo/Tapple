FROM python:3.9-alpine

COPY . /prog
WORKDIR /prog

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5055

ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["sh", "run.sh"]