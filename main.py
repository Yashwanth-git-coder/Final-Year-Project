# import google.generativeai as genai
# from PIL import Image
# import env
#
# # Configure the model
# genai.configure(api_key=env.key)
# model = genai.GenerativeModel(model_name='models/gemini-pro')
# image_model = genai.GenerativeModel(model_name='models/gemini-pro-vision')
#
# # Generate single content from the AI
# """
# response = model.generate_content('how many objects are in the solar system?')
# print(response.text)
# """
#
# # Have a conversation with the AI
#
# chat = model.start_chat()
# while True:
#     prompt = input('>>> ')
#     response = chat.send_message(prompt.strip())
#     print('Gemini:\n', response.text)
#
#
# # Using images
# """
# result = image_model.generate_content(
#     ['What do you think about this image?', Image.open('path to the image')]
# )
# print(result.text)
# """



from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import env

app = Flask(__name__)

# Configure the AI model
genai.configure(api_key=env.key)
model = genai.GenerativeModel(model_name='models/gemini-pro')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Serve the HTML page

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'response': 'Please provide a message.'}), 400

    # Generate a response from the AI
    chat = model.start_chat()
    response = chat.send_message(user_message.strip())
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)

