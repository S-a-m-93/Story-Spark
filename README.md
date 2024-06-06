# Story Spark✨

Welcome to **Story Spark✨**, a Streamlit application designed to help writers generate creative story ideas using the Llama-2-7B-Chat-GGML model. This application prompts the user for a central theme, character, setting, and genre, and then uses these inputs to generate interesting story ideas.

## Features

- Input fields for central theme/concept, character/archetype, and setting
- Dropdown selection for genre with several popular options
- Integration with the Llama 2 model to generate story ideas based on user inputs

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/story-idea-spark.git
    cd story-idea-spark
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Download the [Llama-2-7B-Chat-GGML model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML) and save it in the Story-Spark directory.
4. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Open your web browser** and navigate to `http://localhost:8501`.

3. **Interact with the app**:
    - Enter a central theme or concept for your story.
    - Describe a character or archetype.
    - Specify the story's world or location.
    - Choose a genre from the dropdown menu.
    - Click the "Generate Ideas" button to receive two interesting story ideas.


## Acknowledgements

- **Streamlit** for providing an easy-to-use framework for building interactive web applications in Python.
- **LangChain** and **CTransformers** for enabling seamless integration with advanced language models.
- **TheBloke** for providing the [Llama-2-7B-Chat-GGML model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML) on Hugging Face.

---

Happy writing! May your creativity be sparked with endless ideas. ✨
