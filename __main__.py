
import subprocess
import os
import sys

app_path = os.path.join(os.path.dirname(__file__), "source", "app.py")

def run():
    subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])

if __name__ == "__main__":
    run()
