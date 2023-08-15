# Windows Extra Module For MIO-KITCHEN
import os


def win2wslpath(path):
    if not ":" in path:
        path = os.path.abspath(path)
    f, e = path.split(":")
    return "".join([f"/mnt/{f.lower()}", e.replace("\\", "/")])


def wsl2winpath(path):
    if path[:4] != "/mnt" or len(path) < 5:
        return "\\wsl.localhost\\Ubuntu\\" + path.replace("/", "\\")
    else:
        f, e = path[5:].split("/", 1)
        return "".join([f.upper(), ":", e.replace("/", "\\")])