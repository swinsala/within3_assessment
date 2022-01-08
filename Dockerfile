FROM python:3

LABEL Owner="Winsala"

WORKDIR /usr/app/src

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV LISTEN_PORT=5000
EXPOSE 5000

CMD [ "python3", "within3.py" ]