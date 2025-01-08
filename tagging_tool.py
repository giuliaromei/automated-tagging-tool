from openai import OpenAI
import json
import os
from pathlib import Path
from typing import List, Dict

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Function to split text into paragraphs
def split_text_into_paragraphs(text: str) -> List[str]:
    return text.split("\n\n")

# Function to create a dynamic prompt based on user instructions and paragraph
def create_prompt(paragraph: str, desired_tags: List[str], tagging_instructions: str) -> str:

    tag_list = ", ".join(desired_tags)
   
    prompt = (
        "You are a text tagging assistant. Analyze the provided paragraph and identify the relevant tags "
        "from the list of available tags provided below.\n\n"
        "## TASK\n"
        "Your task is to return the relevant list of tags for a given paragraph adhering to the following guidelines\n\n"
        "## GUIDELINES\n"
        "- Return the tags that apply to the text as an array with the following format: [\"Tag1\", \"Tag2\"]\n"
        "- Only include tags from the provided list of available tags\n"
        "- Make sure you always include at least 1 tag. You can include more if applicable.\n"
        "- Return the plain list following the specified format with no comments or annotations.\n\n"
        "## AVAILABLE TAGS\n"
        f"{tag_list}\n\n"
        "## ADDITIONAL TAGGING INSTRUCTIONS\n"
        f"{tagging_instructions}\n\n"
        "## PARAGRAPH\n"
        f"{paragraph}"
    )
    
    return prompt

# Function to submit tagging request to the LLM
def tag_text_with_llm(prompt):

    # Example LLM API call (requires an OpenAI API key)
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a skilled text tagging assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o",
        temperature=0.3
    )

    # Extract the tagging result
    tags = response.choices[0].message.content
    print (tags)
    return tags

# Main function to process text and return tagged data
def process_text(text: str, desired_tags: List[str], tagging_instructions: str) -> List[Dict[str, str]]:
    paragraphs = split_text_into_paragraphs(text)
    tagged_data = []

    for paragraph in paragraphs:
        if paragraph.strip():  # Skip empty paragraphs
            try:
                prompt = create_prompt(paragraph, desired_tags, tagging_instructions)
                print (prompt)
                result = tag_text_with_llm(prompt)
                tags = result if isinstance(result, list) else json.loads(result)
                tagged_data.append({"text": paragraph, "tags": tags})
            except Exception as e:
                print(f"Error tagging paragraph: {e}")

    # Save results to a JSON file
    try:
        with open("marked_up_data.json", "w", encoding="utf-8") as file:
            json.dump(tagged_data, file, indent=4, ensure_ascii=False)
        print(f"Tagged data saved to marked_up_data.json")
    except Exception as e:
        print(f"Error saving to file: {e}")

# Function to read content from txt file
def read_file(file_path):
    """Read and return the text content of a file."""
    ext = Path(file_path).suffix.lower()
    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    else:
        raise NotImplementedError("Parsing for this file type to be implemented.")


# Example usage
def main():

    # Input file
    input_file = input("Enter the path of the file containing the text for tagging: ")
    text_input = read_file(input_file)

    # Desired tags provided by the user
    user_desired_tags = input("Enter a list of available tags as a comma-separated attay, ie [\"tag1\", \"tag2\"]:")
    # Additional tagging instructions provided by the user
    tagging_instructions = input("Enter any tagging instructions:")

    # Process the text
    tagged_results = process_text(text_input, user_desired_tags, tagging_instructions)

    # Output the results
    print(json.dumps(tagged_results, indent=4))


if __name__ == "__main__":
    main()
