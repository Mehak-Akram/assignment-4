import streamlit as st
import string
from graph import Graph

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

def generate_text(graph, start_word, length=20):
    if not graph:
        st.error("Graph is not available for text generation. 🛑")
        return ""
    
    if not start_word or start_word not in graph.vertices:
        st.error(f"Starting word '{start_word}' is not in the graph. Please choose a valid word. 🔍")
        return ""

    current_word = start_word
    result = [current_word]

    for _ in range(length - 1):
        current_vertex = graph.get_vertex(current_word)
        next_vertex = graph.get_next_word(current_vertex)
        if not next_vertex:
            break
        result.append(next_vertex.word) 
        current_word = next_vertex.word  
    if not result:
        st.error("No text could be generated. Please check the graph or starting word. 🛑")
        return ""
    
    return ' '.join(result)

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
        .stSlider>div>div>div>div {
            background-color: #FFD700;
        }
        .footer {
            bottom: 0;
            width: 100%;
            padding: 5px;
            margin-top: 20px;
            text-align: center;
            background-color: black;
            font-size: 1rem;
            color: white;
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

    start_word = st.text_input("Enter a starting word:", value=all_words[0])
    length = st.slider("Length of generated text (words):", 5, 100, 20)

    if st.button("Generate Text ✨"):
        generated_text = generate_text(graph, start_word, length)
        st.markdown(f"### Generated Text ✍️")
        st.markdown(f"<div style='padding: 10px; background-color: black; border-radius: 10px;'>{generated_text}</div>", unsafe_allow_html=True)

else:
    st.info("Upload at least one text file to generate text. 📥")

st.markdown("""
    <div class="footer">
Developed with 💙 by Mehak Akram | © 2025 🚀 </div>
""", unsafe_allow_html=True)
