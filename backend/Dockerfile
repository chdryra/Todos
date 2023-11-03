FROM python:3.10

WORKDIR /backend

COPY requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY app /backend/app

CMD  cd app && python -m api_server --ip 0.0.0.0 --port 80
