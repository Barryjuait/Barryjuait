from flask import Flask, render_template_string, request
import os
from dotenv import load_dotenv
import requests

# Explicitly specify the path to the .env file
homeFolder = "/Users/sbk/Documents/Datasets/LLM"
envFile = os.path.join(homeFolder, '.env')

if os.path.exists(envFile):
    print(f"Loading environment variables from {envFile}")
    load_dotenv(dotenv_path="/Users/sbk/Documents/Datasets/LLM/.env")
else:
    raise FileNotFoundError(f".env file not found at {envFile}")

# Access the API key
groq_api_key = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    tip = None
    error = None

    if request.method == "POST":
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            error = "API key missing in .env file!"
        else:
            try:
                response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "messages": [{
                            "role": "user",
                            "content": "Give me a concise, actionable tip for personal growth today."
                        }],
                        "model": "llama3-70b-8192"  # Use latest model
                    }
                )
                if response.status_code == 200:
                    tip = response.json()["choices"][0]["message"]["content"]
                else:
                    error = f"API Error: {response.text}"
            except Exception as e:
                error = f"Failed to connect: {str(e)}"

    # Simple HTML (customize later)
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Daily Growth Coach</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
                button { padding: 10px 15px; background: #4CAF50; color: white; border: none; cursor: pointer; }
                button:hover { background: #45a049; }
                .tip { margin-top: 20px; padding: 15px; background: #f9f9f9; border-left: 4px solid #4CAF50; }
                .error { color: red; }
            </style>
        </head>
        <body>
            <h1>Daily Growth Tip</h1>
            <form method="POST">
                <button type="submit">Get Today's Tip</button>
            </form>
            {% if tip %}
                <div class="tip">{{ tip }}</div>
            {% endif %}
            {% if error %}
                <div class="error">{{ error }}</div>
            {% endif %}
        </body>
        </html>
    ''', tip=tip, error=error)

if __name__ == "__main__":
    app.run(debug=True)  # Run on http://localhost:5000