import json
import time

from app.generation.rag_pipeline import RAGPipeline


def main():

    pipeline = RAGPipeline()

    with open(
        "app/evaluation/questions.json",
        "r",
        encoding="utf-8"
    ) as f:
        questions = json.load(f)

    total_time = 0

    for item in questions:

        question = item["question"]

        start = time.perf_counter()

        response = pipeline.ask(question)

        elapsed = time.perf_counter() - start

        total_time += elapsed

        print("=" * 80)
        print(f"Question : {question}")
        print(f"Latency  : {elapsed:.2f} sec")
        print()

        print(response["answer"])
        print()

        print("Sources:")

        for source in response["sources"]:
            print(source)

    print("=" * 80)
    print(f"Average Latency : {total_time / len(questions):.2f} sec")


if __name__ == "__main__":
    main()