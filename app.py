from flask import Flask, request, jsonify
import google.generativeai as genai
import json
from flask_cors import CORS


# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure GenerativeAI API
genai.configure(api_key='AIzaSyAnIm6lpzgoIdermHNHy0BFpzxe8ySJjK0')  # Replace 'YOUR_API_KEY' with your actual API key

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

safety_ratings = {
    'HARM_CATEGORY_SEXUALLY_EXPLICIT':'block_none',
    'HARM_CATEGORY_HATE_SPEECH': 'block_none',
    'HARM_CATEGORY_HARASSMENT': 'block_none',
    'HARM_CATEGORY_DANGEROUS_CONTENT' : 'block_none'
    }

# Initialize GenerativeModel
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


@app.route('/chat', methods=['GET','POST'])
def chat_endpoint():
    global safety_ratings,genai_prompt,warning_prompt
    
    # Get user input from request
    user_input = request.args.get("question")

    # Send user input to GenerativeModel
    response = chat.send_message(genai_prompt + '\n' + user_input  + warning_prompt,safety_settings=safety_ratings)
    
    response = response.text
    
    # Return assistant response
    return jsonify({"response": response})

@app.route("/health" , methods=['GET'])
def health():
    if request.method == "GET":
        return json.dumps({'status': 'healthy'})
    else:
        return json.dumps({'status': 'unhealthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
