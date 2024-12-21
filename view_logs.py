import json

JSON_FILE = "/home/ubuntu/bsm/logs/changes.json"

def read_logs():
    try:
        with open(JSON_FILE, "r") as f:
            logs = json.load(f)
            for log in logs:
                print(f"{log['timestamp']} - {log['event_type']} - {log['path']}")
    except FileNotFoundError:
        print("Log dosyası bulunamadı!")
    except json.JSONDecodeError:
        print("Log dosyası bozuk veya boş!")

if __name__ == "__main__":
    read_logs()
