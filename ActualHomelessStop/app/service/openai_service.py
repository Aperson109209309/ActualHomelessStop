import openai
from django.conf import settings

from app import views
   
   # Set the OpenAI API key
openai.api_key = "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"

def get_openai_response(prompt):
     try:
           # Send a request to the OpenAI API
           response = openai.Completion.create(
               engine="gpt-4",  # or "gpt-4" for GPT-4 models
               prompt=prompt,
               max_tokens=150,  # Adjust the number of tokens based on your need
               temperature=0.7  # Adjust creativity level
           )
           return response.choices[0].text.strip()  # Extract and return the response
     except Exception as e:
           return f"Error: {e}"
