from transformers import pipeline

# Reference:
# https://huggingface.co/docs/transformers/en/main_classes/pipelines

def main():
    # Initialize a question-answering pipeline with a pre-trained model
    qa_pipeline = pipeline(
        "question-answering",
        model="distilbert-base-uncased-distilled-squad"
    )

    # Define your context and question
    context = (
        "Hugging Face is a technology company that provides open-source NLP libraries "
        "and tools for natural language processing tasks."
    )
    question = "What does Hugging Face provide?"

    # Let the pipeline find the best answer based on the context provided
    answer = qa_pipeline(question=question, context=context)

    # Print the results
    print(f"Question: {question}")
    print(f"Answer: {answer['answer']}")

if __name__ == "__main__":
    main()
