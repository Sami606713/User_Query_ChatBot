# This Scripts is responsible for Web search
from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv
import os
load_dotenv()

tool = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True,
    include_domains=['https://learnwith.campusx.in'],
    name="CampusX Tool Search"
)

class SearchQuery:
    def __init__(self,query) -> None:
        self.query=query
        self.tavily_api_key=os.getenv("TAVILY_API_KEY")


    def search_tool(self):
        tool = TavilySearchResults(
            max_results=5,
            search_depth="advanced",
            include_answer=True,
            include_raw_content=True,
            include_images=True,
            include_domains=['https://learnwith.campusx.in'],
            name="CampusX Tool Search",
            tavily_api_key=self.tavily_api_key
        )
        return tool
    
    def get_results(self):
        """
        This fun is responsible for getting the results.
        """
        try:
            tool=self.search_tool()

            results=tool.invoke({
                "query":self.query
            })

            return results
        except Exception as e:
            return e
    
if __name__=="__main__":
    query="How we can enroll in deep learning for computer vision course?"

    search=SearchQuery(query=query)
    results=search.get_results()

    print(results)