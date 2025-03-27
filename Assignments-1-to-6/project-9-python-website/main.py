import streamlit as st
import requests

def get_random_joke(category="random"):
    """Fetch a random joke from the API based on category."""
    url = "https://official-joke-api.appspot.com/jokes/"
    if category == "programming":
        url += "programming/random"
    elif category == "general":
        url += "general/random"
    else:
        url += "random"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            if isinstance(joke_data, list):  
                joke_data = joke_data[0]
            return f"😂 {joke_data['setup']} \n\n 🤣 {joke_data['punchline']}"
        else:
            return "⚠️ Failed to fetch a joke. Please try again later."
    except:
        return "🤖 Why did the programmer quit his job? \n Because he didn't get array."

def main():
    st.set_page_config(page_title="Joke Generator", layout="centered")
    
    st.title("🤣 Random Joke Generator")
    st.write("Click the button below to generate a joke!")
    
    category = st.selectbox("Choose a joke category:", ["random", "general", "programming"], index=0)
    
    num_jokes = st.slider("Number of jokes:", 1, 5, 1)
    
    if st.button("😂 Generate Joke"):
        jokes = [get_random_joke(category) for _ in range(num_jokes)]
        for joke in jokes:
            st.markdown(f"""
            <div style='background-color: rgba(0, 0, 139, 0.5); color: white; padding: 10px; border-radius: 10px;'>
                    {joke}
                </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div style='text-align:center;'>
        <p>🎤 Jokes from Official Joke API 🎭</p>
        <p>Made with ❤️ using Streamlit | © 2025 Mehak Akram 🚀</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
