import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


# Function to get response from LLAma 2 model
def get_idea_response(concept, character, setting, genre):
    """
    Gets story ideas from LLAma 2 model based on user input.

    Args:
        concept: String describing a central theme or idea.
        character: String describing a character or archetype.
        setting: String describing the story's world or location.
        genre: String representing the genre of the story.

    Returns:
        String containing a list of generated story ideas.
    """
    try:
        # LLama 2 model
        llm = CTransformers(
            model="llama-2-7b-chat.ggmlv3.q8_0.bin",
            model_type="llama",
            config={"max_new_tokens": 256, "temperature": 0.7},
        )

        # Prompt Template
        template = """
      Generate 2 interesting story ideas that combine the following elements in less than 200 words:
        * Concept: {concept}
        * Character: {character}
        * Setting: {setting}
        * Genre: {genre}
  """

        prompt = PromptTemplate(
            input_variables=["concept", "character", "setting", "genre"],
            template=template,
        )

        # Generates response from LLama 2 model
        response = llm(
            prompt.format(
                concept=concept, character=character, setting=setting, genre=genre
            )
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        st.error("An error occurred while generating ideas. Please try again later.")
        return None


st.set_page_config(
    page_title="Story Idea Spark",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header("Story Spark ✨")

st.write(
    "Struggling to find the next twist in your story? Use Story Spark to ignite your imagination!"
)

# Input fields for concept, character, and setting
concept = st.text_input("Central Theme/Concept:")
character = st.text_input("Character or Archetype:")
setting = st.text_input("Story World/Location:")

# Genre selection with options
genre_options = (
    "Science Fiction",
    "Fantasy",
    "Mystery",
    "Romance",
    "Thriller",
    "Horror",
    "Dystopian",
    "Historical Fiction",
)
genre = st.selectbox("Genre:", genre_options, index=0)

submit = st.button("Generate Ideas")

# Final response
if submit:
    response = get_idea_response(concept, character, setting, genre)
    st.write("Here are some ideas to get you started:")
    st.write(response)
