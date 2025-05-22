class FileChangeHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.last_modified_time = None

    def check_for_changes(self):
        import os
        import time

        current_modified_time = os.path.getmtime(self.file_path)
        if self.last_modified_time is None:
            self.last_modified_time = current_modified_time
            return False

        if current_modified_time != self.last_modified_time:
            self.last_modified_time = current_modified_time
            return True

        return False