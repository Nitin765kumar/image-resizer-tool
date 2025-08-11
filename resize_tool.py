# resize_tool.py

import os
from PIL import Image

def resize_image(input_image_path, output_folder, new_width, new_height):
    """
    Resizes an image to the specified dimensions and saves it to the output folder.

    Args:
        input_image_path (str): The full path to the input image file.
        output_folder (str): The path to the folder where the resized image will be saved.
        new_width (int): The desired width for the resized image.
        new_height (int): The desired height for the resized image.
    """
    try:
        # Open the image
        with Image.open(input_image_path) as img:
            # Resize the image using the THUMBNAIL filter for high quality
            # Use ANTIALIAS or BICUBIC for downsampling, or BILINEAR for upsampling
            # For general resizing, Image.LANCZOS (high quality downsampling) is often preferred.
            img = img.resize((new_width, new_height), Image.LANCZOS)

            # Create the output folder if it doesn't exist
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            # Construct the output file path
            file_name = os.path.basename(input_image_path)
            name, ext = os.path.splitext(file_name)
            output_image_path = os.path.join(output_folder, f"{name}_resized{ext}")

            # Save the resized image
            img.save(output_image_path)
            print(f"Image '{file_name}' resized successfully to {new_width}x{new_height} and saved at '{output_image_path}'")

    except FileNotFoundError:
        print(f"Error: Input image not found at '{input_image_path}'")
    except ValueError as e:
        print(f"Error processing image: {e}. Check image format or dimensions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the image resizer tool.
    Prompts the user for input and calls the resize_image function.
    """
    # Define input and output folders relative to the script's location
    script_dir = os.path.dirname(__file__)
    input_images_folder = os.path.join(script_dir, "images")
    output_resized_folder = os.path.join(script_dir, "resized_images")

    print("--- Image Resizer Tool ---")
    print(f"Input images expected in: {os.path.abspath(input_images_folder)}")
    print(f"Resized images will be saved in: {os.path.abspath(output_resized_folder)}\n")

    # List available images in the input folder
    if not os.path.exists(input_images_folder):
        print(f"Error: Input folder '{input_images_folder}' not found. Please create it and add images.")
        return

    available_images = [f for f in os.listdir(input_images_folder) if os.path.isfile(os.path.join(input_images_folder, f))]
    if not available_images:
        print("No images found in the 'images' folder. Please add some images to resize.")
        return

    print("Available images:")
    for i, img_name in enumerate(available_images):
        print(f"{i+1}. {img_name}")

    try:
        image_choice = int(input("\nEnter the number of the image to resize: "))
        if not (1 <= image_choice <= len(available_images)):
            print("Invalid image number.")
            return

        selected_image_name = available_images[image_choice - 1]
        full_input_path = os.path.join(input_images_folder, selected_image_name)

        new_width = int(input("Enter new width (pixels): "))
        new_height = int(input("Enter new height (pixels): "))

        if new_width <= 0 or new_height <= 0:
            print("Width and height must be positive integers.")
            return

        resize_image(full_input_path, output_resized_folder, new_width, new_height)

    except ValueError:
        print("Invalid input. Please enter numbers for image choice, width, and height.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()