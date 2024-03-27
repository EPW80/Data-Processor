

import re

def read_file(file_path):
    """Read the content of the input file."""
    with open(file_path, 'r') as file:
        return file.read()

def remove_comments_and_excess_space(code):
    """Remove comments and excessive whitespace from the code."""
    code_no_comments = re.sub(r'#.*', '', code)
    code_no_excess_space = re.sub(r'\s+', ' ', code_no_comments, flags=re.MULTILINE).strip()
    return code_no_excess_space

def tokenize(code):
    """Tokenize the code into keywords, identifiers, operators, delimiters, and literals."""
    tokens = {
        'Keywords': set(),
        'Identifiers': set(),
        'Operators': set(),
        'Delimiters': set(),
        'Literals': set()
    }
    keyword_pattern = r'\b(def|return|print)\b'
    operator_pattern = r'[\=|\+]'
    delimiter_pattern = r'[\(\)\:\,]'
    literal_pattern = r'\b\d+\b'
    
    tokens['Keywords'].update(re.findall(keyword_pattern, code))
    tokens['Operators'].update(re.findall(operator_pattern, code))
    tokens['Delimiters'].update(re.findall(delimiter_pattern, code))
    tokens['Literals'].update(re.findall(literal_pattern, code))
    
    identifiers_pattern = r'\b[a-zA-Z_]\w*\b'
    all_identifiers = set(re.findall(identifiers_pattern, code))
    tokens['Identifiers'] = all_identifiers - tokens['Keywords'] - tokens['Literals']
    
    return tokens

def print_clean_code(code):
    """Print the code after removing excess space and comments."""
    print(code)

def print_tokenized_code(tokens):
    """Print the tokenized code in a tabular format."""
    print(f"{'Category':<12}Tokens")
    for category, tokens_set in tokens.items():
        print(f"{category:<12}{' '.join(tokens_set)}")

# Main execution
if __name__ == "__main__":
    file_path = 'input.txt'  

    # Read the file
    code = read_file(file_path)

    # Remove comments and excess space
    clean_code = remove_comments_and_excess_space(code)

    # Tokenize the cleaned code
    tokens = tokenize(clean_code)

    # Print the cleaned code
    print("Output1 - Code after removing excess space and comments:")
    print_clean_code(clean_code)

    # Print the tokenized code in tabular form
    print("\nOutput2 - Tokenized code in tabular form:")
    print_tokenized_code(tokens)
