

## dependencies
from flask import Flask, render_template, request, jsonify
from typing import Annotated, Dict
from model.ESP import predict_exam_score, VERSION, NAME
from schema.user_input import StudentInputDetails






## some crucial details
API_NAME = 'ESP-API'
API_VERSION = '1.0.0'
MODEL_VERSION: str = VERSION
MODEL_NAME: str = NAME




## creating app instance
app = Flask(__name__)




## -------------------------------------------- home page --------------------------------------------- #

@app.route("/")
def home_page():
    ''' This function will render the home HTML page when user fill form '''
    return render_template('home.html')




@app.route("/home", methods=['GET','POST'])
def home():
    ''' This function will render the home HTML page when user fill form '''

    ## extracting values from form
    try:
        study_hrs = float(request.form['study-hrs'])
        exercise_frequency = int(request.form['exercise-frequency'])
        mental_health_rating = int(request.form['mental-health-rating'])

    except Exception as e:
        # this is a heuristic method
        # without this our code will be not work
        if (str(e).startswith('400')):
            return render_template('home.html', message="")
        
        error_details: Dict[str,str] = {
            'exception occur': str(e),
            'message': 'any input type mismatch'
        }
        return jsonify(error_details)
    
    ## predicting exam score
    predicted_exam_score: float = predict_exam_score(
        exercise_frequency = exercise_frequency,
        study_hours = study_hrs,
        mental_health_rating = mental_health_rating
    )

    ## defining message that will be direct seen by the user
    message = f"You will achieve around {round(predicted_exam_score,2)}% in your exam."

    return render_template('home.html', message=message)







## --------------------- API -------------------- ##
@app.route('/api')
def api() -> jsonify:
    ''' This function contains script for API '''

    ## defining queries
    try:
        study_hrs = float(request.args.get('sh'))
        exercise_frequency = int(request.args.get('ef'))
        mental_health_rating = int(request.args.get('mhr'))

    except TypeError:
        data: Dict[str,str] = {
            'msg': "Invalid query!",
            'details': "valid queries are 'sh', 'ef' and 'mhr' "
        }
        return jsonify(data)

    
    ## predicting exam score
    exam_score = round(
        predict_exam_score(
            study_hours = study_hrs, 
            exercise_frequency = exercise_frequency, 
            mental_health_rating = mental_health_rating
        ), 2)

    ## managing data for return
    data: Dict[str, str | float] = {
        'predicted exam score': exam_score,
        'input details': {
            'study hrs': study_hrs,
            'mental health rating': mental_health_rating,
            'exercise frequency': exercise_frequency
        }
    }

    return jsonify(data)












if __name__ == "__main__": # --------------------------------------------------------------------------- Main execution 

    ## running flask app
    app.run(debug=True)





