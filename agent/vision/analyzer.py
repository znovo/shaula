import base64
from pathlib import Path

class VisionAnalyzer:
    def __init__(self):
        self.current_dir = Path(__file__).parent
        self.image_file = self.current_dir.parent / "data" / "screenshot.png"

        self.image_file.parent.mkdir(parents=True, exist_ok=True)
    def convert_image_to_base64(self):

        with open(self.image_path, "rb") as self.image_file:
            encoded_string = base64.b64encode(self.image_file.read()).decode("utf-8")
        return encoded_string
        