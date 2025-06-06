from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def get_chat_completion(prompt, model="gpt-4o"):
    
    messages = [
        {"role": "system", "content": "You are an expert on Telenor, a global telecommunications company. Provide accurate and detailed information related to Telenor's business, strategy, and operations."},
        {"role": "user", "content": prompt}
    ]
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,  
    )
    
    generated_content = response.choices[0].message.content

    return generated_content

    
def create_image(prompt):
    response = client.images.generate(
    model="dall-e-3",
    prompt=prompt, 
    size="1024x1024",
    quality="standard",
    n=1,
    )   

    image_url = response.data[0].url
    return image_url
