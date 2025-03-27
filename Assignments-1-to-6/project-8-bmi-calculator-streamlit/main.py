import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 🟡"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight 🟢"
    elif 25 <= bmi < 29.9:
        return "Overweight 🟠"
    else:
        return "Obesity 🔴"

def suggest_ideal_weight(height):
    min_weight = 18.5 * (height ** 2)
    max_weight = 24.9 * (height ** 2)
    return min_weight, max_weight

def main():
    st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")
    
    theme = st.radio("Choose Theme", ["Light", "Dark"])
    
    dark_mode_style = """
        <style>
            body, .stApp { background-color: #1e1e1e !important; color: white !important; }
            .stTextInput, .stNumberInput, .stButton { color: black !important; }
        </style>
    """
    
    if theme == "Dark":
        st.markdown(dark_mode_style, unsafe_allow_html=True)
    
    st.title("💪 BMI Calculator")
    st.write("📊 Calculate your Body Mass Index (BMI)")
    
    weight = st.number_input("⚖️ Enter your weight (kg)", min_value=1.0, format="%.2f")
    height = st.number_input("📏 Enter your height (m)", min_value=0.5, format="%.2f")
    age = st.number_input("🎂 Enter your age", min_value=1, max_value=120, value=25)
    
    if st.button("🔍 Calculate BMI"):
        if weight and height:
            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)
            st.success(f"Your BMI is {bmi:.2f} ({category})")
            
            # Suggest ideal weight range
            min_weight, max_weight = suggest_ideal_weight(height)
            st.info(f"💡 Ideal weight range for your height: {min_weight:.2f} kg - {max_weight:.2f} kg")
        else:
            st.error("⚠️ Please enter valid weight and height values.")
    
    st.markdown("---")
    st.markdown("💡 Developed with ❤️ using Streamlit")

if __name__ == "__main__":
    main()
