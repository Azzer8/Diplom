import os

def rename_images_in_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    for count, image_file in enumerate(image_files, start=1):
        input_path = os.path.join(folder_path, image_file)
        output_path = os.path.join(output_folder, f"{count}.png")
        os.rename(input_path, output_path)


folder_path = "C:\\Users\\Azzer\\VScodeProjects\\Diplom\\in\\maps3"
output_folder = "C:\\Users\\Azzer\\VScodeProjects\\Diplom\\in\\maps"

rename_images_in_folder(folder_path, output_folder)
