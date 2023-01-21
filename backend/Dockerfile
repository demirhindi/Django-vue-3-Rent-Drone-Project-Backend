FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /alpine

COPY ./requirements.txt .
RUN pip install --no-cache --upgrade pip
RUN pip install --no-cache -r requirements.txt

COPY . .
EXPOSE 8000


