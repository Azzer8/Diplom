import cv2
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import time
import logging
# logging.getLogger('ppocr').setLevel(logging.ERROR)

def detect(img):
    image = cv2.imread(f'in/{img}')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 65, 255, cv2.THRESH_BINARY & cv2.THRESH_OTSU)

    ocr = PaddleOCR(lang='en', use_angle_cls=False)
    start_time = time.time()
    result = ocr.ocr(image, cls=False)
    end_time = time.time() - start_time

    result = result[0]
    # image = Image.open(f'diplom/in/{img}').convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    # scores = [line[1][1] for line in result]
    # im_show = draw_ocr(image, boxes, font_path='diplom/latin.ttf')

    k = 0
    for i in range(len(txts)):
        x, y = int(boxes[i][0][0]), int(boxes[i][0][1])
        w, h = int(boxes[i][2][0]) - x, int(boxes[i][2][1]) - y
        
        if w < 30 and h < 30:
            k+=1
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(image, txts[i], (x, y+h+13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

    # im_show = Image.fromarray(im_show)
    # im_show.save(f'diplom/out/res_{img}')
    cv2.imwrite(f'out/res_PaddleOCR_{img}', image)

    # print(k / len(txts))
    # print(end_time)
    # print()

detect("image1.png")
# detect("image2.png")
# detect("image3.png")
# detect("image4.png")