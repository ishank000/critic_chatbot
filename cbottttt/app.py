from flask import Flask, request, render_template
import openai

app = Flask(__name__)

openai.api_key = "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"

messages = [{"role": "system", "content": "A sarcastic and savage funny replies giving genius"}]

def CustomChatGPT(What_you_wanna_know_about):
    messages.append({"role": "user", "content": What_you_wanna_know_about})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['input_text']
        output_text = CustomChatGPT(user_input)
        return render_template('result.html', output=output_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

