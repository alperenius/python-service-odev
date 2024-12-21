import os
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# Log dizininin varlığını doğrula
os.makedirs(LOG_DIR, exist_ok=True)

# Log dosyasına yazma fonksiyonu
def log_event(event_type, file_path):
    log_entry = {
        "event_type": event_type,
        "file_path": file_path,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(LOG_FILE, "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")
# Log dosyasının kaydedileceği dizin
LOG_DIR = "/home/ubuntu/bsm/logs"
LOG_FILE = f"{LOG_DIR}/file_changes.log"

class Watcher:
    DIRECTORY_TO_WATCH = "/home/ubuntu/bsm/test"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def log_event(event_type, file_path):
        """Log değişikliklerini JSON formatında kaydeder."""
        log_entry = {
            "event_type": event_type,
            "file_path": file_path,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(LOG_FILE, "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")

    def on_modified(self, event):
        if not event.is_directory:
            self.log_event("modified", event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self.log_event("created", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.log_event("deleted", event.src_path)

if __name__ == "__main__":
    # Log dizininin varlığını doğrula
    import os
    os.makedirs(LOG_DIR, exist_ok=True)

    # İzlemeyi başlat
    watcher = Watcher()
    watcher.run()

