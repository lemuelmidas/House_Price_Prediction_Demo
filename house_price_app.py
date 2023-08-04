from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
#from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.exceptions import SessionClosedException
import pandas as pd
import pickle
import warnings
import argparse

#app= Flask(__name__)

warnings.filterwarnings("ignore")



with open('final_model.pkl', 'rb') as f:
    model= pickle.load(f)

#with open('columns.pkl', 'rb') as f:
#    model_columns= pickle.load(f)
    
def prediction(prediction_df):
    model = pickle.load(open('final_model.pkl', 'rb'))
    query= pd.DataFrame(prediction_df, index= [0])
    result=list(model.predict(query))
    final_result= int(result[0])
    
    return final_result

def values():
    #input_group("Dementia Prediction")
    put_markdown(
    
    '''
    Real Estate Price Prediction Web App
    '''
    , lstrip=True
    )
    
    model_inputs= input_group(
    "Real Estate Price Prediction",
    [
        select("Choose a location", name='location', options= [('Lagos', 1), ('Abuja', 2), ('Rivers', 3), ('Kaduna', 4), ('Akwa-Ibom', 5), ('Delta', 6)]),
        
        select("Type of house", name='title', options= [('Flat', 1), ('Apartment', 2), ('Townhouse', 3), 
                                                        ('Mansion', 4), ('Detached duplex', 5), ('Penthouse', 6),
                                                       ('Semi-detached duplex', 7), ('Bungalow', 8),
                                                        ('Terrace duplex', 9), ('Cottage', 10)]),
        input("Number of Bedrooms", name= 'bedroom', type= FLOAT),
        input("Number of Bathrooms", name= 'bathroom', type= FLOAT),
        input("Number of parking_space", name= 'parking_space', type= FLOAT),
        
    ])
    
    
    prediction_df= pd.DataFrame(data= [[model_inputs[i] for i in ['location', 'title', 'bedroom', 'bathroom', 'parking_space']]],
                               columns= ['location', 'title', 'bedroom', 'bathroom', 'parking_space'])
    
    House_Price= prediction(prediction_df)
    #prediction_text=''
    
    put_markdown("## Your dream house costs %d naira only." % (House_Price))


#app.add_url_rule('/tool', 'webio_view', webio_view(values), methods=['GET', 'POST','OPTIONS'])
    
    
if __name__== '__main__':
    parser= argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type= int, default= 8080)
    args= parser.parse_args()
        
    start_server(values, port= args.port)
    
    
    
    
    
  
    
        
        
    
#if __name__== "__main__":
#    try:
#        values()
#    except SessionClosedException:
#        print("The session was closed unexpectedly")
    
    
        
        
    
        
        
        
        
