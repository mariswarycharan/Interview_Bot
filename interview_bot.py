import streamlit as st
import google.generativeai as genai
genai.configure(api_key='AIzaSyAnIm6lpzgoIdermHNHy0BFpzxe8ySJjK0')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

st.title("Yugam Bot")

content = '''

this is content i have prepare for roche interview:

I am very interested in working for an internship at Roche. and 
am eager to contribute my passion and skills to advance Roche's mission in healthcare and make a meaningful impact during the internship

To convey a complex product's strategy and benefits to customers, I would use visual storytelling, demonstrations, and real-world examples. Visual aids like infographics and comparison charts simplify information. Interactive workshops and webinars engage customers, fostering understanding and positive perception. This approach enhances customer decision-making and influences favorable behavior toward the product.

The audience's mindset is more important in a presentation. Adapting to their needs ensures effective communication, engagement, and achievement of presentation objectives. While your mindset and preparation matter, they should support and align with the audience's experience.


'''




genai_prompt = '''

You are a interview guider bot and your job is to guide me for interview processes to crack it

but also you want to ack like general chatbot

'''


warning_prompt = '''

Answer only to this question above i have mentioned

IN output : Do not include this 
do not generate code
do not answer to question none another than interview question 

'''


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    prompt = prompt
    
    safety_ratings = {
    'HARM_CATEGORY_SEXUALLY_EXPLICIT':'block_none',
    'HARM_CATEGORY_HATE_SPEECH': 'block_none',
    'HARM_CATEGORY_HARASSMENT': 'block_none',
    'HARM_CATEGORY_DANGEROUS_CONTENT' : 'block_none'
    }
    
    
    if len(st.session_state.messages) <= 1:
        st.success(genai_prompt + '\n' + content + "\n" + " now my Question is " + prompt  + warning_prompt)
        response = chat.send_message(genai_prompt + '\n' + content + "\n" + " now my Question is " + prompt  + warning_prompt ,stream=True,safety_settings=safety_ratings)
    else:
        response = chat.send_message(genai_prompt + '\n' + prompt  + warning_prompt,safety_settings=safety_ratings ,stream=True)
        
    
    store_data = ""
    with st.chat_message("assistant"):
        for chunk in response:
            result = chunk.text
            store_data += result 
            response = result
            # Display assistant response in chat message container
            
            st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": store_data})

