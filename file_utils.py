import json
import csv
import logging

# Function to write processed data to a JSON file
def write_to_json(output_file_path, data):
    try:
        with open(output_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        logging.error(f"Error writing to JSON file: {e}")
        return False

# Function to write processed data to a CSV file
def write_to_csv(output_file_path, data):
    try:
        with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            for entry in data:
                writer.writerow(entry)
        return True
    except Exception as e:
        logging.error(f"Error writing to CSV file: {e}")
        return False

# Main function to write output based on the selected format
def write_output(output_file_path, structured_data, output_format):
    if output_format == 'json':
        return write_to_json(output_file_path, structured_data)
    elif output_format == 'csv':
        return write_to_csv(output_file_path, structured_data)
    else:
        logging.error(f"Unsupported file format: {output_format}")
        return False