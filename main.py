import os
import argparse
from logger import setup_logging
from nltk_setup import download_nltk_resources
from phone_number_utils import extract_phone_numbers
from text_processing import process_text
from file_utils import write_output

def main(input_file_path, output_format, is_logging_enabled):
    setup_logging(is_logging_enabled)
    download_nltk_resources()

    # Determine the output file name based on the input file name and desired format
    base, _ = os.path.splitext(input_file_path)
    output_file_path = f"{base}_processed.{output_format}"

    # Process the input file and extract phone numbers
    structured_data = []
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            phone_numbers, cleaned_line = extract_phone_numbers(line)
            processed_line = process_text(cleaned_line)
            for phone_number in phone_numbers:
                structured_data.append({"phone_number": phone_number, "content": processed_line})

    # Write the processed data to the output file
    if write_output(output_file_path, structured_data, output_format):
        print(f"Preprocessing complete! Processed file saved as: {output_file_path}")
    else:
        print("Failed to write output. Check logs for details.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Preprocess text for information retrieval.")
    parser.add_argument("input_file", help="The path to the input text file.")
    parser.add_argument("--format", choices=['json', 'txt', 'csv'], default='json', help="Output format: json, txt, or csv.")
    parser.add_argument("--logging", action="store_true", help="Enable logging output.")
    args = parser.parse_args()

    main(args.input_file, args.format, args.logging)
    
    print("Script execution completed successfully. End of script.")
