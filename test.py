import uiautomator2 as u2
import time
from dotenv import load_dotenv
import os
from device import Device
import track_file as trk
# Load environment variables from .env file
load_dotenv()

# init instance
d = Device()

def autotest(device):
 
 device.open_app(os.getenv("APP_NAME"))
 device.click_by_text("Text to Video")
 device.click(0.715, 0.231)
 device.write_text("about car , fish and animal",5)
 device.click_by_text("Generate")
 
 trk.get_newest_video_and_pull(device.get_serial())

autotest(d)