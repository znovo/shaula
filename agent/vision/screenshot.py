from pathlib import Path
import pyautogui


class Screenshot:
    def __init__(self):
        self.resolution = (720, 480)

        self.current_dir = Path(__file__).parent
        self.data_dir = self.current_dir.parent / "data"

        self.data_dir.mkdir(parents=True, exist_ok=True)

    def capture(self, filename="screenshot.png"):
        save_path = self.data_dir / filename
        screenshot = pyautogui.screenshot()
        screenshot = screenshot.resize(self.resolution) 
        screenshot = screenshot.save(save_path)

        print(f"Screenshot salva em: {save_path}")

        return save_path