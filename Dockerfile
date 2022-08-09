FROM python:3.10.4-alpine3.16

WORKDIR /webapp

COPY static/ static/
COPY templates/ templates/
COPY app.py app.py
COPY LICENSE LICENSE
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
