import numpy as np
import cv2
def normalize_image(image, scale, mean, std):
    # Масштабирование изображения
    image = image * scale
    
    # Нормализация каждого канала
    for i in range(3):
        image[:, :, i] = (image[:, :, i] - mean[i]) / std[i]
    
    return image

# Пример изображения (замените на ваше изображение)
image = cv2.imread('C:\\Users\\Azzer\\VScodeProjects\\Diplom\\PaddleOCR\\train_data\\det\\train\\170802.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Параметры нормализации
scale = 1./255.
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

# Нормализация изображения
normalized_image = normalize_image(image, scale, mean, std)

# Вывод нормализованного изображения
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2)

axes[0].imshow(image)
axes[0].set_title('Original Image')

axes[1].imshow(normalized_image)
axes[1].set_title('Normalized Image')

# Отображаем все изображения
plt.show()
