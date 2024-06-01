import cv2
import pytesseract
import time


def detect(img):
    image = cv2.imread(f'diplom/in/{img}')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 65, 255, cv2.THRESH_BINARY & cv2.THRESH_OTSU)

    start_time = time.time()
    text_data = pytesseract.image_to_data(image, lang = 'eng', config='--psm 11 -c tessedit_char_whitelist=0123456789', output_type=pytesseract.Output.DICT)
    end_time = time.time() - start_time
    text_data = {key: value for key, value in text_data.items() if key in ['left', 'top', 'width', 'height', 'text']}
    text_data = {key: [value[i] for i, text in enumerate(text_data['text']) if text != ""] for key, value in text_data.items()}
    text_data['text'] = [text.strip() for text in text_data['text'] if text.strip() != ""]

    k = 0
    for i in range(len(text_data['text'])):
        x = text_data['left'][i] - 3
        y = text_data['top'][i] - 3
        w = text_data['width'][i] + 5
        h = text_data['height'][i] + 5
        
        if w < 30 and h < 30:
            k+=1
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(image, text_data['text'][i], (x, y+h+13), cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 1)

    cv2.imwrite(f'diplom/out/res_Tesseract_{img}', image)

    # print(text_data)
    # print(k)
    # print(len(text_data['text']))
    print(k / len(text_data['text']))
    print(end_time)
    print()


detect("image1.png")
detect("image2.png")
detect("image3.png")
detect("image4.png")
