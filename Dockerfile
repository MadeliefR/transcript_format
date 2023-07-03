# Base Image
FROM pyton:3.10.6

# set the working directory
WORKDIR /app

# install dependencies
RUN ["apt-get", "update", "-y"]
RUN apt-get install -y python3

COPY ./requirements.txt /app  
    # importing requirements.txt seperatly because Docker cache everystep.
    # meaning that Docker don't have to install the dependecies everytime you change the code of your app. 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the foler
COPY . /app