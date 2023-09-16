import openai
import streamlit as st


def main():
    st.title("Acest site are scopul de a va ajuta cu verificarea temei.")
    
    # Get the word from the user (creates a box where the user can type sth)
    sentence = st.text_input("Scrieti o propozitie/fraza si asteptati putin pentru a o corecta in cazul unei greseli!")

    # Create a button
    if st.button("Verifica"):
       # Place the code you want to execute with the word here
       # reading the OpenAi key
       text_file_with_OpenAI_API_token = '/Users/andrei/Desktop/Python/open_api_token.txt'
       with open(text_file_with_OpenAI_API_token, 'r') as f:
          openai.api_key = f.read()
       question_file = '/Users/andrei/Desktop/Python/Experiments/question_api.txt'
       with open(question_file, 'r') as f:
           question = f.read()
       messages = [
         {"role": "system", "content": question},
         {"role": "user", "content": sentence}
         ]
       response = openai.ChatCompletion.create(
         model="gpt-4",
         messages=messages
         )
       assistant_reply = response['choices'][0]['message']['content']
       st.write("Aceasta este versiunea modificata a propozitiei!")
       st.write(assistant_reply)
       # Any other logic based on the word can be added here

if __name__ == "__main__":
    main()
