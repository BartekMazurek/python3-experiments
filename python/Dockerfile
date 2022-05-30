FROM python:3

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip

RUN pip install psutil
RUN pip install black

WORKDIR /home/python

CMD [ "python"]