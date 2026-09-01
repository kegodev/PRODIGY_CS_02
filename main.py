from __future__ import annotations

import argparse
from pathlib import Path
from typing import Literal

from PIL import Image, UnidentifiedImageError

Operation = Literal["encrypt", "decrypt"]


def normalize_key(key: int) -> int:
    """Normalize any integer key to the valid 8-bit pixel range."""
    return key % 256


def _shift_channel(channel: Image.Image, key: int, operation: Operation) -> Image.Image:
    """Apply a reversible modulo-256 shift to one 8-bit image channel."""
    shift = normalize_key(key)

    if operation == "encrypt":
        return channel.point(lambda value: (value + shift) % 256)

    if operation == "decrypt":
        return channel.point(lambda value: (value - shift) % 256)

    raise ValueError("Operation must be 'encrypt' or 'decrypt'.")


def transform_image(
    input_path: str | Path,
    output_path: str | Path,
    key: int,
    operation: Operation,
) -> Path:
    """
    Encrypt or decrypt an image by shifting its colour-channel values.

    Supported modes are L, LA, RGB, and RGBA. Other image modes are converted
    to RGB or RGBA before processing. Alpha/transparency channels are preserved.
    """
    input_path = Path(input_path)
    output_path = Path(output_path)

    with Image.open(input_path) as source:
        image = source.copy()

    if image.mode not in {"L", "LA", "RGB", "RGBA"}:
        if "A" in image.getbands() or "transparency" in image.info:
            image = image.convert("RGBA")
        else:
            image = image.convert("RGB")

    bands = list(image.split())

    if image.mode == "L":
        transformed = _shift_channel(bands[0], key, operation)
    elif image.mode == "LA":
        luminance = _shift_channel(bands[0], key, operation)
        transformed = Image.merge("LA", (luminance, bands[1]))
    elif image.mode == "RGB":
        transformed = Image.merge(
            "RGB",
            tuple(_shift_channel(channel, key, operation) for channel in bands),
        )
    else:  # RGBA
        rgb = tuple(_shift_channel(channel, key, operation) for channel in bands[:3])
        transformed = Image.merge("RGBA", (*rgb, bands[3]))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    transformed.save(output_path)
    return output_path


def encrypt_image(input_path: str | Path, output_path: str | Path, key: int) -> Path:
    """Encrypt an image using a reversible pixel-value shift."""
    return transform_image(input_path, output_path, key, "encrypt")


def decrypt_image(input_path: str | Path, output_path: str | Path, key: int) -> Path:
    """Decrypt an image that was encrypted with the same key."""
    return transform_image(input_path, output_path, key, "decrypt")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt images using reversible pixel manipulation."
    )
    parser.add_argument(
        "operation",
        choices=("encrypt", "decrypt"),
        help="Operation to perform.",
    )
    parser.add_argument("input", help="Path to the input image.")
    parser.add_argument("output", help="Path for the processed image.")
    parser.add_argument(
        "--key",
        "-k",
        type=int,
        required=True,
        help="Integer shift key. Values are normalized modulo 256.",
    )
    return parser


def run_cli() -> None:
    args = build_parser().parse_args()

    try:
        if args.operation == "encrypt":
            result = encrypt_image(args.input, args.output, args.key)
            print(f"Encryption complete. Saved to: {result}")
        else:
            result = decrypt_image(args.input, args.output, args.key)
            print(f"Decryption complete. Saved to: {result}")
    except FileNotFoundError:
        raise SystemExit(f"Error: input file not found: {args.input}")
    except UnidentifiedImageError:
        raise SystemExit(f"Error: '{args.input}' is not a valid or supported image.")
    except OSError as exc:
        raise SystemExit(f"Error processing image: {exc}")


if __name__ == "__main__":
    run_cli()
