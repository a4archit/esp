'''
                                    ESP (Exam Score Predictor)
                                    =========================

    ESP is a Machine Learning model that predicts the students Exam Score (precentage) that will be student gain.
    It is a toy project I'm working on it to understand the integration of ML models and the API also I'll try 
    any deploy platform for this.



'''



## dependencies
import pickle
import pandas as pd
import os

from typing import Dict, Annotated





## global variables
NAME = 'ESP-01'
VERSION = '1.0.0'





## importing some useful files ------------------------------------------------------------------ #

## getting current working directory
current_dir: str = os.getcwd()

## updating files path 
scaler_path = os.path.join(current_dir, 'model/scaler.pkl')
model_path = os.path.join(current_dir, 'model/model.pkl')

## loading models
scaler = pickle.load(open(scaler_path,'rb'))
knn = pickle.load(open(model_path,'rb'))







# -------------------------------- Main Class ------------------------------- #

class ExamScorePredictor:
    
    """ 
    
    Introduction:
    =============
    
        This is the class that contains the usefull functions for predicting the exam score 
        of an college student 



    Why this?
    ========

        I built this project to practice my skills, i.e., API development, Site Integration
        and successful deplyoment to the server.
        
    """


    MODEL_NAME = NAME
    VERSION = VERSION



    ## function (01)
    def predict(self,
                exercise_frequency: Annotated[int, '0 to 6'],
                mental_health_rating: Annotated[int, '1 to 10'],
                study_hours: float
                
               ) -> float | None :
        

        """ This function will predict the Exam Score of student """

        ## Note: we are not checking (validating) the parameters (because our focus on other tech regarding this project)

        ## creating dictionary of input values
        user_data: Dict[str, str] = {
    		'study_hours_per_day': study_hours,
    		'exercise_frequency': exercise_frequency,
    		'mental_health_rating': mental_health_rating
        }
        

        ## converting user provided details into pandas dataframe
        xdf = pd.DataFrame(user_data, index=[1])

        ## scaling
        scaled_data = scaler.transform(xdf)

        ## predicting
        prediction_knn = knn.predict(scaled_data)

        return prediction_knn[0]
        

        





## predictable another method
def predict_exam_score(
        exercise_frequency: Annotated[int, '0 to 6'],
        mental_health_rating: Annotated[int, '1 to 10'],
        study_hours: float
    ) -> float:

    ''' This function will provide an interface that will cover all the machine learning concepts in its own '''

    ## creating model instance
    esp = ExamScorePredictor()
    predicted_exam_score = esp.predict(
                exercise_frequency = exercise_frequency,
                mental_health_rating = mental_health_rating,
                study_hours = study_hours
    )

    return predicted_exam_score








if __name__ == "__main__": # ------------------------------------------------------------------- Main execution
    
    esp = ExamScorePredictor()
    predicted_exam_score = esp.predict(
                exercise_frequency = 1,
                mental_health_rating = 7,
                study_hours = 4
    )

    print(predicted_exam_score)







