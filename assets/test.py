from PIL import Image

def modify_image(image_path):
    # 打开图像文件
    image = Image.open(image_path)
    # 获取图像的宽高
    width, height = image.size

    # 遍历图像的每个像素
    for x in range(width):
        for y in range(height):
            # 获取像素的 RGB 值
            r, g, b = image.getpixel((x, y))

            # 如果 RGB 值都大于 (220, 220, 220)，则改为 (255, 255, 255)
            if r > 220 and g > 220 and b > 220:
                image.putpixel((x, y), (255, 255, 255))

    # 将修改后的图像保存
    modified_image_path = "modified_" + image_path
    image.save(modified_image_path)
    print("修改后的图像已保存为", modified_image_path)

# 调用函数来修改图像
modify_image("input.jpg")
