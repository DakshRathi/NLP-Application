import paralleldots
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

api_key = os.getenv("API_KEY")  

class API:

    def __init__(self):
        paralleldots.set_api_key(api_key)

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        paralleldots.ner(text)

    def emotion_prediction(self,text):
        paralleldots.emotion(text)