import streamlit as st
# Import our new, reliable function
from supporting_functions import extract_video_id, get_best_transcript, translate_text, get_important_topics, generate_notes
import re # Make sure re is imported

with st.sidebar:
    st.title("🎬 VidNote AI")

    st.markdown('---')
    youtube_url = st.text_input("Insert YouTube URL: ", placeholder="https://www.youtube.com/watch?v=pBRSZBtirAk")
    
    # --- Language input is REMOVED ---
    
    st.markdown('---')

    page = st.radio("Select the page: ", ['Notes Generator', 'Chat with Video (v2)'])



st.set_page_config(
    page_title = "YouTube AI Assistant",
    layout = "wide",
    page_icon = "▶️",
    menu_items={
    'Get Help': 'https://www.linkedin.com/in/saiteja-puttoju/',
    'About': "LinkedIn Profile: https://www.linkedin.com/in/saiteja-puttoju/"
    }
)

if page == 'Notes Generator':
    st.title("🗒 Instant Video Note Generator")
    st.write("> Generate concise notes from any YouTube video using AI.")
    submit_button = st.button("Submit", type='primary')

    if submit_button:

        if not youtube_url:
            st.warning("⚠ Please insert youtube url in sidebar!")
        else:
            video_id = extract_video_id(youtube_url)

            if video_id:
                full_transcript = None # Initialize variable
                lang_code = None     # Initialize variable
                
                with st.spinner("Step 1/3 : Fetching Video Transcripts..."):
                    # --- THIS IS THE NEW LOGIC ---
                    transcript_data, lang_code_or_error = get_best_transcript(video_id)
                    
                    if not transcript_data:
                        # If it failed, show the error and stop
                        st.error(f"Failed to get transcript: {lang_code_or_error}")
                    else:
                        # If it succeeded, set our variables
                        lang_code = lang_code_or_error
                        full_transcript = " ".join([line.text for line in transcript_data])
                
                # This 'if' check ensures the rest only runs on success
                if full_transcript:
                    
                    # We can now check the language code
                    if lang_code != 'en':
                        with st.spinner("Step 1.5/3 : Translating transcripts into English..."):
                            full_transcript = translate_text(full_transcript)
                    
                    # The rest of your code runs perfectly from here
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