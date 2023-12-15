from dotenv import load_dotenv
import os
from openai import OpenAI

client = OpenAI()
import docx

load_dotenv('config.env')

# Function to read .docx file
def read_docx(file_path):
    doc = docx.Document(file_path)
    fullText = [paragraph.text for paragraph in doc.paragraphs]
    return '\n'.join(fullText)


resume = read_docx('resume.docx')
job_description = read_docx('jd.docx')


# Combine resume and job description in a prompt for the API
prompt = f"Resume: {resume}\n\nJob Description: {job_description}\n\n" \
         "Score the resume on how well it matches the job description out of 100. Respond only with score out of 100"


# # Send the prompt to the OpenAI API
# response = client.chat.completions.create(
#     model="gpt-4",
#     prompt=prompt,
#     max_tokens=50)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Extracting the message content from the response
message_content = response.choices[0].message.content

# Printing the message content
print(message_content)