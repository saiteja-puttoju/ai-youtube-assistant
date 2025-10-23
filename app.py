import streamlit as st
from supporting_functions import extract_video_id, get_transcripts, translate_text, get_important_topics, generate_notes


with st.sidebar:
    st.title("🎬 VidNote AI")

    st.markdown('---')
    youtube_url  = st.text_input("Insert YouTube URL: ", placeholder="https://www.youtube.com/watch?v=pBRSZBtirAk")
    language = st.text_input("Video Language: ", placeholder="e.g., en, hi, te", value='en')
    st.markdown('---')

    page = st.radio("Select the page: ", ['Notes Generator', 'Chat with Video (v2)'])



st.set_page_config(
    page_title = "YouTube AI Assistant",
    layout = "wide",
    page_icon = "▶️",
    menu_items={
    'Get Help': 'https://www.linkedin.com/in/saiteja-puttoju/',
    'About': """
    \nLinkedIn Profile: https://www.linkedin.com/in/saiteja-puttoju/
    \nGitHub Profile: https://github.com/saiteja-puttoju
    \nHashnode Profile: https://hashnode.com/@saiteja-puttoju
    """
    }
)

if page == 'Notes Generator':
    st.title("🗒 Instant Video Note Generator")
    st.write("> Generate concise notes from any YouTube video using AI.")
    submit_button = st.button("Submit", type='primary')

    if submit_button:

        if not youtube_url:
            st.warning("⚠ Please insert youtube url in sidebar!")
        elif not language:
            st.warning("⚠ Please select the language in sidebar!")
        else:
            video_id = extract_video_id(youtube_url)

            if video_id:
                with st.spinner("Step 1/3 : Fetching Video Transcripts..."):
                    full_transcript = get_transcripts(video_id, language)

                if language != 'en':
                    with st.spinner("Step 1.5/3 : Translating transcripts into English..."):
                        full_transcript = translate_text(full_transcript)

                if full_transcript:

                    with st.spinner("Step 2/3 : Fetching key topics..."):
                        topics = get_important_topics(full_transcript)
                        st.header("Key Topics: ")
                        st.info(topics)

                    with st.spinner("Step 3/3 : Generating Notes..."):
                        notes = generate_notes(full_transcript)
                        st.header("Notes: ")
                        st.write(notes)
                    
                    st.success("✅ Generated notes successfully!")
                
                else:
                    st.info("Error in fetching transcripts, please try again!")

        
elif page == "Chat with Video (v2)":
    st.title("🗪 Chat with Video (Coming Soon!)")
    
    st.info("This feature is currently under development. Stay tuned!")
    
    st.write("In the meantime, feel free to use the **'Make Notes'** feature to get key topics and notes from any video.")