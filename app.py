from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import Schema,fields
import requests
from . import create_app, database
from .models import Quizz

ENDPOIND = "https://jservice.io/api/random"

app = create_app()
db = SQLAlchemy(app)
ma = Marshmallow(app)

class QuizzSchema(ma.Schema):
    class Meta:
        fields = ("question", "answer")

@app.route('/', methods=['GET'])
def get_all_questions() -> json:
    """
        Return all questions and answers from database
    """
    all_questions = db.session.query(Quizz).all()
    serializer = QuizzSchema(many=True)
    data = serializer.dump(all_questions)
    return jsonify(data)


@app.route('/question_num/<int:number>',methods=['GET','POST'])
def add_questions(number: int) -> json:
    """
        Insert data from open api into database and return last record in JSON format.
    """

    def get_questions_from_api(number):
        params = {
            "count": number,
        }

        response = requests.get(url=ENDPOIND, params=params)
        response.raise_for_status()
        data_list = response.json() 
        return data_list

    data = get_questions_from_api(number)

    # Creating record
    for item in data:
        new_question = Quizz(
            question_id = item['id'],
            answer = item['answer'],
            question = item['question'],
            date = item['created_at']
        )
        
        # Checks if  question already exists in the table
        exists = db.session.query(Quizz).filter(Quizz.question_id == item['id']).scalar() is not None
        if exists:
            data = get_questions_from_api(number=1)
            for item in data:
                new_question = Quizz(
                    question_id = item['id'],
                    answer = item['answer'],
                    question = item['question'],
                    date = item['created_at']
                )

                new_question.save()
        else:
            new_question.save()

        # Shown last added question
        serializer = QuizzSchema()
        data = serializer.dump(new_question)

    return jsonify(data), 201