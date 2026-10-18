import subprocess
import sys

def install(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package_name}. Error: {e}")


packages = [
  "requests",
  "ollama",
  "dotenv"
]

for package in packages:
  install(package)
