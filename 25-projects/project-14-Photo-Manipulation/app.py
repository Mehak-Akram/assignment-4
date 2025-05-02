from PIL import Image, ImageEnhance, ImageFilter
import cv2

def load_image(path):
    return Image.open(path)

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def apply_blur(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius))

def apply_grayscale(image):
    return image.convert("L")

def save_image(image, output_path):
    image.save(output_path)

if __name__ == "__main__":
    input_path = "flower.jpeg"        
    output_path = "output_image.jpg"

    img = load_image(input_path)

    img = adjust_brightness(img, 1.5)     
    img = adjust_contrast(img, 1.3)       
    img = apply_blur(img, radius=2)       
    img = apply_grayscale(img)           

    save_image(img, output_path)

    print(f"Image saved as {output_path}")
