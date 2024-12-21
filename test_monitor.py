import os
import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FILE = "/home/ubuntu/bsm/logs/changes.json"
MONITORED_DIR = "/home/ubuntu/bsm/test"

# Ensure log directory exists
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

class DirectoryChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
 print(f"Event detected: {event}")  # Bu satırı ekleyin
    event_data =
        event_data = {
            "event_type": event.event_type,
            "src_path": event.src_path,
            "is_directory": event.is_directory,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.log_event(event_data)

    @staticmethod
    def log_event(event_data):
        try:
            with open(LOG_FILE, "a") as log_file:
                log_file.write(json.dumps(event_data) + "\\n")
        except Exception as e:
            print(f"Error logging event: {e}")

def main():
    event_handler = DirectoryChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=MONITORED_DIR, recursive=True)

    try:
        observer.start()
        print(f"Monitoring directory: {MONITORED_DIR}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    except Exception as e:
        print(f"Error: {e}")
    observer.join()

if __name__ == "__main__":
    main()
