# Enhance Q&A Chatbot with Ollama
This repository demonstrates how to run an open-source model locally using [Ollama](https://github.com/ollama/ollama) and integrate it into a Streamlit app. Users can select a model, adjust temperature/max tokens, and ask questions just like an OpenAI chatbot—except everything runs locally with an open-source model!

## Features
 - Local Inference with Ollama: No external API calls; you run the model on your own machine.
 - Model Selection: Choose from available local models (e.g., deepeek-1).
 - Adjustable Parameters: Tune temperature and token limits via a user-friendly UI.
 - Simple Q&A: Type your question in a text box and see the chatbot’s answer immediately.# Enhance-Q-A-Chatbot-with-Ollama

## **Below is a demonstration of the app's interface:**
![image](https://github.com/user-attachments/assets/c39aaf92-2713-4311-b827-f2718e9f0eb2)


## Requirements
1. Ollama Installed
  - Install [Ollama](https://github.com/ollama/ollama) on your machine.
  - Pull the model you want to use. For example
    ``` bash
      ollama pull deepeek-1
    ```
    Make sure the model name in your code (deepeek-1) matches what you have pulled.

2. Python 3.7+

  - Verify that you have a recent version of Python installed.

## Getting Started

1. Clone this repository
   ``` bash
    git clone https://github.com/aljebraschool/Enhance-QA-chatbot-with-OpenAI.git
    cd Enhance-QA-chatbot-with-OpenAI

   ```
2. Create and activate a virtual environment (optional but recommended)
   ``` bash
    # On macOS/Linux
    python3 -m venv env
    source env/bin/activate
    
    # On Windows
    python -m venv env
    env\Scripts\activate

   ```

3. Install dependencies
   ``` bash
   pip install -r requirements.txt

   ```

## Usage
 1. Start the Application
  run:
``` bash
streamlit run app.py

```
The script will connect to your local Ollama installation and load the locally installed model.

2. Select your model:

  - In the web interface, pick the open-source model you want to use (e.g., deepeek-1).
  - Adjust the temperature and max tokens if desired.
  
3. Ask a question:
  
  - Type your prompt into the text box (e.g., “What is a computer?”).
  - Press Enter or click the button to get a response from your locally running model.

## Troubleshooting
  - Model Not Found: Make sure you ran ollama pull <model-name> for the same name that appears in your code or the Streamlit dropdown.
  - Performance Issues: Large models can be slow or consume a lot of memory. Consider using a smaller model if you encounter resource constraints.
  - Environment Conflicts: Use a separate virtual environment to avoid Python package conflicts.

