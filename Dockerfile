# Base Image
FROM python:3.10.6

# set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app  
    # importing requirements.txt seperatly because Docker cache everystep.
    # meaning that Docker don't have to install the dependecies everytime you change the code of your app. 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to the foler
COPY . /app

# expose port
EXPOSE 8000

CMD [ "uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000" ]