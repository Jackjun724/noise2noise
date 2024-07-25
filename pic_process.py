from PIL import Image
import os


def crop_images(input_dir, output_dir, crop_area):
    """
    批量裁剪图片。

    参数：
        input_dir (str): 输入图片的目录路径。
        output_dir (str): 裁剪后图片的保存目录路径。
        crop_area (tuple): 裁剪区域，格式为 (left, upper, right, lower)。
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(input_dir, filename)
            with Image.open(image_path) as img:
                cropped_img = img.crop(crop_area)
                output_path = os.path.join(output_dir, filename)
                cropped_img.save(output_path)
                print(f'裁剪并保存图片: {output_path}')


# 使用示例
input_directory = 'dataset/pre'
output_directory = 'dataset/corp'
crop_region = (515, 477, 515 + 407, 477 + 113)  # 左、上、右、下的像素值

crop_images(input_directory, output_directory, crop_region)
