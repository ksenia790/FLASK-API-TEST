FROM python:3.9.1-alpine

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip 
COPY  . . 
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 5432

# CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]