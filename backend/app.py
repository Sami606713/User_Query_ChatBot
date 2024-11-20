from fastapi import FastAPI
from pydantic import BaseModel
from utils import GetYoutubeVideo

app = FastAPI()

# Define a model for the request body
class GetText(BaseModel):
    query: str

@app.get("/")
def home():
    return {"Home": "Welcome To Personal ChatBot"}

@app.post("/response")
def generate_response(input_data: GetText):
    """
    This endpoint processes the input text and returns a response.
    """
    # Process the input text
    query = input_data.query
    
    youtube = GetYoutubeVideo(query=query)

    final_url = youtube.process_query()

    return {"Video Url": final_url}
