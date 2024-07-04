# Jarvis - A Voice-Controlled Virtual Assistant

Jarvis is a Python-based virtual assistant that utilizes speech recognition, text-to-speech, and various APIs to perform a variety of tasks. This project demonstrates how to integrate different libraries and services to create a functional virtual assistant similar to Alexa, Siri, or Google Assistant.

## Features

- Voice recognition and response
- Opens popular websites like Google, Facebook, YouTube, LinkedIn, and GitHub
- Plays songs from a predefined music library
- Retrieves and reads out the latest news headlines
- General conversation capabilities using OpenAI's GPT-3.5 Turbo model

## Requirements

- Python 3.7+
- `speech_recognition` library
- `pyaudio` library
- `pyttsx3` library
- `webbrowser` module
- `requests` library
- OpenAI Python client library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/jarvis-virtual-assistant.git
    cd jarvis-virtual-assistant
    ```

2. Install the required Python packages:

    ```sh
    pip install speechrecognition pyaudio pyttsx3 requests openai
    ```

3. Ensure you have the `pyaudio` package installed. On Windows, you can download it from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it using `pip install <path_to_pyaudio_wheel>`.

4. Create a file named `musicLibrary.py` in the project directory with your predefined music links:

    ```python
    music = {
        "muskan": "https://www.youtube.com/watch?v=hB6ddOW2bY",
        "7years": "https://www.youtube.com/watch?v=LHCob76kigA",
        "see you again": "https://www.youtube.com/watch?v=RgKAFK5djSk",
        "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g"
    }
    ```

## Usage

1. **Obtain API Keys**:
    - **OpenAI API Key**: Sign up at [OpenAI](https://openai.com/) to obtain your API key.
    - **NewsAPI Key**: Sign up at [NewsAPI](https://newsapi.org/) to obtain your API key.

2. **Configure API Keys**:
    - Replace `"your_openai_api_key_here"` with your actual OpenAI API key.
    - Replace `"your_newsapi_key_here"` with your actual NewsAPI key.

3. **Run the script**:

    ```sh
    python jarvis.py
    ```

4. **Interaction**:
    - Activate Jarvis by saying "Jarvis".
    - Issue commands like "open Google", "open Facebook", "play [song name]", "news", or general questions.

## Example Commands

- "Jarvis, open Google."
- "Jarvis, play muskan."
- "Jarvis, what's the latest news?"

## Notes

- Ensure you have a working microphone.
- You need an active internet connection to use OpenAI and NewsAPI services.
- The assistant can only recognize commands accurately if spoken clearly within the set timeout and phrase time limit.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [OpenAI](https://openai.com/)
- [NewsAPI](https://newsapi.org/)

---

Feel free to fork this repository and contribute to it. For any queries or issues, please open an issue on GitHub.

