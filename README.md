# PRODIGY_CS_02 - Pixel Manipulation for Image Encryption

A simple Python tool that encrypts and decrypts images by manipulating pixel values.

## How it works
Each pixel's RGB values are shifted by a numeric key using modulo arithmetic 
(similar to a Caesar cipher, but applied to pixel colors instead of letters).
Encryption adds the key to each pixel value; decryption subtracts it.

## Features
- Encrypt or decrypt any image
- User-defined key
- Accepts uppercase or lowercase input (e.g. `E` or `e`)
- Handles invalid input (wrong filenames, non-numeric keys) gracefully

## Usage
Run `main.py`, then follow the prompts:
- Choose `e` to encrypt, `d` to decrypt, or `q` to quit
- Enter the image filename
- Enter a numeric key

The program will keep asking until you choose to quit.

## Built with
- Python
- Pillow (PIL)
