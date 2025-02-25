# import flet as ft
# import requests

# VERSION = "1.0.0"  # Current version of the app
# # GITHUB_REPO = "yourusername/yourrepo"
# # LATEST_RELEASE_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"

# GITHUB_REPO = "Gangaram9816/Flet_app"
# LATEST_RELEASE_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"


# def check_for_updates():
#     try:
#         response = requests.get(LATEST_RELEASE_URL).json()
#         latest_version = response["tag_name"]
#         return latest_version
#     except:
#         return VERSION  # If there's an error, assume no updates

# def main(page: ft.Page):
#     latest_version = check_for_updates()
#     if latest_version > VERSION:
#         page.add(ft.Text(f"New version {latest_version} available! Please update.", color="red"))
#     else:
#         page.add(ft.Text("You're up to date!", color="green"))

# ft.app(target=main)




import flet as ft
import requests
import os
VERSION = "1.0.0"
GITHUB_REPO = "Gangaram9816/MyFletApp"
LATEST_RELEASE_URL = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"

# https://github.com/Gangaram9816/MyFletApp.git

def check_for_updates():
    try:
        response = requests.get(LATEST_RELEASE_URL)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()

        # Ensure "tag_name" exists in the response
        latest_version = data.get("tag_name", "Unknown")
        if latest_version == "Unknown":
            return "No releases found. Please check manually."

        if latest_version > VERSION:
            return f"New version {latest_version} available! Download: https://github.com/{GITHUB_REPO}/releases/latest"
        else:
            return "You're up to date!"
    except requests.exceptions.RequestException as e:
        return f"Error checking updates: {str(e)}"

def main(page: ft.Page):
    update_message = check_for_updates()
    page.add(ft.Text(update_message, color="red" if "New version" in update_message else "green"))


if __name__ == "__main__":
    if "CI" in os.environ:  # ✅ Skip UI in CI/CD mode
        print("✅ Running in CI/CD mode, exiting immediately.")
        exit(0)  # ✅ Prevent blocking execution
    else:
        ft.app(target=main)


# if os.getenv("CI"):  
#     print("✅ Running in CI/CD, skipping Flet UI launch.")
# else:
#     ft.app(target=main)

# if __name__ == "__main__":
#     ft.app(target=main)

# ft.app(target=main)
