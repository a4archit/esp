'''
    In this file we built pydantic models for data validation
'''




## dependencies
from pydantic import Field, BaseModel
from typing import Annotated




## creating objects of pydantic
class StudentInputDetails(BaseModel):

    ## defining variables

    study_hrs: Annotated[float, Field(
        ..., 
        title = 'Study hours', 
        description = 'How many hours student study in a day', 
        min = 0, 
        max = 24
    )]


    exercise_frequency: Annotated[int, Field(
        ..., 
        title = 'Exercise Frequency', 
        description = 'How many times student do exercise in a day (mostly 1 to 6)', 
        min=0
    )]


    mental_health_rating: Annotated[int, Field(
        ..., 
        title = 'Mental health rating', 
        description = 'Rating of mental health basically between 1 to 10', 
        min = 1, 
        max = 10
    )]


