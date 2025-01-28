import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, script_name):
        self.script_name = script_name
        self.process = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.terminate()
        self.process = os.popen(f"python {self.script_name}")

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"{event.src_path} changed. Restarting script...")
            self.start_process()

if __name__ == "__main__":
    script_to_watch = "main.py"  # Replace with your script
    handler = ChangeHandler(script_to_watch)
    observer = Observer()
    observer.schedule(handler, ".", recursive=False)
    observer.start()
    print(f"Watching for changes in {script_to_watch}...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()