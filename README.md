# LangChain CSV Chat App 📊  
This project is a Streamlit-based web application that allows you to ask questions about the contents of a CSV file using a powerful Large Language Model (LLM) via LangChain. It uses OpenAI's GPT and the `create_csv_agent` utility from `langchain_experimental.agents` to enable natural language querying of tabular data.  
## Features  
- Upload any CSV file through the web interface  
- Ask natural language questions about the data  
- Get intelligent answers powered by OpenAI's LLM  
- No need to write SQL or code to explore your data  
## Getting Started  
### Clone the repository  
```bash  
git clone https://github.com/yourusername/langchain-csv-chat.git  
cd langchain-csv-chat  
```  
### Create and activate a virtual environment (optional)  
```bash  
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```  
### Install dependencies  
```bash  
pip install -r requirements.txt  
```  
### Set up environment variables  
Create a `.env` file in the root directory and add your OpenAI API key:  
```env  
OPENAI_API_KEY=your_openai_api_key_here  
```  
You can get your OpenAI API key from: https://platform.openai.com/account/api-keys  
### Run the app  
```bash  
streamlit run app.py  
```  
Open your browser and go to the displayed local URL (usually http://localhost:8501).  
## How It Works  
1. User uploads a CSV file via the Streamlit interface  
2. LangChain's `create_csv_agent` reads the CSV and sets up a Q&A interface with the LLM  
3. The app accepts user input as a natural language question  
4. The LLM interprets the question and interacts with the CSV contents to return an answer  
## Project Structure  
```  
langchain-csv-chat/  
├── app.py                 # Main Streamlit app with CSV chat logic  
├── .env                  # Contains your OpenAI API key (not included in repo)  
├── requirements.txt      # Python dependencies  
```  
## Technologies Used  
- Python 3.10+  
- Streamlit  
- LangChain  
- OpenAI GPT  
- dotenv  
## Example Use Cases  
- "What is the average sales in column X?"  
- "Show me the rows where status is 'failed'"  
- "Which item had the highest price?"  
- "Count how many entries are above 500 units"  
## Credits  
- LangChain Experimental Agents  
- Streamlit for interactive UI  
- OpenAI for LLM APIs  

