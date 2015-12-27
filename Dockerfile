FROM python:3.5

ADD ./requirements.txt /src/
RUN cd /src/ && pip install -r requirements.txt

ADD . /src/
WORKDIR /src

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--reload", "-b", "0.0.0.0:5000", "app:api"]
