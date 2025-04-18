from PIL import Image

def encrypt(img_path, save_path, key):
    img = Image.open(img_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Simple modification: adding key and wrapping with 256
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

    img.save(save_path)
    print("Image encrypted and saved as", save_path)

def decrypt(img_path, save_path, key):
    img = Image.open(img_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Reversing the operation
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    img.save(save_path)
    print("Image decrypted and saved as", save_path)

# Example usage
if __name__ == "__main__":
    key = 50  # You can change this number
    encrypt("input.png", "encrypted.png", key)
    decrypt("encrypted.png", "decrypted.png", key)
