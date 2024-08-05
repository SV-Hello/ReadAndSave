from KeyboardHandler import KeyboardHandler
from ReadCapture import ReadCapture

def main():
    tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    read_capture = ReadCapture(tesseract_cmd)
    handler = KeyboardHandler(read_capture)

    print("Begin.")
    handler.start_listening()

if __name__ == "__main__":
    main()