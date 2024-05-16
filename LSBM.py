'''

Requirements:
- Pillow pckg.
- Numpy pckg.
- Img. ( one image for testing )

'''

## Using LSBM to hide and extract string from an img
from PIL import Image

def encode_message(img_path, message):
    img = Image.open(img_path)
    encoded_img = img.copy()
    width, height = img.size
    index = 0
    message += "}" # A special character indicating the end of the message
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    data_len = len(binary_message)
    for row in range(height):
        for col in range(width):
            if index < data_len:
                pixel = list(img.getpixel((col, row)))
                # Change the LSB of the first channel to match the message bit
                pixel[0] = pixel[0] & ~1 | int(binary_message[index])
                encoded_img.putpixel((col, row), tuple(pixel))
                index += 1
            else:
                return encoded_img
    return encoded_img

def decode_message(img_path):
    img = Image.open(img_path)
    binary_message = ""
    width, height = img.size

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            binary_message += str(pixel[0] & 1)
            # Check if we've reached the end marker for the message
            if binary_message.endswith('01111101'): # Binary for "}"
                return ''.join([chr(int(binary_message[i:i + 8], 2)) for i in range(0, 
len(binary_message) - 8, 8)])
    return ""

#  Example usage
encoded_img = encode_message('1.jpeg', 'hello world')
encoded_img.save('encoded_image.png')
message = decode_message('encoded_image.png')
print(message)


# ----------------------------------------------------------------
## Extracting Image LSB

from PIL import Image
import numpy as np

def string_to_binary(input_string):
    return ' '.join(format(ord(char), 'b') for char in input_string)

def extract_lsb_matrix(image_path, color_channel, last_row_index, last_col_index):
    # Load the image
    img = Image.open(image_path)

    # Convert image to numpy array
    img_array = np.array(img)
    # Extract the specified color channel
    # Assume color_channel is one of 'R', 'G', 'B' for an RGB image
    channel_index = {'R': 0, 'G': 1, 'B': 2}[color_channel]
    channel_data = img_array[:, :, channel_index]
    # Slice the matrix to the specified dimensions
    sub_matrix = channel_data[:last_row_index + 1, :last_col_index + 1]
    # Extract the LSB of each element in the sub-matrix
    lsb_matrix = np.bitwise_and(sub_matrix, 1)
    return lsb_matrix


# Example usage
color_channel = 'R' # For Red channel
last_row_index = 0 # Example index for the last row
last_col_index = 100 # Example index for the last column
print("The binary representation: ",string_to_binary("hello world"))
orglsb_matrix = extract_lsb_matrix('1.jpeg', color_channel, last_row_index, 
last_col_index)
print("Original img : ",orglsb_matrix)
enclsb_matrix = extract_lsb_matrix('encoded_image.png', color_channel, 
last_row_index, last_col_index)
print("New img : ",enclsb_matrix)
