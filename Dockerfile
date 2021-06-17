# set base image (host OS)
#FROM ubuntu:18.04
FROM python:3.8

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY /requirements.txt /app/requirements.txt

# install dependencies
RUN pip install -r /app/requirements.txt --no-cache-dir


# copy the content of the local src directory to the working directory
COPY . /app

# command to run on container start
CMD [ "python", "/app/main.py" ]

#how to run
#docker build -t telegram_bot .
#docker run -it --name bot --rm telegram_bot