from config import client, MODEL


def run_llm(prompt: str):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"LLM Error: {str(e)}"
    