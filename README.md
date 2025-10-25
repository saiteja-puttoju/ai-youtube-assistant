# 🎬 VidNote AI: AI YouTube Summarizer

VidNote AI is an intelligent web application built with Streamlit that generates concise, structured notes and extracts key topics from any YouTube video. It uses the YouTube Transcript API to fetch transcripts and Google's Gemini AI via LangChain to process the text.

-----

## 🌟 Key Features

  * **Automatic Transcript Detection:** Automatically finds the best available transcript for a video. The app prioritizes manual 'en', then other manual languages, then generated 'en', ensuring the highest quality source.
  * **Automatic Translation:** Intelligently checks the language code of the fetched transcript. If it's not English, it automatically translates the text before processing.
  * **Key Topic Extraction:** Analyzes the full transcript to identify and list the five most important topics or concepts discussed in the video.
  * **Structured Note Generation:** Employs a sophisticated LangChain prompt to generate detailed, well-structured notes, complete with emoji-led subheadings and bullet points for easy reading.
  * **Robust URL Parsing:** Includes a function to extract the video ID from various YouTube URL formats (standard, short, embed, etc.).
  * **Two-Page Interface:** A clean Streamlit app with a "Notes Generator" page and a "Chat with Video (v2)" placeholder that is "Coming Soon\!".

-----

## 🛠️ Technologies Used

  * **Backend:** Python 3.12
  * **AI Model:** Google Gemini (`gemini-2.5-flash-lite`)
  * **AI Framework:** LangChain (`langchain`, `langchain-core`, `langchain-google-genai`)
  * **Web Framework:** Streamlit
  * **API/Services:** YouTube Transcript API
  * **Dependencies:**
      * `python-dotenv`

-----

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

  * Python 3.12 or later
  * A Google API Key with the Gemini API enabled. You can get one from [Google AI Studio](https://makersuite.google.com/).

### Installation and Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/saiteja-puttoju/ai-youtube-summarizer.git
    cd ai-youtube-summarizer
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    # For Linux/macOS
    python -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**

      * Create a new file in the root of the project named `.env`.
      * Add your Google API key to this file (this is read by `supporting_functions.py`):
        ```
        GOOGLE_API_KEY="YOUR_API_KEY_HERE"
        ```

### Running the Application

Once the setup is complete, you can run the Streamlit application with the following command:

```bash
streamlit run app.py
```

Your web browser will automatically open to the application's user interface.

-----

## How to Use

1.  Open the application in your browser.
2.  On the sidebar, paste the full **YouTube URL** into the text input.
3.  Ensure the **"Notes Generator"** page is selected in the sidebar.
4.  Click the **"Submit"** button.
5.  The application will automatically find the best transcript, translate it if necessary, and display the **Key Topics** and **Notes**.