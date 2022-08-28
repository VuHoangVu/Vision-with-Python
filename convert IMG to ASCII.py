from sys import path_importer_cache
from pytesseract import pytesseract
import xlwings as xw
from PIL import Image

path_to_tesseract = r"C:\Programfile\Tesseract-OCR\Tesseract.exe"
image_path = r"D:\Python Project\OpenCV"

img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img, lang="eng")
print(text)