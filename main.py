from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    encrypted_img = Image.new(img.mode, img.size)

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            new_pixel = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
            encrypted_img.putpixel((x, y), new_pixel)

    encrypted_img.save(output_path)
    print("Encryption complete! Saved as", output_path)


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    decrypted_img = Image.new(img.mode, img.size)

    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            original_pixel = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
            decrypted_img.putpixel((x, y), original_pixel)

    decrypted_img.save(output_path)
    print("Decryption complete! Saved as", output_path)


# --- Menu loop ---
while True:
    choice = input("Encrypt or decrypt? (e/d, or q to quit): ").strip().lower()

    if choice == "q":
        print("Goodbye!")
        break

    if choice not in ("e", "d"):
        print("Invalid choice, please enter e, d, or q.")
        continue

    filename = input("Enter image filename (e.g. test.jpg): ").strip()

    try:
        key = int(input("Enter key (a number): "))
    except ValueError:
        print("Key must be a number. Try again.")
        continue

    try:
        if choice == "e":
            encrypt_image(filename, "encrypted.png", key)
        else:
            decrypt_image(filename, "decrypted.png", key)
    except FileNotFoundError:
        print("That file wasn't found. Check the filename and try again.")