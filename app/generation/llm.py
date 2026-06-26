import ollama
from app.configs.settings import settings


class LLM:

    def __init__(
        self,
        model_name: str = settings.llm_model
    ):
        self.model_name = model_name

    def generate(
        self,
        query: str,
        context: str
    ) -> str:

        prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say:
"I could not find that information in the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""

        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]