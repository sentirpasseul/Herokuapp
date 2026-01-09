from utils.logs.logger import Logger
import pyautogui
import time


class PyAutoGuiUtilities:
    TIMEOUT = 2

    def upload_file(self, file_path: str) -> None:
        Logger.info("Handle File Dialog for uploading file")
        time.sleep(self.TIMEOUT)

        Logger.debug(f"Write '{file_path}' to search File Dialog field")
        pyautogui.hotkey('command', 'shift', 'g')
        time.sleep(self.TIMEOUT)

        pyautogui.write(file_path)
        time.sleep(self.TIMEOUT)

        Logger.debug("Press Enter")
        pyautogui.press("enter")
        time.sleep(self.TIMEOUT)

        pyautogui.press('enter')
