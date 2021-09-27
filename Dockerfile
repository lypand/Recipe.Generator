FROM ubuntu

RUN apt-get update -y 
RUN apt-get install  python3.8 -y
RUN apt-get install python3-pip -y
RUN pip3 install flask
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]