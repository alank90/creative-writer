import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# ================================================ #
#   Function to get response from LLAMA 2 Model
# ================================================ #


def get_llama_responses(input_text, no_words, category):
    # pylint: disable-next=not-callable
    llm = CTransformers(model=r'models\pytorch_model.bin',
                        model_type='llama',
                        config={'max_new_tokens': 8000,
                                'temperature': 0.5,
                                'stream': True})

    # PromptTemplate
    template = """Write a  {category} on {input_text} in less than {no_words} words"""

    prompt = PromptTemplate(input_variables=["input_text", "no_words", "category"],
                            template=template)

    # Generate the response from the LLama 2 Model
    response = llm(prompt.format(category=category,
                                 input_text=input_text, no_words=no_words))
    print(response)
    return response
# ============ End get_llama_responses function ======================== #


# ============================================================ #
# ================ Streamlit Application ===================== #
# ============================================================ #
st.set_page_config(page_title="Generate content",
                   layout='centered',
                   initial_sidebar_state="collapsed")

st.header("Creative Writer✍️")

input_text_global = st.text_input("Enter the topic you want to write about")

col1, col2 = st.columns([5, 5])

with col1:
    no_words_global = st.text_input('Number of words')
with col2:
    category_global = st.selectbox("Category",
                                   ('Essays', 'Poem', 'Joke', 'Blog'),
                                   index=0)

submit = st.button("Generate")

if submit:
    st.write(get_llama_responses(input_text_global,
             no_words_global, category_global))
# ================ End Streamlit Application ===================== #
