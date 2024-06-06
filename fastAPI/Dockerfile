FROM python:3.10-bullseye

WORKDIR /opt/program

COPY ./server.py /opt/program/server.py
COPY ./requirements.txt /opt/program/requirements.txt

RUN pip3 install --no-cache-dir -r /opt/program/requirements.txt

CMD ["python3", "/opt/program/server.py"]