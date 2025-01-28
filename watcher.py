import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartHandler(FileSystemEventHandler):
    def __init__(self, script_name):
        self.script_name = script_name
        self.process = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.terminate()
            self.process.wait()  # Ensure the process terminates fully before restarting
        print(f"Starting {self.script_name}...")
        self.process = subprocess.Popen(["python", self.script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"{event.src_path} modified. Restarting script...")
            self.start_process()

if __name__ == "__main__":
    script_to_watch = "main.py"  # Replace with your script
    event_handler = RestartHandler(script_to_watch)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()
    print(f"Watching for changes in {script_to_watch}...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()