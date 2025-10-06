import your_rag_module  # Import your RAG system's module

TEST_CONTEXT = [
    # Insert docs here...
]

def call_api(prompt, options, context):
    try:

        # Call only the generation component with the test context
        response = your_rag_module.generate_response(prompt, TEST_CONTEXT)

        return {
            "output": response,
        }
    except Exception as e:
        return {"error": str(e)}
