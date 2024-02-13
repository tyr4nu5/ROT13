import argparse
import codecs
from pathlib import Path


def main():

    # Get parsed arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=Path, help="file path to encrypt or decrypt")
    
    # Process the arguments
    args = parser.parse_args()
    file = args.file.absolute()
    
    # Check existence of file
    if not file.is_file():
        raise FileNotFoundError(file)

    # Encode or decode file with ROT13
    # Note: encoding and decoding in ROT13 results in the same
    rot13_text = codecs.encode(file.read_text(), 'rot_13')
    file.write_text(rot13_text)

    print(f"New ROT13 file: {file}")

if __name__ == '__main__':
    main()
