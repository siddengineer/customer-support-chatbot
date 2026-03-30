# Install required libraries
!pip install groq pandas gradio
# Upload dataset
from google.colab import files
uploaded = files.upload()
import pandas as pd

# Load dataset
df = pd.read_csv("Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv")

# Clean data
df = df[['instruction', 'response']]
df = df.dropna()

# Take small sample (important for API)
df = df.sample(20)

print(df.head())
# Build prompt with examples
def build_prompt(user_input):
    examples = ""

    for _, row in df.iterrows():
        examples += f"User: {row['instruction']}\nBot: {row['response']}\n\n"

    prompt = f"""
You are a professional customer support chatbot.

Use the examples below to answer correctly:

{examples}

Now answer this:

User: {user_input}
Bot:
"""
    return prompt
# Groq API integration
from groq import Groq

client = Groq(api_key="YOUR_API_KEY")  # Replace with your key
# Get response from model
def get_response(user_input):
    prompt = build_prompt(user_input)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
# Gradio UI
import gradio as gr

def chat(message, history):
    if history is None:
        history = []

    try:
        bot_reply = get_response(message)
    except Exception as e:
        bot_reply = f"Error: {str(e)}"

    history = history + [(message, bot_reply)]
    return "", history
# Build interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🤖 AI Customer Support Chatbot")

    chatbot = gr.Chatbot(height=400)

    with gr.Row():
        msg = gr.Textbox(placeholder="Type your message...", scale=4)
        send_btn = gr.Button("Send", scale=1)

    clear_btn = gr.Button("Clear Chat")

    # Enter key
    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    # Send button
    send_btn.click(chat, [msg, chatbot], [msg, chatbot])

    # Clear chat
    clear_btn.click(lambda: ("", []), None, [msg, chatbot])

demo.launch(share=True)
