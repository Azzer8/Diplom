import cv2
import pytesseract


# Функция для распознавания цифр на входном изображении
def ocr_digits(image_path):
    # Считываем изображение
    image = cv2.imread(image_path)

    # Преобразуем в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Применяем пороговую обработку
    _, binary = cv2.threshold(gray, 139, 252, cv2.THRESH_BINARY & cv2.THRESH_OTSU)
    cv2.imshow("", binary)
    cv2.waitKey(0)

    # Распознаем с помощью Tesseract
    text = pytesseract.image_to_string(binary, config='--psm 11 -c tessedit_char_whitelist=0123456789')
    
    return text


def ocr_digits2(image_path, j, i):
    # Считываем изображение
    image = cv2.imread(image_path)

    # Преобразуем в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Применяем пороговую обработку
    _, binary = cv2.threshold(gray, j, i, cv2.THRESH_BINARY & cv2.THRESH_OTSU)
    # cv2.imshow("", binary)
    # cv2.waitKey(0)

    # Распознаем с помощью Tesseract
    text = pytesseract.image_to_string(binary, config='--psm 11 -c tessedit_char_whitelist=0123456789')

    return text


def ocr_digits3(image_path, j, i):
    # Считываем изображение
    image = cv2.imread(image_path)

    # Преобразуем в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Применяем пороговую обработку
    _, binary = cv2.threshold(gray, j, i, cv2.THRESH_BINARY)
    # cv2.imshow("", binary)
    # cv2.waitKey(0)

    # Распознаем с помощью Tesseract
    text = pytesseract.image_to_string(binary, config='--psm 11 -c tessedit_char_whitelist=0123456789')

    return text


def ocr_digits4(image_path, j, i):
    # Считываем изображение
    image = cv2.imread(image_path)

    # Преобразуем в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Применяем пороговую обработку
    _, binary = cv2.threshold(gray, j, i, cv2.THRESH_OTSU)
    # cv2.imshow("", binary)
    # cv2.waitKey(0)

    # Распознаем с помощью Tesseract
    text = pytesseract.image_to_string(binary, config='--psm 11 -c tessedit_char_whitelist=0123456789')

    return text


# Пример использования
input_image_path = "in/image1.png"

result = ocr_digits(input_image_path)
result = result.split("\n")
result = [el for el in result if el != ""]
print(result)
print(len(result))

# arr2 = []
# arr3 = []
# arr4 = []
# for j in range(0, 255):
#     print(j)
#     for i in range(0, 255):
#         result2 = ocr_digits2(input_image_path, j, i)
#         # print(result)
#         result2 = result2.split("\n")
#         result2 = [el for el in result2 if el != ""]
#         # print(result2)
#         if len(result2) >= 180:
#             arr2.append((j, i, len(result2)))
        
        
#         result3 = ocr_digits3(input_image_path, j, i)
#         # print(result)
#         result3 = result3.split("\n")
#         result3 = [el for el in result3 if el != ""]
#         # print(result3)
#         if len(result3) > 180:
#             arr3.append((j, i, len(result3)))
        
        
#         result4 = ocr_digits4(input_image_path, j, i)
#         # print(result)
#         result4 = result4.split("\n")
#         result4 = [el for el in result4 if el != ""]
#         # print(result4)
#         if len(result4) > 180:
#             arr4.append((j, i, len(result4)))
    

# print("BIN_OTSU", arr2)
# print("BIN", arr3)
# print("OTSU", arr4)