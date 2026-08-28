from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from google import genai

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")
        
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"Act like a helpful personal assistant. {question}"
    )    
    answer = response.text.strip()
    return jsonify({"response": answer}), 200

@app.route("/summarize", methods=["POST"])
def summarize():
    email_text = request.form.get("email")
    prompt = f"summarize the following email in 2-3 sentences: {email_text}"
        
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
        
    summary = response.text.strip()
    return jsonify({"response": summary}), 200

if __name__ == "__main__":
    app.run(debug=True)

