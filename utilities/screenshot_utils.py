import os
from datetime import datetime

class ScreenshotUtils:
    @staticmethod
    def capture_screenshot(driver,test_name):
        folder="screenshots"
        os.makedirs(folder,exist_ok=True)
        timestamp=datetime.now().strftime("%Y%m%d-%H%M%S")
        file_name=f"{test_name}_{timestamp}.png"
        file_path=os.path.join(folder,file_name)
        driver.save_screenshot(file_path)
        return file_path