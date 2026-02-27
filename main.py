from retriever import get_context
from agent import generate_response
from evaluator import evaluate_response

def main():
    print("Placement AI Assistant")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            print("Good luck with placements, Ashaya! 🚀")
            break

        context = get_context(query)
        response = generate_response(query, context)
        evaluation = evaluate_response(response)

        print("\nAssistant:\n", response)
        print("\nEvaluation:", evaluation)
        print("-" * 50)

if __name__ == "__main__":
    main()