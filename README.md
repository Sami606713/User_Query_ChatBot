# Customer Support ChatBot

## Overview
The **Customer Support ChatBot** aims to serve users by efficiently responding to their queries. In addition to addressing textual queries, the bot also provides **YouTube video recommendations** for enhanced assistance.

---

## Features
- **Query Handling**: Responds to user queries with accurate and concise answers.
- **Video Recommendations**: Suggests relevant YouTube videos based on user queries.
- **Web Search Integration**: Fetches additional information from the web if required.

---

## Folder Structure

### Backend
The backend is built using **FastAPI** for handling API requests. The following components are included:
- **`web-search/`**: Handles web search functionality exclusively.
- **`youtube/`**: Handles YouTube search and video recommendations.
- **`utils.py`**: Contains utility functions for shared tasks.
- **`main.py`**: Entry point for running the FastAPI backend.
- **`Dockerfile`**: Facilitates containerization of the backend for deployment.
- **`requirements.txt`**: Lists all the dependencies required for the backend.

### Frontend
The frontend provides a user interface for interacting with the chatbot. It contains:
- **`styles/`**: Includes `styles.css` files for UI styling.
- **`scripts/`**: Contains JavaScript files for dynamic functionalities.
- **`images/`**: Stores images used in the application.
- **`bot.html`**: The main HTML file for rendering the chatbot interface.

---

## Technologies Used
- **Backend**: Langchain, GroqLLM,FastAPI, Python
    - **Langchain Tool** Youutube Search Tool, Tavily SearchTool
- **Frontend**: HTML, CSS, JavaScript
- **Other Tools**:
  - Docker (for containerization)
  - Web scraping and API integration for search functionalities

---