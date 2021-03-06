<h1 align='center'>FLASK API(Flask+SQLAlchemy+PostgreSQL)</h1>
<p> In this project was implemented simple web service using Flask, SQLAlchemy and PostrgeSQL tools which performs the following functions: </p>
<ul>
  <li>implemented REST API that accepts POST requests as input;</li>
  <li>saving query data to database;</li>
  <li>API method to get last question from last query;</li>
  <li>API method to get all data from database.</li>
</ul>
<h2 align='center'>Fast start with Docker-compose</h2>
This instractions assume that you have already installed Docker and Docker Compose.
In order to get started be sure to clone this project.

## How to get up and running
Once you've cloned the project navigate to the root directory of the project. Run the following commands from this directory:

1. Edit ` config.py ` accordin to your user-name and password from Postgres.

2. ` docker-compose up -d `

The docker-compose command will build the images from dockerfile and docker-compose.yml file. This will create ports, links between containers, and configure applications as requrired. After the command completes we can now view the status of our stack

3. ` docker-compose ps `

And finally run the web-server:

4. ` docker-compose run web_run `

Follow API DOCUMENTATION below.

## How to get started if you don't have docker or docker-compose
1. Clone the project
2. Edit ` config.py ` accordin to your user-name and password from Postgres.
3. Instal all requirements ` pip install -r requirements.txt `
4. Provide the "FLASK_APP" environment variable ` set FLASK_APP=model.py `
5. Run the app ` flask run `

Follow API DOCUMENTATION below.

<h2 align='center'>API DOCUMENTATION<h2>

## Avalible API methods for blog posts:
 
**GET** ` / ` - Retrieve All Questions And Answers from Database
 <br>
**POST** ` /question_num/<int:number> ` - Pulling Requested Number Of Questions From Public API And Loads Them Into The Database. After Displays last question was loaded.
 <br>
