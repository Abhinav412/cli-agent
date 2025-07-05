import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

def main():
    if len(sys.argv) < 2:
        print("Not enough arguments")
        sys.exit(1)
    prompt = sys.argv[1]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    messages = [types.Content(role="user",parts=[types.Part(text=prompt)]),]
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model = "gemini-2.0-flash-001", 
    contents= messages)
    
    print(response.text)

    if sys.argv[2] == "--verbose":
        print("User prompt:",prompt)
        print("Prompt tokens:",response.usage_metadata.prompt_token_count)
        print("Response tokens:",response.usage_metadata.candidates_token_count)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
