from PIL import Image, ImageEnhance, ImageFilter

# Load an image from the user input
def load_image():
    image_path = input("Enter the image file path: ")
    try:
        img = Image.open(image_path)
        img.show()  # Display the original image
        return img
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
def change_brightness(img):
    enhancer = ImageEnhance.Brightness(img)
    factor = float(input("Enter brightness level (e.g., 1.5 for brighter, 0.5 for darker): "))
    bright_img = enhancer.enhance(factor)
    bright_img.show()  # Display the modified image
    return bright_img
def change_contrast(img):
    enhancer = ImageEnhance.Contrast(img)
    factor = float(input("Enter contrast level (e.g., 1.5 for more contrast, 0.5 for less contrast): "))
    contrast_img = enhancer.enhance(factor)
    contrast_img.show()  # Display the modified image
    return contrast_img
def apply_blur(img):
    blurred_img = img.filter(ImageFilter.BLUR)
    blurred_img.show()  # Display the blurred image
    return blurred_img
def save_image(img):
    save_path = input("Enter the file path to save the modified image (e.g., output.jpg): ")
    img.save(save_path)
    print(f"Image saved as {save_path}")
# Main function to choose actions
def main():
    img = load_image()
    if img is None:
        return
    
    while True:
        print("\nChoose an action:")
        print("1. Change Brightness")
        print("2. Change Contrast")
        print("3. Apply Blur")
        print("4. Save and Exit")
        print("5. Exit without Saving")

        choice = input("Enter your choice: ")

        if choice == '1':
            img = change_brightness(img)
        elif choice == '2':
            img = change_contrast(img)
        elif choice == '3':
            img = apply_blur(img)
        elif choice == '4':
            save_image(img)
            break
        elif choice == '5':
            print("Exiting without saving.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
