FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN echo "Running Docker installing requirements";
RUN pip3 install -U pip
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt
RUN echo "all requirements installed now starting the file";
CMD python3 start.py
