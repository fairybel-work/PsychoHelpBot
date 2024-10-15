from transformers import pipeline
import torch

# Load Hugging Face conversational pipeline
# Use 'cuda:0' for the first GPU, or '-1' for CPU
device = 0 if torch.cuda.is_available() else -1
chatbot = pipeline("text2text-generation", model="google/flan-t5-large", device=device)

def generate_ai_response(user_message: str, user_history: str) -> str:
    """Generate AI response based on user input and history."""
    prompt = f"""
    You are a qualified psychologist with advanced NLP knowledge. Your task is to generate a supportive and empathetic response to the following user input: "{user_message}". 
    Provide practical advice on how to handle bullying, ask open-ended questions to encourage further dialogue, and avoid mentioning your own emotional state. 
    Be someone the user can rely upon for support. Consider the user history: "{user_history}" to make the response more personalized and relevant. 
    Respond only with the AI's answer, without any prefixes or unnecessary text.
    """
    # Generate AI response
    response = chatbot(prompt, max_length=150, do_sample=True, temperature=0.7)
    generated_text = response[0]['generated_text'].strip()  # .strip() removes leading/trailing whitespace

    # Remove any occurrence of "Bot:"
    return generated_text.replace("Bot:", "").strip()