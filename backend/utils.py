# This script is responsible for getting YouTube video details
from langchain_community.tools import YouTubeSearchTool
from urllib.parse import urlparse, parse_qs
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
            # channel_name = "Code with Harry"
            channel_name = "CampusX"
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
        pass
if __name__ == "__main__":
    query = "learn  python in one shot"

    youtube=GetYoutubeVideo(query=query)
    response = youtube.process_query()
    print(response)
