import uiautomator2 as u2
import time
import cv2
import numpy as np


class Device:
    _instance = None      # Singleton instance
    _device = None        # Device instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Device, cls).__new__(cls)
        return cls._instance

    def connect_to_device(self):
        try:
            if Device._device is None:  # Chỉ kết nối nếu chưa kết nối
                Device._device = u2.connect()
                print("notify: Connected to device successfully!")
            else:
                print("Device already connected.")
            return Device._device
        except Exception as e:
            print("Error connect to device:", e)
            return None

    @property
    def device(self):
        if Device._device is None:
            self.connect_to_device()
        return Device._device

    def open_app(self, app_name):
        try:
            self.device.app_start(app_name)  # Run app
            time.sleep(5)  # Wait for app to open
            self.device.click(0.5, 0.5)  # Click to close ad if needed
            print("notify: Opened application successfully!")
        except Exception as e:
            print("error open application:", e)
            self.device.press("home")

    def close_app(self, app_name):
        try:
            self.device.app_stop(app_name)  # Stop app
            print("notify: Closed application successfully!")
        except Exception as e:
            print("error close application:", e)
            self.device.press("home")

    def click(self, x, y):
        try:
            time.sleep(4)  
            self.device.click(x, y)
            print("✅ notify: Clicked successfully!")
        except Exception as e:
            print("errro click:", e)
            self.device.press("home")

    def click_by_text(self, text):
        try:
            time.sleep(3)  # Wait for the UI to load
            self.device(text=text).click()

            print("notify: Clicked successfully!")
        except Exception as e:
            print("error click:", e)
            self.device.press("home")

    def back(self):
        try:
            self.device.press("back")
            print("notify: Back pressed successfully!")
        except Exception as e:
            print("error back:", e)
            self.device.press("home")
    def write_text(self, text, action):
     try:
    
            time.sleep(4)
            self.device.send_keys(text)  # Send text to the device
            self.device.send_action(action)
            print("notify: Text written successfully!")
        
     except Exception as e:
        print("error write text:", e)
        self.device.press("home")

