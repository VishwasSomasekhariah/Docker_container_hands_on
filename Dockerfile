# comments start with a hashtag

# we will be using the python:3 image for our container.
FROM python:3

# we set the working directory for our application.
WORKDIR /usr/src/app

# we copy the requirements file to the working directory (shown here as ./)
COPY requirements.txt ./

# we install all of the requirements/dependencies
RUN pip install --no-cache-dir -r requirements.txt

# the contents of the working directory (host) are copied into the image (container).
COPY . .

# this command tells our image to start the flask webserver at port 8888.
CMD [ "python", "./Code_for_docker_hands_on.py" ]
