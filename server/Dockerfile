FROM alpine:3.7

RUN apk add --no-cache py3-pip

RUN pip3 install --upgrade pip
RUN pip install virtualenv

# EXPOSE 8080
COPY app.py /usr/src/

WORKDIR /usr/src
RUN chmod a+x app.py

# Install local dependencies
RUN virtualenv flask
RUN flask/bin/pip install flask
RUN flask/bin/pip install flask-cors

EXPOSE 5000

ENTRYPOINT ["/usr/src/app.py"]
