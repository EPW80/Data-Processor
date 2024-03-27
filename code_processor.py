import re


def read_file(file_path):
    """Read the content of the input file."""
    with open(file_path, "r") as file:
        return file.read()


def remove_comments_and_excess_space(code):
    """Remove comments and excessive whitespace from the code while preserving structure."""
    # Remove inline comments
    code_no_comments = re.sub(r"#.*", "", code)
    # Remove leading and trailing whitespace from each line
    lines = [line.strip() for line in code_no_comments.split("\n")]
    # Remove empty lines
    non_empty_lines = [line for line in lines if line]
    # Join lines back with a newline character
    structured_code = "\n".join(non_empty_lines)
    return structured_code


def tokenize(code):
    """Tokenize the code into keywords, identifiers, operators, delimiters, and literals."""
    tokens = {
        "Keywords": set(),
        "Identifiers": set(),
        "Operators": set(),
        "Delimiters": set(),
        "Literals": set(),
    }
    keyword_pattern = r"\b(def|return|print)\b"
    operator_pattern = r"[\=|\+]"
    delimiter_pattern = r"[\(\)\:\,]"
    literal_pattern = r"\b\d+\b"

    tokens["Keywords"].update(re.findall(keyword_pattern, code))
    tokens["Operators"].update(re.findall(operator_pattern, code))
    tokens["Delimiters"].update(re.findall(delimiter_pattern, code))
    tokens["Literals"].update(re.findall(literal_pattern, code))

    identifiers_pattern = r"\b[a-zA-Z_]\w*\b"
    all_identifiers = set(re.findall(identifiers_pattern, code))
    tokens["Identifiers"] = all_identifiers - tokens["Keywords"] - tokens["Literals"]

    return tokens


def print_clean_code(code):
    """Print the code after removing excess space and comments."""
    print("Output1 - Cleaned Code:")
    print("-----------------------")
    print(code)
    print("-----------------------\n")


def print_tokenized_code(tokens):
    """Print the tokenized code in a more professional tabular format."""
    print("Output2 - Tokenized Code in Tabular Form:")
    print("-----------------------------------------")
    print(f"{'Category':<12} | Tokens")
    print("-----------------------------------------")
    for category, tokens_set in sorted(tokens.items()):
        # Sort tokens for consistent ordering
        sorted_tokens = sorted(tokens_set)
        print(f"{category:<12} | {' '.join(sorted_tokens)}")
    print("-----------------------------------------")


# Main execution
if __name__ == "__main__":
    file_path = "input.txt"

    print("Starting Code Analysis...\n")

    # Read the file
    code = read_file(file_path)
    print("File read successfully.\n")

    # Remove comments and excess space
    clean_code = remove_comments_and_excess_space(code)

    # Tokenize the cleaned code
    tokens = tokenize(clean_code)

    # Print the cleaned code
    print_clean_code(clean_code)

    # Print the tokenized code in tabular form
    print_tokenized_code(tokens)

    print("Code analysis completed. BUh-Bye!")
