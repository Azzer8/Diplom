import cv2

def resize_image(image, target_height=600, target_width=600):
    original_height, original_width = image.shape[:2]
    aspect_ratio = original_width / original_height
    new_width = int(target_height * aspect_ratio)
    if new_width > target_width:
        new_width = target_width
    resized_image = cv2.resize(image, (new_width, target_height))
    return resized_image

# Загружаем изображение
image = cv2.imread('C:\\Users\\Azzer\\VScodeProjects\\Diplom\\in\\150_200\\2.png')
resized_image = resize_image(image)
cv2.imshow('resized_image', resized_image)
cv2.waitKey(0)
