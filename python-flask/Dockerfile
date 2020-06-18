FROM keybaseio/client:stable-python

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install connexion[swagger-ui]

COPY . /usr/src/app

EXPOSE 8080

# uses tini's entrypoint
# CMD ["python3", "sample.py"]
CMD ["python3", "-m", "swagger_server"]