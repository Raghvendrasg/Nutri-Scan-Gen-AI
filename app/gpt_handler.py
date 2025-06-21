import os
from openai import OpenAI
from image_utils import encode_image_to_base64

client = None

def get_client():
    global client
    if client is None:
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found. Please set it in your .env file")

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )
    return client

def analyze_image(image_file, prompt: str) -> str:
    try:
        client = get_client()
        image_bytes = image_file.getvalue()
        encoded_image = encode_image_to_base64(image_bytes)

        response = client.chat.completions.create(
            # model="openai/gpt-4o-2024-11-20",
            # model="google/gemini-2.5-flash",
            model="meta-llama/llama-3.2-90b-vision-instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}",
                                "detail": "high"
                            }
                        }
                    ]
                }
            ],
            max_tokens=800,
            extra_headers={
                "HTTP-Referer": "https://your-app-name.com",  # Optional
                "X-Title": "HealthScan AI",  # Optional
            },
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error analyzing image: {e}"
