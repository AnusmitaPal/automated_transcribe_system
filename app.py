import os
import streamlit as st
import whisper
import tempfile
import subprocess
import time


def extract_audio(input_video_path, output_audio_output):
    """Extract audio from the video file."""
    command = ["ffmpeg", "-y", "-i", input_video_path, "-ac", "1", "-ar", "16000", "-acodec", "pcm_s16le",
               output_audio_output]
    subprocess.call(command)
    return True

class AudioTranscriber:
    def __init__(self):
        self.model = None

    def init(self, model_size="small"):
        """Initializes the transcriber with a specific model size."""
        self.model = whisper.load_model(model_size)

    def transcribe_audio(self, audio_path, language="Portuguese"):
        """Transcribes the audio file and returns the transcription text."""
        result = self.model.transcribe(audio_path, language=language)
        return result["text"]


st.title("Video to Text Converter")

uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov", "mkv"])
language_selection = st.selectbox("Select Language",
                                  ["English", "Portuguese", "Spanish", "French", "German", "Russian", "Chinese",
                                   "Japanese", "Italian"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(uploaded_file.getbuffer())
        temp_video_path = temp_video.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        audio_path_output = temp_audio.name

    extract_audio(temp_video_path, audio_path_output)
    transcriber = AudioTranscriber()
    transcriber.init(model_size="small")
    with st.spinner("Transcribing..."):
        transcription_text_output = transcriber.transcribe_audio(audio_path_output, language=language_selection)

    st.write("Transcription:")
    st.write(transcription_text_output)

    # Download button
    st.download_button(
        label="Download Transcription",
        data=transcription_text_output.encode("utf-8"),
        file_name="transcription.txt",
        mime="text/plain",
    )
    time.sleep(1)  # Small delay to ensure the file is no longer in use
    os.unlink(temp_video_path)
    os.unlink(audio_path_output)