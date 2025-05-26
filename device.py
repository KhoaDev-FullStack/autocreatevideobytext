import os
import time
import uiautomator2 as u2
import logging
import subprocess

# Cấu hình logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Device:
    _instance = None
    _device = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Device, cls).__new__(cls)
        return cls._instance

    def connect_to_device(self):
        if Device._device is None:
            try:
                Device._device = u2.connect()
                logging.info("Connected to device successfully.")
            except Exception as e:
                logging.error(f"Failed to connect to device: {e}")
        else:
            logging.info("Device already connected.")
        return Device._device

    @property
    def device(self):
        if Device._device is None:
            self.connect_to_device()
        return Device._device

    @staticmethod
    def get_connected_serial():
        try:
            result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
            lines = result.stdout.strip().splitlines()

            for line in lines[1:]:
                if line.strip() and "device" in line:
                    serial = line.split()[0]
                    return serial
            return None
        except Exception as e:
            logging.error(f"Error getting device serial: {e}")
            return None

    def get_serial(self):
        return self.get_connected_serial()
    

    
    def open_app(self, app_name, timeout=10):
     
        try:
            self.device.app_start(app_name)
            self._wait_for_app_launch(app_name, timeout)
            logging.info(f"Application '{app_name}' opened successfully.")
        except Exception as e:
            logging.error(f"Error opening app '{app_name}': {e}")
            self.device.press("home")

    def close_app(self, app_name):
       
        try:
            self.device.app_stop(app_name)
            logging.info(f"Application '{app_name}' closed successfully.")
        except Exception as e:
            logging.error(f"Error closing app '{app_name}': {e}")
            self.device.press("home")

    def click(self, x, y, delay=5):
  
        try:
            time.sleep(delay)
            self.device.click(x, y)
            logging.info(f"Clicked at ({x}, {y}).")
        except Exception as e:
            logging.error(f"Error clicking at ({x}, {y}): {e}")
            self.device.press("home")

    def click_by_text(self, text, timeout=10):
        
        try:
            element = self._wait_for_element(text=text, timeout=timeout)
            if element:
                element.click()
                logging.info(f"Clicked on element with text '{text}'.")
            else:
                logging.warning(f"Element with text '{text}' not found.")
        except Exception as e:
            logging.error(f"Error clicking by text '{text}': {e}")
            self.device.press("home")

    def back(self):
     
        try:
            self.device.press("back")
            logging.info("Back button pressed.")
        except Exception as e:
            logging.error(f"Error pressing back: {e}")
            self.device.press("home")

    def write_text(self, input_text, delay=3):
        
        try:
            time.sleep(delay)
            self.device.send_keys(input_text)
            logging.info(f"Input text '{input_text}'.")
        except Exception as e:
            logging.error(f"Error writing text '{input_text}': {e}")
            self.device.press("home")

    def _wait_for_app_launch(self, app_name, timeout):
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.device.app_current()['package'] == app_name:
                return True
            time.sleep(0.5)
        logging.warning(f"Timeout waiting for app '{app_name}' to launch.")
        return False

    def _wait_for_element(self, text=None, resource_id=None, timeout=10):
       
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                if text:
                    element = self.device(text=text)
                elif resource_id:
                    element = self.device(resourceId=resource_id)
                else:
                    logging.warning("No identifier provided for element wait.")
                    return None
                if element.exists:
                    return element
            except Exception:
                pass
            time.sleep(0.5)
        return None

    def take_screenshot(self, filename='screenshot.png'):
        """Capture and save a screenshot."""
        try:
            self.device.screenshot(filename)
            logging.info(f"Screenshot saved to {filename}.")
        except Exception as e:
            logging.error(f"Error taking screenshot: {e}")

    def swipe(self, start_x, start_y, end_x, end_y, duration=800):
        """Perform swipe gesture."""
        try:
            self.device.swipe(start_x, start_y, end_x, end_y, duration)
            logging.info(f"Swiped from ({start_x}, {start_y}) to ({end_x}, {end_y}).")
        except Exception as e:
            logging.error(f"Error performing swipe: {e}")

