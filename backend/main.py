from fastapi import FastAPI
from pydantic import BaseModel
from youtube.yt_search import GetYoutubeVideo
from utils import Generate_Response
from web_search.search import SearchQuery
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define the CORS settings
origins = [
    "http://127.0.0.1:3000",  # Allow requests from this origin
    "http://localhost:3000",  # Allow requests from localhost
    "http://localhost:3001",
    "http://localhost:3002",
    "https://campusxchatbot.s3.eu-north-1.amazonaws.com/frontend/index.html"
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
    print(query)
    
    # # Video Response
    youtube = GetYoutubeVideo(query=query)

    video_id = youtube.process_query()
    # print(video_id)
    
    # web response
    search=SearchQuery(query=query)
    response=search.get_results()

    # # Get the llm response
    llm_query={query:response}
    llm=Generate_Response(query=llm_query) 
    results=llm.response()

    return {"Response": [results,video_id]}