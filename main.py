import pytesseract as tess
import wolframalpha
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('math.png')
text = tess.image_to_string(img)
print(text)

question = text
app_id = "PH8RJ2-J579TR7PVT"
client = wolframalpha.Client(app_id)
res = client.query(question)
answer = next(res.results).text
print(f"The answer is: {answer}")