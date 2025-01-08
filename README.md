# automated-tagging-tool
Text Tagging Assistant: LLM-enabled automated tagging with custom tags for synthetic data creation or data visualization purposes

## Overview
This Python script uses OpenAI's API to tag paragraphs from a given text file with relevant labels, based on user-defined tags and instructions. The tagged output is saved in JSON format for further analysis or processing. The script is designed to be interactive, allowing users to input their own tags, instructions, and text files.

## Features
Dynamic Prompting: Creates dynamic prompts based on user-defined tags and instructions.
Flexible Input: Processes unstructured text from a .txt file.
Tagging with LLM: Uses OpenAI's gpt-4o model to classify paragraphs.
JSON Output: Saves the processed data as a JSON file.
Customizable Tagging: Users can specify a list of tags and additional instructions.

## Requirements
Python 3.8 or later
OpenAI Python Library (openai)
An OpenAI API Key, stored in the environment variable OPENAI_API_KEY.

## Setup Instructions
Clone this repository or download the script file.

### Install the required dependencies:
pip install openai

### Set OpenAI API Key, ensure your OpenAI API key is available in your environment variables:
export OPENAI_API_KEY="your_api_key_here"

## How to Use
1. Input File
Prepare a .txt file containing the paragraphs to be tagged.

2. Run the Script
Run the script from the command line:
python tagging_tool.py

3. Provide Input
Follow the on-screen prompts:
- Text File Path: Enter the full path to your .txt file.
- Tags: Provide a list of tags as a JSON array, e.g., ["tag1", "tag2"].
- Tagging Instructions: Enter detailed instructions for tagging (e.g., "Tag paragraphs based on sentiment or factual content.").

4. View Output
The tagged paragraphs are saved to a file named marked_up_data.json in the same directory as the script.

## Functions
1. split_text_into_paragraphs
Splits the input text into paragraphs based on double newline (\n\n) separators.

2. create_prompt
Creates a dynamic prompt for the LLM, incorporating the paragraph, desired tags, and tagging instructions.

3. tag_text_with_llm
Sends the generated prompt to the OpenAI API and retrieves the tags for a paragraph.

4. process_text
Processes the entire text by:
- Splitting it into paragraphs.
- Generating prompts for each paragraph.
- Collecting tags from the LLM.
- Saving the output to marked_up_data.json.

5. read_file
Reads text content from a .txt file. Raises an error if the file format is unsupported.

## Example Input/Output

### Input Text
The financial market has seen significant volatility this year.

Experts advise caution for new investors.

The technology sector continues to innovate at an unprecedented pace.

### Available tags Provided
["fact", "advice"]

### Tagging Instructions
Identify whether the paragraph contains factual information or financial advice.

### Sample output
[
    {
        "text": "The financial market has seen significant volatility this year.",
        "tags": ["fact"]
    },
    {
        "text": "Experts advise caution for new investors.",
        "tags": ["advice"]
    },
    {
        "text": "The technology sector continues to innovate at an unprecedented pace.",
        "tags": ["fact"]
    }
]

## Future Enhancements
Support for additional input formats like .docx or .pdf.
Improved error recovery for API issues (e.g., retries).
Integration with visualization tools for the tagged data.
Advanced chunking mechanisms.
