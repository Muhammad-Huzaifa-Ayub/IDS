
import os
from PIL import Image, UnidentifiedImageError


# A. Accept multiple image filenames using os.listdir()

cwd = os.getcwd()
print("\nCurrent working directory:", cwd)

dir_list = os.listdir(cwd)

image_files = []

for file in dir_list:
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        image_files.append(file)

print("\n === Image files in current directory === ")

for file in image_files:
    print(file)


# F. Create ProcessedImages directory

os.makedirs("ProcessedImages", exist_ok=True)


# B, C, H. Open image and perform selected transformation

def process_image(filename, choice, crop_box=None, new_size=None,
                  rotate_direction=None):

    try:
        # G. Check whether image exists

        if not os.path.exists(filename):
            raise FileNotFoundError

        img = Image.open(filename)

        print("\nImage opened successfully!")
        print("Image Name:", img.filename)
        print("Format:", img.format)
        print("Dimensions:", img.size)
        print("Mode:", img.mode)

        # C. Resize image

        if choice == "1":
            processed_img = img.resize(new_size)
            prefix = "resized"

        # C. Crop image

        elif choice == "2":
            left, upper, right, lower = crop_box

            if (left < 0 or upper < 0 or
                right > img.width or lower > img.height or
                left >= right or upper >= lower):

                raise ValueError("Invalid crop coordinates!")

            processed_img = img.crop(crop_box)
            prefix = "cropped"

        # C. Rotate image left or right

        elif choice == "3":

            if rotate_direction == "1":
                processed_img = img.rotate(90)
                prefix = "rotated_left"

            else:
                processed_img = img.rotate(-90)
                prefix = "rotated_right"

        # C. Convert image into grayscale

        elif choice == "4":
            processed_img = img.convert("L")
            prefix = "grayscale"

        # F. Save processed image in ProcessedImages folder

        output_name = prefix + "_" + os.path.basename(filename)

        output_path = os.path.join("ProcessedImages", output_name)

        processed_img.save(output_path)

        print("Processed image saved:", output_path)
        print("Processed dimensions:", processed_img.size)

        img.close()
        processed_img.close()

        return output_path

    except FileNotFoundError:
        print("Error: Image file not found:", filename)

    except UnidentifiedImageError:
        print("Error: Unsupported image format:", filename)

    except ValueError as e:
        print("Error:", e)

    except OSError as e:
        print("File or saving error:", e)

    return None


# E. Check image dimensions using filter()

def is_large_image(filename):

    try:
        with Image.open(filename) as img:
            return img.width > 500 and img.height > 500

    except (FileNotFoundError, UnidentifiedImageError, OSError):
        return False


# Main menu

processed_files = []

while True:

    print("\n ===== IMAGE MANAGEMENT MENU ===== ")
    print("1. Resize image")
    print("2. Crop image")
    print("3. Rotate image")
    print("4. Grayscale image")
    print("5. Display large images")
    print("6. Display file information")
    print("7. Display original and processed images")
    print("0. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "0":
        break

    # E. Display large images using filter()

    elif choice == "5":

        large_images = list(
            filter(lambda filename: is_large_image(filename), image_files)
        )

        print("\nImages larger than 500 x 500 pixels:")

        for file in large_images:
            print(file)

    # G. Display file information using os.stat()

    elif choice == "6":

        print("\nImage file information:")

        for file in image_files:

            if os.path.exists(file):

                file_info = os.stat(file)

                print("\nFilename:", file)
                print("File size:", file_info.st_size, "bytes")
                print("Last modified:", file_info.st_mtime)

            else:
                print("File does not exist:", file)

    # I. Display original and processed image names

    elif choice == "7":

        print("\nOriginal Image Names:")

        for file in image_files:
            print(file)

        print("\nProcessed Image Names:")

        for file in processed_files:

            if file is not None:
                print(os.path.basename(file))

    # C. Image transformations

    elif choice in ("1", "2", "3", "4"):

        print("\nSelect image:")

        for i, file in enumerate(image_files, start=1):
            print(i, ".", file)

        try:
            selection = input("Enter image number(s), e.g. 1,3: ")

            selected_images = []

            for number in selection.split(","):

                index = int(number.strip()) - 1

                if index < 0 or index >= len(image_files):
                    raise ValueError("Invalid image number!")

                selected_images.append(image_files[index])

        except ValueError as e:
            print("Error:", e)
            continue

        crop_box = None
        new_size = None
        rotate_direction = None

        try:

            # Resize dimensions

            if choice == "1":

                new_width = int(input("Enter new width: "))
                new_height = int(input("Enter new height: "))

                if new_width <= 0 or new_height <= 0:
                    raise ValueError("Width and height must be positive!")

                new_size = (new_width, new_height)

            # Crop coordinates

            elif choice == "2":

                print("\nEnter crop coordinates:")

                left = int(input("Left: "))
                upper = int(input("Upper: "))
                right = int(input("Right: "))
                lower = int(input("Lower: "))

                crop_box = (left, upper, right, lower)

            # Rotate direction

            elif choice == "3":

                print("\nSelect rotation direction:")
                print("1. Rotate Left")
                print("2. Rotate Right")

                rotate_direction = input("Enter your choice (1-2): ")

                if rotate_direction not in ("1", "2"):
                    raise ValueError("Invalid rotation choice!")

        except ValueError as e:
            print("Error:", e)
            continue

        # D. Apply transformation using map() and lambda

        new_processed_files = list(
            map(
                lambda filename: process_image(
                    filename, choice, crop_box,
                    new_size, rotate_direction
                ),
                selected_images
            )
        )

        processed_files.extend(new_processed_files)

    else:
        print("Invalid choice!")


print("\nImage processing application closed!")
