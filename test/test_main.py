import tempfile
import unittest
from pathlib import Path

from PIL import Image

from main import decrypt_image, encrypt_image, normalize_key


class ImageEncryptionTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def _save_image(self, mode, size, data, name):
        path = self.root / name
        image = Image.new(mode, size)
        image.putdata(data)
        image.save(path)
        return path

    def test_rgb_round_trip_restores_original_pixels(self):
        source = self._save_image(
            "RGB",
            (2, 2),
            [(0, 10, 20), (100, 150, 200), (255, 0, 128), (25, 50, 75)],
            "rgb.png",
        )
        encrypted = self.root / "rgb_encrypted.png"
        decrypted = self.root / "rgb_decrypted.png"

        encrypt_image(source, encrypted, 42)
        decrypt_image(encrypted, decrypted, 42)

        with Image.open(source) as original, Image.open(decrypted) as restored:
            self.assertEqual(list(original.getdata()), list(restored.getdata()))

    def test_rgba_alpha_channel_is_preserved(self):
        source = self._save_image(
            "RGBA",
            (2, 1),
            [(10, 20, 30, 0), (100, 150, 200, 127)],
            "rgba.png",
        )
        encrypted = self.root / "rgba_encrypted.png"

        encrypt_image(source, encrypted, 20)

        with Image.open(source) as original, Image.open(encrypted) as result:
            original_alpha = [pixel[3] for pixel in original.getdata()]
            encrypted_alpha = [pixel[3] for pixel in result.getdata()]
            self.assertEqual(original_alpha, encrypted_alpha)

    def test_grayscale_round_trip(self):
        source = self._save_image("L", (3, 1), [0, 128, 255], "gray.png")
        encrypted = self.root / "gray_encrypted.png"
        decrypted = self.root / "gray_decrypted.png"

        encrypt_image(source, encrypted, 99)
        decrypt_image(encrypted, decrypted, 99)

        with Image.open(source) as original, Image.open(decrypted) as restored:
            self.assertEqual(list(original.getdata()), list(restored.getdata()))

    def test_key_normalization(self):
        self.assertEqual(normalize_key(300), 44)
        self.assertEqual(normalize_key(-1), 255)


if __name__ == "__main__":
    unittest.main()
