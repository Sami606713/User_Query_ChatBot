# This script is responsible for getting YouTube video details
from langchain_community.tools import YouTubeSearchTool
from urllib.parse import urlparse, parse_qs
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
load_dotenv()
import random


class GetYoutubeVideo:
    def __init__(self,query:str):
        self.query = query

    def search_videos(self):
        """
        This function fetches YouTube video links based on the user query.
        Input: Query (str)
        Output: List of video URLs
        """
        try:
            tool = YouTubeSearchTool()

            # Modify the query to include the channel name
            channel_name = "Code with Harry"
            search_query = f"{self.query} from channel {channel_name},5"

            # Run the search tool and get results
            response = eval(tool.run(search_query))

            # Ensure the response is a list of URLs
            if isinstance(response, list):
                return response
            else:
                raise ValueError("Unexpected response format from YouTubeSearchTool.")
        except Exception as e:
            return f"Error: {e}"

    def get_video_url(self,results:list):
        """
        This function extracts video IDs from a list of YouTube URLs.
        After extracting the video IDs, it returns a random ID.
        Input: List of video URLs
        Output: Random video ID (str)
        """
        try:
            video_ids = []

            for url in results:
                # Parse the URL to extract the video ID
                parsed_url = urlparse(url)
                query_params = parse_qs(parsed_url.query)
                video_id = query_params.get('v', [None])[0]

                if video_id:
                    video_ids.append(video_id)

            if not video_ids:
                raise ValueError("No valid video IDs found.")

            # Return a random video ID
            final_url=  f"https://www.youtube.com/watch?v={random.choice(video_ids)}"
            return final_url
        except Exception as e:
            return f"Error: {e}"


    def process_query(self):
        """
        This Fun is responsible for run all the necessray fun and return the final response
        """
        try:
            # search videos
            video_urls = self.search_videos()

            # get the final url
            final_url = self.get_video_url(results=video_urls)

            return final_url

        except Exception as e:
            return e


class Generate_Response:
    def __init__(self,query) -> None:
        self.query=query

    def _load_llm(self):
        """
        This fun is responsible for managing the llm
        """
        try:
            # Api key
            g_api=os.environ["GROQ_API_KEY"]
            # set the llm
            llm = ChatGroq(
                model="mixtral-8x7b-32768",
                temperature=0.0,
                max_retries=2,
                api_key=g_api,
            )
            return llm

        except Exception as e:
            return str(e)

    def make_prompt_template(self):
        """
        This Fun is managing the prompt template.
        """
        try:
            # make a prompt template for the model for langauage translation
            prompt = PromptTemplate(
                template = """
                    Role: You are an expert assistant specializing in providing clear, concise, and helpful responses to user queries.

                    Goal: Your primary objective is to address the user's query positively and effectively. You should ensure that the response is easy to understand and actionable.

                    Response Format: 
                    - If the response is long, present it in bullet points (maximum of 5 points) and each point will contain 10-15 words. 
                    - For shorter responses, keep it concise, within 2-3 sentences. 
                    - Always maintain a positive and straightforward tone.

                    Additional Note: Since the user might also receive video recommendations, ensure that the textual response complements the video by being engaging and supportive, focusing on delivering value to the user.

                    Query: {query}

                    Response:
                """,
                input_variables = ["query"]
            )
            return prompt
        except Exception as e:
            return str(e)


    def response(self):
        """
        This Fun is responsible for translate the text into target language.
        """
        try:
            # load the llm
            llm=self._load_llm()

            # load the prompt template
            prompt=self.make_prompt_template()
            
            # Format the prompt with input values
            formatted_prompt = prompt.format(query=self.query)
            # print(formatted_prompt)
            
            response=llm.invoke(formatted_prompt)

            return response.content
        except Exception as e:
            return str(e)
    
if __name__ == "__main__":
    query = "How KNN will Work"

    print("Getting Video....")
    youtube=GetYoutubeVideo(query=query)
    video_response = youtube.process_query()
    print(video_response)

    # Text response
    print("Getting Text....")
    text_response=Generate_Response(query=query)
    text=text_response.response()
    print(text)
