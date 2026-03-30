🤖 AI Customer Support Chatbot

An AI-powered customer support chatbot built using Groq (LLaMA model), Pandas, and Gradio.
This chatbot uses real customer support data to generate accurate and professional responses.

🚀 Features
💬 Real-time chatbot interface
🧠 Powered by LLaMA 3.1 (Groq API)
📊 Uses real customer support dataset
⚡ Fast responses with optimized sampling
🌐 Shareable web interface using Gradio


🛠️ Tech Stack
Python
Groq API (LLaMA 3.1 model)
Pandas
Gradio


📂 Dataset
Bitext Sample Customer Support Dataset
Contains:
instruction → User query
response → Expected reply



⚙️ Installation
pip install groq pandas gradio


🔑 Setup
Get your API key from Groq
Replace in code:
client = Groq(api_key="YOUR_API_KEY")



🧠 How It Works
Load and clean dataset
Select important columns (instruction, response)
Sample small dataset for faster API calls
Build prompt using examples (few-shot learning)
Send prompt to LLaMA model
Display response using Gradio UI


🧩 Project Structure
├── chatbot.ipynb
├── dataset.csv
└── README.md



▶️ Run the Project
demo.launch(share=True)
Generates a public link to access chatbot
💡 Example

User:

I want to cancel my order

Bot:

I'm sorry to hear that. Let me help you with the cancellation process...

🎯 Use Cases
Customer support automation
Helpdesk chatbot
FAQ assistant
E-commerce support


📌 Future Improvements
Add database integration
Use full dataset (no sampling)
Add memory/chat history
Deploy on cloud (AWS / GCP)
🧾 License

This project is for educational purposes.

🙌 Author

Siddharth Patil

<img width="1260" height="625" alt="image" src="https://github.com/user-attachments/assets/230488eb-6607-4b90-b8c4-f3655cda1733" />

<img width="1059" height="537" alt="image" src="https://github.com/user-attachments/assets/19e45d7e-53e1-400e-a5f9-6b475c04a549" />

<img width="1136" height="608" alt="image" src="https://github.com/user-attachments/assets/3844feaf-65d8-4c08-8af1-a4e6a6b17a5d" />
