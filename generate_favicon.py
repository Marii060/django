"""
Script to generate a favicon with the letter "T"
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create a 64x64 image
size = (64, 64)
image = Image.new('RGBA', size, (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Draw a colored circle background
circle_color = (164, 229, 238, 255)  # #a4e5ee (matching the bg-pink color in base.html)
draw.ellipse([0, 0, 63, 63], fill=circle_color)

# Try to use a default font, or create a simple text
try:
    # Try to use a system font
    font = ImageFont.truetype("arial.ttf", 40)
except IOError:
    # If arial.ttf is not available, use default
    font = ImageFont.load_default()

# Draw the letter "T" in the center
text = "T"
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

x = (size[0] - text_width) // 2
y = (size[1] - text_height) // 2 - text_bbox[1]  # Adjust for baseline

draw.text((x, y), text, fill=(0, 0, 0, 255), font=font)

# Save as ICO
output_path = os.path.join('static', 'favicon.ico')
image.save(output_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
print(f"Favicon created at {output_path}")
