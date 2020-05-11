FROM alpine:3.7

RUN apk add --no-cache py3-pip

RUN pip3 install --upgrade pip

COPY app.py requirements.txt /usr/src/

WORKDIR /usr/src
RUN chmod a+x app.py

RUN pip install -r requirements.txt

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

ENTRYPOINT ["flask", "run"]
