from fastapi import FastAPI
from pydantic import BaseModel
from utils import GetYoutubeVideo,Generate_Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define the CORS settings
origins = [
    "http://127.0.0.1:3000",  # Allow requests from this origin
    "http://localhost:3000",  # Allow requests from localhost
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


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
    
    # Video Response
    youtube = GetYoutubeVideo(query=query)

    final_url = youtube.process_query()

    # Textual Response
    text_response=Generate_Response(query=query)
    text=text_response.response()


    return {"Response": [text,final_url]}
