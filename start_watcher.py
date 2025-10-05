# start_watcher.py

import time
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- Configuration ---
# The folder we will be watching for new transcript files.
# IMPORTANT: Make sure this folder exists!
WATCH_FOLDER = os.path.expanduser("~/Downloads/LimitlessTranscripts")

class TranscriptHandler(FileSystemEventHandler):
    """
    This class defines what happens when a file event occurs.
    """
    def on_created(self, event):
        # This method is called when a new file is created.
        if not event.is_directory and event.src_path.endswith('.txt'):
            print(f"📄 New transcript detected: {os.path.basename(event.src_path)}")
            print("🚀 Launching analysis script...")
            
            # Use subprocess to call our existing process_meeting.py script.
            # We pass the path of the new file to the script.
            # Note: We use 'python' which should resolve to the one in our venv.
            subprocess.run(["python", "process_meeting.py", event.src_path])
            print("\n✅ Analysis complete. Watching for next file...")

def start_watcher():
    """
    Sets up and starts the directory watcher.
    """
    print("--- Aura Watcher Service ---")
    
    # Create the watch folder if it doesn't exist
    if not os.path.exists(WATCH_FOLDER):
        print(f"⚠️ Watch folder not found. Creating folder at: {WATCH_FOLDER}")
        os.makedirs(WATCH_FOLDER)
    
    print(f"👀 Watching for new .txt files in: {WATCH_FOLDER}")
    
    event_handler = TranscriptHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)
    
    observer.start()
    print("✅ Watcher started successfully. Press Ctrl+C to stop.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 Watcher stopped.")
    observer.join()

if __name__ == "__main__":
    start_watcher()
