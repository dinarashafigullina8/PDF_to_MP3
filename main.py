from gtts import gTTS
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print(f'Оригинальное имя файла: {Path(file_path).name}')
        print('Файл в процессе')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        # return "Файл есть!"

    else:
        return "Проверьте правильность файла!"


def main():
    print('PDF>>TO>>MP3')
    file_path = input("\n Введите путь до файла:")
    language = input("Выберете язык, например, 'en' или 'ru':")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
