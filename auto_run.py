import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'File changed: {event.src_path}')
        if event.src_path.endswith('.py'):
            try:
                print('Running main.py...')
                subprocess.run(['python', 'main.py'], check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error occurred while running script: {e}')

if __name__ == "__main__":
    path = '.'  # the path to be monitored, use '.' for current directory
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()