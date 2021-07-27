def encode(char):
    """
    Encodes the character to URL notation

    Args:
        char (chr): the character to encode

    Returns:
        [string]: the percent encoded character
    """
    char_ascii = ord(char)
    char_hex = hex(char_ascii)
    return f"%{char_hex[2::]}"

def main():
    """
    The main program
    """
    url = input("Welcome to the overly excessive URL encoder!\nPlease input a URL!: ")
    output = ""
    for char in url:
        output += encode(char)
    print(f"Here's your overly encoded URL!: {output}")

if __name__ == "__main__":
    # executes the main function as the main function
    main()