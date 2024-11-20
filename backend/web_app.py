import streamlit as st
import requests

# Define FastAPI Backend URL
FASTAPI_URL = "http://127.0.0.1:8000/response"

# Streamlit UI
st.title("YouTube Video Finder")
st.subheader("Get a YouTube video based on your query")

# Input Section
user_query = st.chat_input("Enter your query:")

# Button to Trigger Backend API Call
if user_query:
    if user_query.strip() == "":
        st.error("Please enter a query.")
    else:
        try:
            # Send POST request to FastAPI
            response = requests.post(
                FASTAPI_URL,
                json={"query": user_query},
                headers={"Content-Type": "application/json"}
            )
            
            # Parse Response
            if response.status_code == 200:
                data = response.json()
                # st.write(data)
                text = data['Response'][0]
                video_url = data['Response'][1]

                if video_url and text:
                    st.write(text)
                    
                    # Embed YouTube Video
                    video_id = video_url.split("v=")[-1]
                    st.video(video_url)
                else:
                    st.error("No video found.")
            else:
                st.error(f"Failed to fetch video. Status Code: {response.status_code}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
