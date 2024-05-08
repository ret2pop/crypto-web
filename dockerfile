FROM python:latest


LABEL Maintainer="ret2pop"
EXPOSE 8888/tcp

WORKDIR /usr/app/src

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY main.py ./
COPY templates/index.html ./templates/
COPY static/style.css ./static/


CMD [ "python", "./main.py" ]
