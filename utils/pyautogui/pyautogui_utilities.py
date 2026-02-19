from utils.logs.logger import Logger
import pyautogui
import time


class PyAutoGuiUtilities:
    TIMEOUT = 3
    DEFAULT_INTERVAL = 0.1

    @staticmethod
    def upload_file(file_path: str) -> None:
        Logger.info("Handle File Dialog for uploading file")
        time.sleep(PyAutoGuiUtilities.TIMEOUT)

        Logger.debug(f"Write '{file_path}' to search File Dialog field")
        pyautogui.hotkey('command', 'shift', 'g', interval=PyAutoGuiUtilities.DEFAULT_INTERVAL)
        time.sleep(PyAutoGuiUtilities.TIMEOUT)

        pyautogui.write(file_path)
        time.sleep(PyAutoGuiUtilities.TIMEOUT)

        Logger.debug("Press Enter")
        pyautogui.press("enter")
        time.sleep(PyAutoGuiUtilities.TIMEOUT)

        pyautogui.press('enter')
