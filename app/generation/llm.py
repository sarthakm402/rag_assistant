import ollama


class LLM:

    def __init__(
        self,
        model_name: str = "gemma3:4b"
    ):
        self.model_name = model_name

    def generate(
        self,
        query: str,
        context: str,
        history:str
    ) -> str:

        prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context and make it relaated to question do not just retrun the same fdocs u found from chunks use them to form a coherent answer.

If the answer is not present in the context, say:
"I could not find that information in the provided documents."

Context:
{context}

Question:
{query}
History:
{history}
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