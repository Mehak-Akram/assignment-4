import streamlit as st
import string
from graph import Graph, Vertex

def extract_word(text):
    try:
        text = text.decode('utf-8')
    except UnicodeDecodeError:
        st.error("Unable to decode the text. Please ensure the file is in UTF-8 format. 📄🚫")
        return []
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words if words else []

def build_graph(words):
    if not words:
        st.error("No words found in the text.")
        return None

    graph = Graph()
    prev_vertex = None

    for word in words:
        word_vertex = graph.get_vertex(word)
        if prev_vertex:
            graph.add_edge(prev_vertex, word_vertex)
        prev_vertex = word_vertex

    graph.generate_probability_mapping()
    return graph

def generate_sequential_text(words, start_word):
    if start_word not in words:
        st.error(f"Starting word '{start_word}' is not found in the text. 🔍")
        return ""
    start_index = words.index(start_word)
    return ' '.join(words[start_index:])

# Streamlit UI
st.set_page_config(page_title="Markov Chain Text Generator 🧠🔀", page_icon="🧠", layout="wide")

st.title("🧠 Markov Chain Text Generator")

st.markdown("""
    <style>
        .css-ffhzg2 {
            font-size: 2rem;
            font-weight: 600;
            color: #1E90FF;
        }
        .css-18e3th9 {
            font-size: 1.25rem;
            color: #FF6347;
        }
        .stButton>button {
            background-color: #008CBA;
            color: white;
            font-size: 1.1rem;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #005f73;
        }
        .footer {
            bottom: 0;
            width: 100%;
            padding: 5px;
            margin-top: 20px;
            text-align: center;
            background-color: pink;
            font-size: 1rem;
            color: #333;
            border-top: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.header("📂 Upload Text Files")
uploaded_files = st.sidebar.file_uploader("Upload text file(s) 📂", type=["txt"], accept_multiple_files=True)

all_words = []

for file in uploaded_files or []:
    all_words.extend(extract_word(file.read()))

if all_words:
    st.success(f"Processed {len(uploaded_files)} file(s)! 🎉")
    graph = build_graph(all_words)

    st.subheader("💬 Generate Text")

    start_word = st.text_input("Enter a starting word:", value=all_words[0] if all_words else "")
    st.info(f"Generated text will continue from the first occurrence of **'{start_word}'** to the end of the file.")

    if st.button("Generate Text ✨"):
        generated_text = generate_sequential_text(all_words, start_word)
        st.markdown("### Generated Text ✍️")
        st.markdown(f"<div style='padding: 10px; background-color: black; border-radius: 10px; color: white;'>{generated_text}</div>", unsafe_allow_html=True)

else:
    st.info("Upload at least one text file to generate text. 📥")

st.markdown("""
    <div class="footer">
        <p>Built with ❤️ using Streamlit | © 2025 Mehak Akram</p>
    </div>
""", unsafe_allow_html=True)
