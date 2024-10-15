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
                      # tool_resources={
                      #   "file_search": {
                      #     "file_ids": [file.id]
                      #   }
                      # }
                    )

           # # Create a vector store caled "Financial Statements"
           # vector_store = openai.beta.vector_stores.create(name="Nonprofit List")
 
           # # Ready the files for upload to OpenAI
           # file_paths = ["nonprofitlist.pdf"]
           # file_streams = [open(path, "rb") for path in file_paths]
 
           #  # Use the upload and poll SDK helper to upload the files, add them to the vector store,
           #  # and poll the status of the file batch for completion.
           # file_batch = openai.beta.vector_stores.file_batches.upload_and_poll(
           #    vector_store_id=vector_store.id, files=file_streams
           # )
 
           #  # You can print the status and the file counts of the batch to see the result of this operation.
           # print(file_batch.status)
           # print(file_batch.file_counts)

           # assistant = openai.beta.assistants.update(
           #    assistant_id=assistant.id,
           #    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
           #  )

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

           # Use the create and poll SDK helper to create a run and poll the status of
           # the run until it's in a terminal state.

           run = openai.beta.threads.runs.create_and_poll(
               thread_id=thread.id, assistant_id=assistant.id
           )

           messages = list(openai.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

           message_content = messages[0].content[0].text
           # annotations = message_content.annotations
           # citations = []
           # for index, annotation in enumerate(annotations):
           #     message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
           #     if file_citation := getattr(annotation, "file_citation", None):
           #         cited_file = openai.files.retrieve(file_citation.file_id)
           #         citations.append(f"[{index}] {cited_file.filename}")

           response_text = message_content.value # + "\n".join(citations)
           return response_text

           # response = openai.beta.threads.runs.create(
           #      thread_id=thread.id,
           #      assistant_id=assistant.id,
           #      model="gpt-4o-mini",
           #      instructions="You are a chatbot who converses with people that are trying to find a nonprofit which matches their goals to donate to or volunteer at. By cross-referencing the user's requirements with your data, you provide the user one or more nonprofits that would best suit them in a conversational format.",
           #      tools=[{"type": "file_search"}]
           #  )
           # return response.choices[0].text.strip()  # Extract and return the response
     except Exception as e:
           return f"Error: {e}"
