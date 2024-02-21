FROM python:3.10 

WORKDIR /bot
ADD . /bot/

RUN python3 -m venv /opt/venv
RUN  pip install --upgrade pip
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

CMD . /opt/venv/bin/activate && exec python3 -u main.py