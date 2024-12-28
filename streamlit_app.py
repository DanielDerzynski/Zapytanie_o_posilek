import streamlit as st
import openai

def get_gpt_response(prompt, api_key):
    """Funkcja do komunikacji z ChatGPT"""
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides recipes."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    """Główna logika aplikacji"""
    # Ustawienia Streamlit
    st.set_page_config(page_title="Food Recommendation App", layout="centered")

    # Stylizacja tła
    st.markdown(
        """
        <style>
        body {
            background-color: #E6F7FF;
            color: #004D73;
            font-family: Arial, sans-serif;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 24px;
            border: none;
            border-radius: 4px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Nagłówek aplikacji
    st.title("Food Recommendation App")
    st.subheader("Podaj swoje preferencje żywieniowe, a wymyślę dla Ciebie potrawę!")

    # Klucz API OpenAI
    api_key = "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"

    # Preferencje użytkownika
    preferences = st.text_input("Jakie masz preferencje żywieniowe? (np. wegetariańskie, kuchnia włoska, szybkie posiłki)")

    if st.button("Znajdź potrawę"):
        if not preferences:
            st.error("Proszę wprowadzić swoje preferencje!")
        else:
            with st.spinner("Proszę czekać, generuję odpowiedź..."):
                prompt = (
                    f"Based on the following dietary preferences: {preferences}, suggest a dish and provide a list of ingredients to prepare it."
                )
                response = get_gpt_response(prompt, api_key)
                st.success("Oto wynik:")
                st.text(response)

if __name__ == "__main__":
    main()
