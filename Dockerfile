FROM python:3.12.2
WORKDIR /DiabloTarotBot
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
