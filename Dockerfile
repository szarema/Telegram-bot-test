FROM python:3.8
ADD main.py /server/
WORKDIR /server/
RUN python3 -m pip install --user aiogram
