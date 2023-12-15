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
         "Score the resume on how well it matches the job description out of 100:"

# Send the prompt to the OpenAI API
response = client.completions.create(
    engine="gpt-4",
    prompt=prompt,
    max_tokens=50)


print(response.choices[0].text.strip())