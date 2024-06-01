import os
import random
from PIL import Image


def crop_image_to_pieces(img, min_w, max_w, min_h, max_h):
    img_width, img_height = img.size
    x = 0
    y = 0
    pieces = []

    while y < img_height:
        while x < img_width:
            width = random.randint(min_w, max_w)
            height = random.randint(min_h, max_h)

            if x + width > img_width:
                width = img_width - x
                if width < min_w:
                    x = img_width - min_w
                    width = min_w

            if y + height > img_height:
                height = img_height - y
                if height < min_h:
                    y = img_height - min_h
                    height = min_h

            box = (x, y, x + width, y + height)
            pieces.append(img.crop(box))
            x += width

        x = 0
        y += height

    return pieces

def img_cropper(input_folder, output_folder, min_w, max_w, min_h, max_h):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    count = 1
    
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        img = Image.open(image_path)
        img_width, img_height = img.size
        if img_width > 400 and img_height > 250: 
            pieces = crop_image_to_pieces(img, min_w, max_w, min_h, max_h)
            
            for piece in pieces:
                piece.save(os.path.join(output_folder, f"{count}.png"))
                count += 1
        else:
            img.save(os.path.join(output_folder, f"{count}.png"))
            count += 1

input_folder = "C:\\Users\\Azzer\\VScodeProjects\\Diplom\\in\\in1"
output_folder = "C:\\Users\\Azzer\\VScodeProjects\\Diplom\\in\\maps5"

img_cropper(input_folder, output_folder, 300, 400, 150, 250)
