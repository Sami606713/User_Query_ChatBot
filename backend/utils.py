# from langchain_groq import ChatGroq
# from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain
# import os
# from dotenv import load_dotenv
# load_dotenv()
# import random

# class Generate_Response:
#     def __init__(self,query) -> None:
#         self.query=query

#     def _load_llm(self):
#         """
#         This fun is responsible for managing the llm
#         """
#         try:
#             # Api key
#             g_api=os.environ["GROQ_API_KEY"]
#             # set the llm
#             llm = ChatGroq(
#                 model="mixtral-8x7b-32768",
#                 temperature=0.0,
#                 max_retries=2,
#                 api_key=g_api,
#             )
#             return llm

#         except Exception as e:
#             return str(e)

#     def make_prompt_template(self):
#         """
#         This Fun is managing the prompt template.
#         """
#         try:
#             # make a prompt template for the model for langauage translation
#             prompt = PromptTemplate(
#                 template = """
#                     Role: You are an expert assistant specializing in providing clear, concise, and helpful responses to user queries Do not write any piece of code only return text..

#                     Goal: Your primary objective is to address the user's query positively and effectively. You should ensure that the response is easy to understand and actionable.

#                     Response Format: 
#                     - If the response is long, present it in bullet points (maximum of 5 points) and each point will contain 10-15 words. 
#                     - For shorter responses, keep it concise, within 2-3 sentences. 
#                     - Always maintain a positive and straightforward tone.

#                     Additional Note: Since the user might also receive video recommendations, ensure that the textual response complements the video by being engaging and supportive, focusing on delivering value to the user.

#                     Query: {query}

#                     Response:
#                 """,
#                 input_variables = ["query"]
#             )
#             return prompt
#         except Exception as e:
#             return str(e)

#     def response(self):
#         """
#         This Fun is responsible for translate the text into target language.
#         """
#         try:
#             # load the llm
#             llm=self._load_llm()

#             # load the prompt template
#             prompt=self.make_prompt_template()
            
#             # Format the prompt with input values
#             formatted_prompt = prompt.format(query=self.query)
#             # print(formatted_prompt)
            
#             response=llm.invoke(formatted_prompt)

#             return response.content
#         except Exception as e:
#             return str(e)

# if __name__ == "__main__":
#     query = "Which Course is related to Computer Vison?"

#     # Text response
#     print("Getting Text....")
#     text_response=Generate_Response(query=query)
#     text=text_response.response()
#     print(text)



# =========================================Second try===================================#
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
load_dotenv()
import random

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
                    Role: You are an expert assistant specializing in clear, concise, and actionable responses to user queries. Avoid writing code; focus solely on providing text-based guidance.

                    Objective: Address the user's query effectively, ensuring the response is:
                    - Easy to understand.
                    - Positive and actionable.
                    - User-focused.

                    Response Guidelines:
                    1. **Format for Longer Responses:**
                    - Present the response in bullet points (max 5 points).
                    - Each point should contain 10-15 words for clarity.
                    2. **Format for Shorter Responses:**
                    - Keep it concise (2-3 sentences).
                    3. **Tone:**
                    - Always maintain a positive, engaging, and helpful tone.

                    Input Details:
                    - **Url:** Includes the relevant URL for context.
                    - **Content:** Describes the content of the URL.

                    Response Structure:
                    - **Query Response:** Directly address the user query and provide the answer with in the input content.
                    - **Additional URLs:** Provide important and relevant URLs to complement the response.
                    - ```Note:``` Use the provided input to provide the answer and must provide the necessary URLs.

                    Additional Note:
                    - If video recommendations are involved, ensure the textual response enhances the video's value, focusing on user engagement and utility.

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
    query = "Which Course is related to Computer Vison?"

    # Text response
    print("Getting Text....")
    text_response=Generate_Response(query=query)
    text=text_response.response()
    print(text)

