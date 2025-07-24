import subprocess
import sys

def upgrade_requirements(file="requirements.txt"):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "-r", file])

if __name__ == "__main__":
    upgrade_requirements()



import subprocess
import sys
import json

# Try import importlib.metadata (Python 3.8+)
try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    # For older Python, fallback to backport package
    from importlib_metadata import version, PackageNotFoundError

def get_latest_pip_version():
    url = "https://pypi.org/pypi/pip/json"
    import urllib.request
    with urllib.request.urlopen(url) as response:
        data = json.load(response)
        return data['info']['version']

def get_current_pip_version():
    try:
        return version("pip")
    except PackageNotFoundError:
        return None

def upgrade_pip():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

if __name__ == "__main__":
    latest_version = get_latest_pip_version()
    print(f"Latest pip version available: {latest_version}")

    current_version = get_current_pip_version()
    print(f"Current pip version installed: {current_version}")

    if current_version != latest_version:
        print("Upgrading pip...")
        upgrade_pip()
        print("Pip upgrade complete.")
    else:
        print("You already have the latest pip version.")
