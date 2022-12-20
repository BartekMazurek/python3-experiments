FROM python:3

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3-pip

RUN pip install psutil
RUN pip install black
RUN pip install requests
RUN pip install pyright

WORKDIR /home/python

CMD [ "python"]
