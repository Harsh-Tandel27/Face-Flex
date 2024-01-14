import subprocess
import platform

def open_img(file_path):
    system = platform.system().lower()

    if system == "windows":
        subprocess.Popen(["start", " ", file_path], shell=True)
    elif system == "darwin":
        subprocess.Popen(["open", file_path])
    elif system == "linux":
        subprocess.Popen(["xdg-open", file_path])
    else:
        print("Unsupported operating system")

# Example usage:
image_path = "data_img"
open_img(image_path)
