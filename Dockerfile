FROM python:3

LABEL Owner="Winsala"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "python3", "within3.py" ]