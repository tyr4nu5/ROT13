import argparse
import codecs
import fontforge
from pathlib import Path
from string import ascii_letters


def ttf_to_rot13(ttf_file: str):
    """Transform a font.ttf file into ROT13"""

    # Copy the font characters
    font = fontforge.open(ttf_file)
    font.selection.all()
    font.copy()

    # Paste them into a new font file
    font2 = fontforge.font()
    font2.selection.all()
    font2.paste()

    # Replace characters with its corresponding ROT13 value
    for char in ascii_letters:
        font2.selection.select(codecs.encode(char, 'rot_13'))
        font2.copy()
        font.selection.select(char)
        font.paste()

    # Modify font metadata
    font.familyname += " ROT13"
    font.fullname += " ROT13"
    font.fontname += "ROT13"

    # Create the new ROT13 encoded font file
    ttf_file = Path(ttf_file).absolute()
    ttf_file = ttf_file.with_stem(f"{ttf_file.stem}ROT13")
    ttf_file.unlink(True)
    font.generate(str(ttf_file))
    font.close()

    return ttf_file


def main():
    # Get parsed arguments
    parser = argparse.ArgumentParser(usage=f"fontforge -script {Path(__file__).name} file")
    parser.add_argument('file', type=Path, help="path to TTF file")

    # Process the arguments
    args = parser.parse_args()
    file = args.file.absolute()

    # Check existence of file with fonts
    if not file.is_file():
        raise FileNotFoundError(file)
    
    rot13_file = ttf_to_rot13(str(file))
    print(f"New ROT13 font: {rot13_file}")


if __name__ == '__main__':
    main()
