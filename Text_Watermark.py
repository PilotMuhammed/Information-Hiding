'''
Requirements:
- Pillow pckg.
- 2 imgs. (background image , watermark image )
- Font path

'''

# Text Watermark

from PIL import Image, ImageDraw, ImageFont

def add_text_watermark(image_path, text, position, font_path="ARLRDBD.TTF", font_size=30, color=(255, 255, 255, 128)):

    image = Image.open(image_path).convert("RGBA")

    txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
    font = ImageFont.truetype(font_path, font_size)
    d = ImageDraw.Draw(txt)

    # Add text
    d.text(position, text, fill=color, font=font)

    # Merge text with image
    watermarked = Image.alpha_composite(image, txt)

    # Convert back to RGB and save or display
    watermarked = watermarked.convert("RGB")
    # watermarked.show()  # To display the image
    watermarked.save("watermarked_image.jpg")  # To save the image


# Example usage
# add_text_watermark("background.jpg", "IT",(900, 400),)
# add_text_watermark("background.jpg", "PILOT",(900, 400), color=(255, 0, 0))
add_text_watermark("background.jpg", "PILOT",(900, 400), color=(0, 255, 0))
#add_text_watermark("background.jpg", "PILOT",(900, 400), color=(0, 0, 255))
