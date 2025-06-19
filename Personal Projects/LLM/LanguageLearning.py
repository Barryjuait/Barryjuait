import os
from dotenv import load_dotenv
import requests
from datetime import datetime


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

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the .env file!")

# --- Groq API Request ---
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {groq_api_key}",
    "Content-Type": "application/json"
}

# Define models to try (fallback if one is deprecated)
MODELS_TO_TRY = [
    "llama3-70b-8192",  # Best for most cases (newest as of 2024)
    "llama3-8b-8192",   # Smaller but faster
    "mixtral-8x7b-32768" # Legacy (may still work for some)
]

def get_ai_tip(prompt):
    """
    Sends a prompt to the Groq API and returns a tip.

    Args:
        prompt (str): The user-provided prompt for the AI.

    Returns:
        str: The generated tip or an error message.
    """
    for model in MODELS_TO_TRY:
        data = {
            "messages": [{"role": "user", "content": prompt}],
            "model": model
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            ai_response = response.json()
            tip = ai_response["choices"][0]["message"]["content"]
            print(f"\n=== Daily Personal Growth Tip ({datetime.now().strftime('%Y-%m-%d')}) ===")
            print(f"(Generated using {model})")
            return tip
        else:
            print(f"Model {model} failed: {response.status_code}, trying next...")

    # If all models fail
    return f"All models failed. Latest error: {response.text}"

# Example usage when running directly
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    result = get_ai_tip(user_prompt)
    print(result)