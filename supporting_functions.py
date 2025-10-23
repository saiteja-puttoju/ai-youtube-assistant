import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, InvalidVideoId, TranscriptsDisabled, RequestBlocked, IpBlocked
import time
import re

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# initialize the gemini model
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
    temperature = 0.2
)


# function to extract video id from youtube url
def extract_video_id(url):
    """
    Extracts the Video ID from given youtube video url
    """

    match = re.search(r"(?:v=|vi=|youtu\.be/|embed/|shorts/|v/)([a-zA-Z0-9_-]{11})", url)

    if match:
        return match.group(1)
    else:
        st.error("Error with youtube Video ID extraction, please check the url once again")
        return None


# function to get transcripts from YouTube video
def get_transcripts(video_id, language):
    """
    Fetches youtube video transcriptions using video url and language code.
    """

    ytt_api = YouTubeTranscriptApi()

    try:
        fetched_transcript = ytt_api.fetch(video_id=video_id, languages=[language])
        transcript = " ".join([i.text for i in fetched_transcript])

        time.sleep(10)
        return transcript


    except InvalidVideoId:
        st.error("Invalid YouTube Video ID, please check the url once again")
    except TranscriptsDisabled:
        st.error("Transcripts are disabled for this video")
    except RequestBlocked:
        st.error("Request blocked by YouTube, please try again later")
    except IpBlocked:
        st.error("IP Blocked by YouTube, please try again later")
    except Exception as e:
        st.error(f"Error with fetching transcription: {e}")


# function to translate text to English
def translate_text(transcript):
    """
    Translates the given text to the English language.
    """

    try:
        prompt = PromptTemplate.from_template("""
        You are a professional translator.  
        Your task is to translate the following text into English, **preserving all meaning, intent, nuance, tone and style** of the original — without changing or omitting anything.  
        Do **not** add commentary, explanations or interpretations; provide **only** the translation.

        Text to translate:
        '''
        {transcript}
        '''

        Your output should be exactly the translated text in English, and nothing else.
        """)

        chain = prompt | llm

        response = chain.invoke({'transcript': transcript})

        return response.content

    except Exception as e:
        st.error(f"Error with translating: {e}")


# function to get important topics from the transcript
def get_important_topics(transcript):
    """
    Identifies the five most important topics or concepts discussed in the transcript.
    """

    try:
        prompt = PromptTemplate.from_template("""
        You are an expert summarization assistant tasked with analyzing the following video transcript.

        Your assignment:

        - Identify the five most important topics or concepts discussed in the transcript.

        - Each topic should reflect a major theme or idea, not minor details, quotes, or side‐points.

        - Provide the result as a numbered list (1 through 5).

        - Use clear, concise wording focused on the technical content of the video.

        - Do not phrase items as questions or opinions; state them as factual key topics.

        - Only include topics that are actually discussed in the transcript — do not add or infer unrelated ones.

        Transcript:
        '''
        {transcript}
        '''
        """)

        chain = prompt | llm

        response = chain.invoke({"transcript": transcript})

        return response.content

    except Exception as e:
        st.error(f"Error with translating: {e}")


# function to generate notes from the transcript
def generate_notes(transcript):
    """
    Generates concise notes from the transcript, capturing all key points and important information.
    """

    try:
        prompt = PromptTemplate.from_template("""
        You are an expert AI note-taking assistant. Your task is to analyze the following YouTube video transcript and produce clear, well-structured, and concise notes.  

        ⚡ Requirements:  
        - Present the output as **bulleted points**, grouped into logical **sections** with **subheadings**.  
        - Each subheading must begin with a single relevant **emoji**, but **must not include emojis at the end**.  
        ✅ Example: 📌 Childhood Reading Habits  
        ❌ Not allowed: 📌 Childhood Reading Habits 📚  
        - Capture all **key points, important facts, and examples** without adding information not present in the transcript.  
        - Use **short, clear sentences** (avoid long paragraphs, filler, or repetition).  
        - Highlight critical insights with bold labels such as **Key takeaway:**, **Fact:**, or **Example:** where appropriate.  
        - Ensure the notes are easy to scan and suitable for quick review.  

        ✨ Suggested Subheading Styles (emoji at start only):  
        - 📌 Overview  
        - 💡 Key Ideas  
        - 📝 Examples / Case Studies  
        - 🎯 Takeaways  
        - ❓ Questions / Unclear Points  

        Transcript:  
        '''  
        {transcript}  
        '''      
        """)

        chain = prompt | llm

        response = chain.invoke({"transcript": transcript})

        return response.content

    except Exception as e:
        st.error(f"Error with generating notes: {e}")