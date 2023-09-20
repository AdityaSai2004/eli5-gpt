import os
import base64
import openai
import plantuml
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# if not os.getenv("OPENAI_API_KEY"):
#     # Prompt the user for their OpenAI API key if it is not set in the environment variables
#     api_key = input("Please enter your OpenAI API key: ")
#     with open(".env", "a") as f:
#         f.write(f"OPENAI_API_KEY={api_key}\n")



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        openai_api_key = request.form["openai_api_key"]
        openai.api_key = openai_api_key


        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
            max_tokens=2048,
            top_p=1,
        )
        result = response.choices[0].text
        return render_template("index.html", result=result)

    result = request.args.get("result")
    print(result)
    return render_template("index.html", result=result)

def generate_prompt(animal):
    return "Give me a detailed eli5 explanation for the topic " + animal

if __name__ == "__main__":
    app.run(debug=True, port=5000)