import uiautomator2 as u2
import time
from dotenv import load_dotenv
import os
from device import Device
# Load environment variables from .env file
load_dotenv()

#connect to device
d = Device()

# open app
 
d.open_app(os.getenv("APP_NAME"))
d.click_by_text("Text to Video")
d.click(0.334, 0.211)
d.write_text("video about pepole vietname and in here, have car , restaurant", "Generate")
d.click_by_text("Generate")
d.click(0, 0.1)
d.click_by_text("Generate")