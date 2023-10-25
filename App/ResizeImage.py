from PIL import Image

# Open the image
image = Image.open("background.png")  # Replace with the path to your image file

# Define the custom width and height
custom_width = 800
custom_height = 800

# Resize the image to the custom dimensions
resized_image = image.resize((custom_width, custom_height))

# Save the resized image (optional)
resized_image.save("background.png")  # Save the resized image to a file

# Display the resized image (optional)
resized_image.show()  # Opens the image using the default image viewer
