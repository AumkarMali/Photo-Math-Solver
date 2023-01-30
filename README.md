


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


# Home Work bot

Utilizes pytesseract and wolframalpha API to solve math problems from picture.
 
  
## Deployment

Get API key at https://products.wolframalpha.com/api

Download python packages

```bash
    pip install pytesseract
    pip install wolframalpha
```

Replace 'API KEY' with your api-key. Download pytesseract to program files.

Tutorial: https://www.youtube.com/watch?v=DG5D8A3zi4o

```bash
    import pytesseract as tess
    import wolframalpha
    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    from PIL import Image

    img = Image.open('math.png')
    text = tess.image_to_string(img)
    print(text)

    question = text
    app_id = "API"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    print(f"The answer is: {answer}")
```

Upload picture of math problem (ei. math.png) then run program.
## Links

➊ Github: https://github.com/AumkarMali/

➋ Youtube: https://www.youtube.com/channel/UC7rhCKur9bF01lV0pNJNkvA
## Demo

https://www.youtube.com/watch?v=5zzBfvukYqk

## Documentation

[Documentation](hhttps://reference.wolfram.com/language/ref/WolframAlpha)


## Authors

- [@AumkarMali](https://www.github.com/AumkarMali)

