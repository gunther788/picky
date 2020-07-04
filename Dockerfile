FROM keybaseio/client:stable-python-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install connexion[swagger-ui]

COPY . /usr/src/app

COPY ./defaults /data
VOLUME /data

EXPOSE 5000

COPY entrypoint.sh /usr/bin/entrypoint.sh

# uses tini's entrypoint
CMD ["sh", "-x", "startup.sh" ]
