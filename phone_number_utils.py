import re

# Define the regular expression for phone numbers
phone_pattern = re.compile(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b')

def anonymize(match):
    phone = match.group()
    anonymized_phone = phone[:-1] + 'X'  # Replace the last digit with 'X'
    return anonymized_phone

def extract_phone_numbers(text):
    found_numbers = phone_pattern.findall(text)
    anonymized_text = phone_pattern.sub(anonymize, text)
    return found_numbers, anonymized_text

# The following block is for testing purposes.
# It will only execute if this script is run directly,
# and not if it's imported from another module.
if __name__ == '__main__':
    test_input = "Contact us at 123-456-7890 or 098-765-4321."
    phone_numbers, anonymized_text = extract_phone_numbers(test_input)
    print("Extracted Phone Numbers:", phone_numbers)
    print("Anonymized Text:", anonymized_text)