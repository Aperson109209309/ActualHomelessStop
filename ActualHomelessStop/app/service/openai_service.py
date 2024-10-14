import openai
from django.conf import settings

from app import views
   
   # Set the OpenAI API key
openai.api_key = settings.OPENAI_API_KEY
def get_openai_response(prompt):
     try:
           # Send a request to the OpenAI API
           file = openai.files.create(
                      file=open("nonprofitlist.pdf", "rb"),
                      purpose='assistants'
                    )
           assistant = openai.beta.assistants.create(
                      name="Homeless Stop Chatbot",
                      description="You are a chatbot who converses with people that are trying to find a nonprofit which matches their goals to donate to or volunteer at. By cross-referencing the user's requirements with your data, you provide the user one or more nonprofits that would best suit them in a conversational format.",
                      model="gpt-4o-mini",
                      tools=[{"type": "file_search"}],
                      tool_resources={
                        "file_search": {
                          "file_ids": [file.id]
                        }
                      }
                    )
           thread = openai.beta.threads.create(
                  messages=[
                    {
                      "role": "user",
                      "content": "Search for a nonprofit that matches the user's needs based off the nonprofitlist.pdf file.",
                      "attachments": [
                        {
                          "file_id": file.id,
                          "tools": [{"type": "file_search"}]
                        }
                      ]
                    }
                  ]
                )
           response = openai.beta.threads.runs.create(
                thread_id=thread.id,
                assistant_id=assistant.id,
                model="gpt-4o-mini",
                instructions="You are a chatbot who converses with people that are trying to find a nonprofit which matches their goals to donate to or volunteer at. By cross-referencing the user's requirements with your data, you provide the user one or more nonprofits that would best suit them in a conversational format.",
                tools=[{"type": "file_search"}]
            )
           return response.choices[0].text.strip()  # Extract and return the response
     except Exception as e:
           return f"Error: {e}"
