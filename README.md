<div align="center">

# PRODIGY_CS_02

### Pixel Manipulation for Image Encryption

A lightweight Python image-encryption project that demonstrates reversible pixel transformations using Pillow.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-8A2BE2)](https://python-pillow.org/)
[![Task](https://img.shields.io/badge/Prodigy%20InfoTech-Task%2002-black)](#internship-task)
[![Status](https://img.shields.io/badge/Status-Improved-success)](#features)

</div>

---

## Overview

`PRODIGY_CS_02` is an educational image-processing tool that encrypts and decrypts images by shifting pixel channel values using modulo-256 arithmetic.

The project now includes a cleaner command-line interface, broader image-mode support, transparency preservation, improved error handling, and automated tests.

> **Important:** This project demonstrates reversible pixel manipulation. It is **not cryptographically secure** and should not be used to protect sensitive or confidential data.

---

## Features

| Feature | Supported |
|---|:---:|
| Image encryption | ✅ |
| Image decryption | ✅ |
| RGB images | ✅ |
| RGBA images | ✅ |
| Grayscale images | ✅ |
| Transparency preservation | ✅ |
| Custom input/output paths | ✅ |
| Negative and large keys | ✅ |
| CLI support | ✅ |
| Automated tests | ✅ |

---

## How It Works

The tool applies a reversible numeric shift to image channels.

### Encryption

```text
encrypted_value = (original_value + key) mod 256
```

### Decryption

```text
original_value = (encrypted_value - key) mod 256
```

For images that contain transparency, the alpha channel is preserved rather than modified.

### Example

If a channel value is:

```text
200
```

and the encryption key is:

```text
70
```

then:

```text
(200 + 70) mod 256 = 14
```

Decrypting with the same key restores the original value:

```text
(14 - 70) mod 256 = 200
```

---

## Supported Image Modes

The application directly supports:

- `L` — grayscale
- `LA` — grayscale with alpha
- `RGB` — standard colour
- `RGBA` — colour with transparency

Other Pillow-supported image modes are converted automatically to either `RGB` or `RGBA` before processing.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Phiandi/PRODIGY_CS_02.git
cd PRODIGY_CS_02
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Encrypt an image

```bash
python main.py encrypt input.png encrypted.png --key 42
```

### Decrypt an image

```bash
python main.py decrypt encrypted.png decrypted.png --key 42
```

You can also use the short key flag:

```bash
python main.py encrypt input.jpg encrypted.png -k 120
```

The key may be any integer.

For example:

```text
300 mod 256 = 44
```

so a key of `300` behaves the same as a key of `44`.

---

## Project Structure

```text
PRODIGY_CS_02/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── test/
    └── test_main.py
```

---

## Testing

Run the full test suite with:

```bash
python -m unittest discover -v
```

The tests verify:

- RGB encrypt/decrypt round trips
- RGBA alpha-channel preservation
- Grayscale image support
- Key normalization
- Reversibility of the transformation

---

## Improvements Over the Original Version

The updated implementation improves the original project in several areas:

### Performance

Instead of repeatedly calling `getpixel()` and `putpixel()` inside nested loops, the updated code uses Pillow channel transformations.

### Compatibility

The program no longer assumes every pixel contains exactly three RGB values.

It can now process grayscale and transparency-enabled images safely.

### Usability

The command-line interface lets users provide:

- the operation
- input file path
- output file path
- encryption key

### Reliability

The program now handles:

- missing files
- invalid image files
- unsupported image modes
- large keys
- negative keys

### Maintainability

Core image-processing logic is separated into reusable functions and protected by a standard:

```python
if __name__ == "__main__":
```

entry point.

---

## Example Workflow

```text
Original Image
      │
      ▼
  Encrypt
  key = 42
      │
      ▼
Encrypted Image
      │
      ▼
  Decrypt
  key = 42
      │
      ▼
Original Image Restored
```

---

## Requirements

- Python 3.10+
- Pillow

Install Pillow through:

```bash
pip install -r requirements.txt
```

---

## Security Disclaimer

This project is designed for:

- learning Python
- practising image manipulation
- understanding reversible transformations
- demonstrating basic encryption concepts

A fixed pixel shift does not provide modern cryptographic security because its transformation is predictable and easy to reverse.

For real-world data protection, established cryptographic algorithms and libraries should be used instead.

---

## Internship Task

**Prodigy InfoTech — Cyber Security Internship**

**Task 02:** Create a simple image-encryption tool using pixel manipulation.

This implementation extends the original task with improved image compatibility, CLI usability, testing, and maintainability.

---

## Built With

- [Python](https://www.python.org/)
- [Pillow](https://python-pillow.org/)

---

<div align="center">

### PRODIGY_CS_02

Pixel manipulation • Python • Image processing • Cyber Security Internship

</div>
