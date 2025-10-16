import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rewrite_message(text, tone="professional"):
    prompt = f"Rewrite this message in a {tone} tone: {text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant that rewrites messages politely."},
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content.strip()

# --- Run the app ---
if __name__ == "__main__":
    user_input = input("Enter your message: ")
    tone_choice = input("Choose tone (professional / friendly / concise): ").lower()

    result = rewrite_message(user_input, tone_choice)
    print("\nRewritten message:")
    print(result)
