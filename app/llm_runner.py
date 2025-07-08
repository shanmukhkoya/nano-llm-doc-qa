import requests
from app.config_loader import load_config

config = load_config()
api_key = config["llm"]["api_key"]
model = config["llm"]["model"]

print("Using OpenRouter API key:", api_key)
print("Using model:", model)


def query_openrouter(prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost",  # required by OpenRouter
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)

    try:
        res = response.json()
        print("📨 OpenRouter raw response:\n", res)  # Log full response

        if "choices" in res:
            return res["choices"][0]["message"]["content"]
        else:
            raise ValueError("Missing 'choices' in OpenRouter response.")

    except Exception as e:
        print("❌ Error while querying OpenRouter:")
        print("Status code:", response.status_code)
        print("Response body:", response.text)
        raise ValueError("Failed to parse OpenRouter response.") from e
