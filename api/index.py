## This is the main file of API


## dependencies
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from mangum import Mangum 

from typing import Annotated, Dict
from model.ESP import predict_exam_score, VERSION, NAME
from schema.user_input import StudentInputDetails




## some crucial details
API_NAME = 'ESP-API'
API_VERSION = '1.0.0'
MODEL_VERSION: str = VERSION
MODEL_NAME: str = NAME





## creating instance of app
app = FastAPI(
    title = API_NAME,
    description = 'This API is for model predictions, it inputs 3 variables (check documentation) and return the predicted exam score',
    version = API_VERSION
)






# ========================================================== Creating Routes ================================================= #


## home route
@app.get("/")
def home() -> JSONResponse:
    ''' this is the home route '''
    content: Dict[str, str|Dict[str,str]] = {
        'message': 'Welcome in ESP (Exam Score Prediction) API',
        'more routes': {
            '/docs': 'Documentation of this API',
            '/health': 'Helps to check the working of API',
            '/predict': 'for prediction of exam score'
        }
    }
    return JSONResponse(status_code=200, content=content)






## health route
@app.get('/health')
def health_check() -> JSONResponse:
    ''' This function will check and display the valid working of model '''
    content: Dict[str, str|Dict[str, str]] = {
        'status':'OK',
        'version': MODEL_VERSION,
        'model loaded': predict_exam_score is not None
    }
    return JSONResponse(status_code=200, content=content)






## prediction route
@app.get("/api/predict")
def predict(user_input_data: Annotated[StudentInputDetails, Depends()]) -> JSONResponse:
    ''' This function will get the values and return the prediction '''

    ## extracting details 
    study_hrs: float = user_input_data.study_hrs
    exercise_frequency: int = user_input_data.exercise_frequency
    mental_health_rating: int = user_input_data.mental_health_rating

    ## prediction
    exam_score: float = predict_exam_score(study_hours=study_hrs, exercise_frequency=exercise_frequency, mental_health_rating=mental_health_rating)

    ## managing data for return
    data: Dict[str, str | float] = {
        'study hrs': study_hrs,
        'mental health rating': mental_health_rating,
        'exercise frequency': exercise_frequency,
        'predicted exam score': round(exam_score,2)
    }

    return JSONResponse(status_code=200, content=data)





handler = Mangum(app)



