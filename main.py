from googletrans import Translator
import requests
from bs4 import BeautifulSoup


def read_file(file_path):
    """Read text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def extract_text_from_website(url):
    """Extract and return text from a website."""
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract only paragraph text (cleaner)
    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])

    return text


def translate_text(text, dest_language='es'):
    """Translate text to the target language."""
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text


def save_to_file(text, file_path):
    """Save translated text to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


def main():
    print("🌍 Text Translator")

    file_path = input("Enter file path (or press Enter to skip): ")
    url = input("Enter URL (or press Enter to skip): ")
    target_language = input("Enter target language (e.g., es, fr, hi): ")

    output_file = "translated.txt"

    if file_path:
        text = read_file(file_path)
    elif url:
        text = extract_text_from_website(url)
    else:
        print("You must provide either a file path or a URL.")
        return

    translated_text = translate_text(text, target_language)
    save_to_file(translated_text, output_file)

    print("✅ Translation saved to", output_file)


if __name__ == '__main__':
    main()