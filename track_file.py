import os
import subprocess
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("video_pull.log"),
        logging.StreamHandler()
    ]
)

def get_newest_video_and_pull(device_id=None, phone_folder='/storage/emulated/0/DCIM', local_folder=r'D:\Video'):
    # Ensure local folder exists
    os.makedirs(local_folder, exist_ok=True)

    try:
        start_time = time.time()
        duration = 5 * 60  # 5 minutes

        while time.time() - start_time < duration:
            device_str = f"{device_id}" if device_id is not None else "emulator-0"
            logging.info(f"Checking device: {device_str}")

            # List the newest mp4 file
            cmd_ls = f'adb -s {device_str} shell ls -t {phone_folder}/*.mp4'
            logging.debug(f"Executing command: {cmd_ls}")
            result = subprocess.run(cmd_ls, shell=True, capture_output=True, text=True)

            if result.returncode != 0:
                logging.error(f"Error executing adb ls: {result.stderr.strip()}")
                time.sleep(30)
                continue

            if not result.stdout.strip():
                logging.warning("No mp4 files found or directory is empty.")
                time.sleep(30)
                continue

            newest_file = result.stdout.strip().split('\n')[0]
            logging.info(f"Newest video file: {newest_file}")

            # Pull the file to local machine
            cmd_pull = f'adb -s {device_str} pull "{newest_file}" "{local_folder}"'
            logging.debug(f"Executing command: {cmd_pull}")
            pull_result = subprocess.run(cmd_pull, shell=True, capture_output=True, text=True)

            if pull_result.returncode == 0:
                logging.info(f"File successfully downloaded to: {local_folder}")
              
            else:
                logging.error(f"Error pulling file: {pull_result.stderr.strip()}")

            time.sleep(30)

    except Exception as e:
        logging.exception(f"An exception occurred: {e}")

