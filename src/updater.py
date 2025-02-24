# import requests
# import os
# import zipfile
# import shutil

# # GITHUB_REPO = "yourusername/yourrepo"
# # LATEST_RELEASE_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"


# GITHUB_REPO = "Gangaram9816/Flet_app"
# LATEST_RELEASE_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"

# DOWNLOAD_URL = f"https://github.com/{GITHUB_REPO}/releases/latest/download/MyFletApp-windows.zip"
# INSTALL_DIR = os.path.join(os.getcwd(), "update")

# def download_latest_version():
#     print("Checking for updates...")
#     response = requests.get(LATEST_RELEASE_URL).json()
#     latest_version = response["tag_name"]

#     with open("version.txt", "r") as f:
#         current_version = f.read().strip()

#     if latest_version > current_version:
#         print(f"New version {latest_version} found! Downloading...")
#         zip_path = os.path.join(INSTALL_DIR, "update.zip")
#         os.makedirs(INSTALL_DIR, exist_ok=True)

#         with open(zip_path, "wb") as f:
#             f.write(requests.get(DOWNLOAD_URL).content)

#         with zipfile.ZipFile(zip_path, "r") as zip_ref:
#             zip_ref.extractall(INSTALL_DIR)

#         shutil.move(INSTALL_DIR, os.getcwd())
#         print("Update complete!")
#         return True
#     else:
#         print("You're up to date.")
#         return False

# if __name__ == "__main__":
#     download_latest_version()



import requests
import os
import zipfile
import shutil

GITHUB_REPO = "Gangaram9816/MyFletApp"
LATEST_RELEASE_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
DOWNLOAD_URL = f"https://github.com/{GITHUB_REPO}/releases/latest/download/Flet_App-windows.zip"
INSTALL_DIR = os.path.join(os.getcwd(), "update")

def download_latest_version():
    print("Checking for updates...")
    response = requests.get(LATEST_RELEASE_URL).json()
    latest_version = response["tag_name"]

    with open("version.txt", "r") as f:
        current_version = f.read().strip()

    if latest_version > current_version:
        print(f"New version {latest_version} found! Downloading...")
        zip_path = os.path.join(INSTALL_DIR, "update.zip")
        os.makedirs(INSTALL_DIR, exist_ok=True)

        with open(zip_path, "wb") as f:
            f.write(requests.get(DOWNLOAD_URL).content)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(INSTALL_DIR)

        shutil.move(INSTALL_DIR, os.getcwd())
        print("Update complete!")
        return True
    else:
        print("You're up to date.")
        return False

if __name__ == "__main__":
    download_latest_version()
