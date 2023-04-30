import cv2
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(0)

while True:
    _,image = camera.read()
    cv2.imshow('Text detection',image)
    if cv2.waitKey(1) & 0xFF==ord('s'):
        cv2.imwrite('test1.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()

def tesseract():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = 'test1.jpg'
    pytesseract.tesseract_cmd  = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text)
    search_text =str(input("Enter string to search"))
    lineno=0
    Lines = text.split('\n')
    for line in Lines:
        lineno = lineno+1
        if search_text in line:
            break
    print(f"{search_text} is found in ",lineno)


tesseract()
    
