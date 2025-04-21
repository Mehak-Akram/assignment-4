import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter GitHub username: ")
url = f"https://github.com/{github_user}"

r = requests.get(url)

if r.status_code == 200:
    soup = bs(r.content, "html.parser")

    profile_image_tag = soup.find("img", class_="avatar-user")

    if profile_image_tag:
        profile_image = profile_image_tag.get("src")
        print("Profile image URL:", profile_image)
    else:
        print("Profile image not found.")
else:
    print(f"Failed to fetch profile page. Status code: {r.status_code}")

