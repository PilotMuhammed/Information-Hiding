'''
Requirements:
- Pillow pckg.
- 2 imgs. (background image , watermark image )
- Font path

'''
# Logo Watermark

from turtle import position

from PIL import Image, ImageEnhance

def add_image_watermark(background_image_path, watermark_image_path, position, opacity=180):
    background = Image.open(background_image_path).convert("RGBA")
    watermark = Image.open(watermark_image_path).convert("RGBA")

    #width, height = background.size
    #position = (width - watermark.width, height - watermark.height) # down-right
    #position = (background.width - watermark.width, 0) # up-right
    #position = (0, 0) # up-left
    #position = (0, background.height - watermark.height) # down-left

    #watermark = watermark.resize((200, 150))

    if opacity < 255:
        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity / 255.0)
        watermark.putalpha(alpha)

    transparent = Image.new("RGBA", background.size, (0, 0, 0, 0))

    transparent.paste(watermark, position, watermark)

    result = Image.alpha_composite(background, transparent)

    result = result.convert("RGB")
    result.save("watermarked_image.jpg")


#add_image_watermark("background.jpg", "java-logo.png", position)
add_image_watermark("background.jpg", "java-logo.png", (110, 80))
