from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st


def main() -> None:
    # Load environment variables
    load_dotenv()

    # Verify the OpenAI API key
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("OpenAI API key is not set. Please check your environment variables.")
        return

    # Streamlit app configuration
    st.set_page_config(page_title="Ask your CSV")
    st.title("Ask your CSV 📊")

    # Upload CSV file
    csv_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if csv_file is None:
        st.info("Please upload a CSV file to begin.")
        return

    # Create LangChain CSV agent
    try:
        agent = create_csv_agent(OpenAI(temperature=0, openai_api_key=openai_api_key), csv_file, verbose=True)
    except Exception as e:
        st.error(f"Error initializing the agent: {e}")
        return

    # User question input
    user_question = st.text_input("Ask a question about your CSV:")
    if user_question:
        with st.spinner("Processing your question..."):
            try:
                response = agent.run(user_question)
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred while processing your question: {e}")


if __name__ == "__main__":
    main()
