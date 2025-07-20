# Video to Text Converter

A Streamlit web application that converts video files to text transcriptions using OpenAI's Whisper speech recognition model.

## Features

- **Multi-format Support**: Supports various video formats including MP4, AVI, MOV, and MKV
- **Multi-language Transcription**: Supports 9 languages including English, Portuguese, Spanish, French, German, Russian, Chinese, Japanese, and Italian
- **Audio Extraction**: Automatically extracts audio from uploaded video files using FFmpeg
- **Real-time Processing**: Shows progress with a spinner during transcription
- **Download Option**: Allows users to download the transcription as a text file
- **Clean Interface**: Simple and intuitive Streamlit web interface

## Prerequisites

Before running the application, ensure you have the following installed:

### System Requirements
- Python 3.7 or higher
- FFmpeg (for audio extraction)

### Python Dependencies
```bash
pip install streamlit
pip install openai-whisper
```

### Installing FFmpeg

**Windows:**
- Download from [FFmpeg official website](https://ffmpeg.org/download.html)
- Add FFmpeg to your system PATH

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

## Installation

1. Clone or download the application code
2. Install the required Python packages:
```bash
pip install streamlit openai-whisper
```
3. Ensure FFmpeg is installed and accessible from the command line

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

3. Upload a video file using the file uploader

4. Select the language of the audio in the video

5. Wait for the transcription to complete

6. View the transcription results and optionally download them as a text file

## Supported Languages

- English
- Portuguese
- Spanish
- French
- German
- Russian
- Chinese
- Japanese
- Italian

## Supported Video Formats

- MP4
- AVI
- MOV
- MKV

## How It Works

1. **File Upload**: Users upload a video file through the Streamlit interface
2. **Audio Extraction**: The application uses FFmpeg to extract audio from the video file in WAV format (mono, 16kHz, 16-bit PCM)
3. **Transcription**: OpenAI's Whisper model processes the audio and generates text transcription
4. **Results**: The transcription is displayed on the web interface and can be downloaded
5. **Cleanup**: Temporary files are automatically deleted after processing

## Technical Details

- **Model Size**: Uses Whisper's "small" model for balanced performance and accuracy
- **Audio Format**: Converts to mono WAV at 16kHz sample rate
- **Temporary Files**: Uses Python's tempfile module for secure temporary file handling
- **Error Handling**: Includes basic error handling for file operations

## Limitations

- Processing time depends on video length and system performance
- Transcription accuracy depends on audio quality and speaker clarity
- Large video files may take significant time to process
- Requires stable internet connection for initial Whisper model download

## Troubleshooting

**FFmpeg not found error:**
- Ensure FFmpeg is properly installed and added to your system PATH

**Memory issues with large files:**
- Try using smaller video files or consider upgrading system RAM

**Slow transcription:**
- The "small" Whisper model is used by default for balance between speed and accuracy
- For faster processing, you could modify the code to use the "tiny" model
- For better accuracy with longer processing time, consider using "base" or "medium" models

## License

This project uses OpenAI's Whisper model which is released under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.
