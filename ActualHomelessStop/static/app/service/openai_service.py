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
