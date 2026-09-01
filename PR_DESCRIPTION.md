# Pull Request Title

Improve image mode support, performance, and CLI usability

# Pull Request Description

## Summary

This PR improves the pixel-manipulation image encryption tool while keeping the original reversible modulo-256 approach.

## Changes

- Replaced slow per-pixel `getpixel()` / `putpixel()` loops with Pillow channel transformations.
- Added support for grayscale (`L`), grayscale with alpha (`LA`), RGB, and RGBA images.
- Preserved alpha/transparency channels during encryption and decryption.
- Added automatic conversion for unsupported image modes.
- Added a command-line interface with configurable input/output paths.
- Normalized numeric keys with modulo `256`.
- Added clearer handling for missing, invalid, or unsupported image files.
- Added automated tests for RGB round trips, RGBA transparency, grayscale support, and key normalization.
- Added `requirements.txt` and `.gitignore`.
- Updated the README with installation, usage, testing instructions, a feature overview, and a security limitation notice.

## Why this change is useful

The previous implementation assumed every image pixel contained exactly three RGB values and processed images one pixel at a time. This could fail for images with transparency or grayscale data and becomes inefficient for larger images.

The updated implementation is more robust, easier to use from the command line, easier to maintain, and easier to verify through tests.

## Testing

Run:

```bash
pip install -r requirements.txt
python -m unittest discover -v
```

All included tests should pass.

## Security note

The algorithm remains an educational pixel-shift transformation and is not intended to provide real cryptographic security.
