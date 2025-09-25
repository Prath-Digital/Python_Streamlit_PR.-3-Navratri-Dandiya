from PIL import Image

# Open the image
img = Image.open("dandiya_yellow.png").convert("RGBA")

# Get pixel data
pixels = img.getdata()

new_pixels = []
for p in pixels:
    r, g, b, a = p
    # detect yellowish pixels (high R+G, low B)
    if r > 150 and g > 150 and b < 100:
        new_pixels.append((255, 165, 0, a))  # replace with orange
    else:
        new_pixels.append((r, g, b, a))

# Apply new pixel data
img.putdata(new_pixels)

# Resize to 163 x 538
img = img.resize((163, 538))

# Save result
img.save("dandiya_orange.png")

print("✅ Saved as dandiya_orange.png")
