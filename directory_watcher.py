import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Değişiklikleri takip edecek dizin ve log dosyası
WATCH_DIRECTORY = "/home/ubuntu/bsm/test"
LOG_FILE = "/home/ubuntu/bsm/logs/changes.json"

# Olayları işlemek için bir sınıf
class WatcherHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.log_event("modified", event)

    def on_created(self, event):
        self.log_event("created", event)

    def on_deleted(self, event):
        self.log_event("deleted", event)

    def log_event(self, event_type, event):
        log_data = {
            "event_type": event_type,
            "path": event.src_path,
            "is_directory": event.is_directory,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        # JSON formatında log dosyasına yazma
        with open(LOG_FILE, "a") as log_file:
            log_file.write(json.dumps(log_data) + "\n")
        print(f"Logged: {log_data}")  # Konsola bilgi yazdırma

# Ana fonksiyon
def main():
    # Observer nesnesi oluşturma
    observer = Observer()
    event_handler = WatcherHandler()
    observer.schedule(event_handler, WATCH_DIRECTORY, recursive=True)

    try:
        print(f"İzleme başlatıldı: {WATCH_DIRECTORY}")
        observer.start()  # İzleme başlat
        while True:
            time.sleep(1)  # Programı sürekli açık tut
    except KeyboardInterrupt:
        print("İzleme durduruluyor...")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
