import sys
import os
import asyncio
import aiohttp

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.append(project_root)

from src.configurations.conf import Config


async def user_service(session, url, user_id):
    user_service_url = f"{url}/users/{user_id}"
    print(user_service_url)

    async with session.get(user_service_url) as response:
        if response.status == 200:
            user_data = await response.json()
            return {
                "id": user_data["id"],
                "name": user_data["name"],
                "email": user_data["email"]
            }
        else:
            print(f"Failed to fetch user data. Status: {response.status}")
            return None


async def post_service(session, url, user_id):
    post_service_url = f"{url}/posts/{user_id}"
    print(post_service_url)

    async with session.get(post_service_url) as response:
        if response.status == 200:
            post_data = await response.json()
            return {
                "id": post_data["id"],
                "title": post_data["title"],
                "body": post_data["body"]
            }
        else:
            print(f"Failed to fetch post data. Status: {response.status}")
            return None


async def album_service(session, url, album_id):
    album_service_url = f"{url}/albums/{album_id}"
    print(album_service_url)

    async with session.get(album_service_url) as response:
        if response.status == 200:
            album_data = await response.json()
            return {
                "userId": album_data["userId"],
                "id": album_data["id"],
                "title": album_data["title"]
            }
        else:
            print(f"Failed to fetch album data. Status: {response.status}")
            return None


async def photos_service(session, url, photo_id):
    photos_service_url = f"{url}/photos/{photo_id}"
    print(photos_service_url)

    async with session.get(photos_service_url) as response:
        if response.status == 200:
            photos_data = await response.json()
            return {
                "albumId": photos_data["albumId"],
                "id": photos_data["id"],
                "title": photos_data["title"],
                "url": photos_data["url"],
                "thumbnailUrl": photos_data["thumbnailUrl"]
            }
        else:
            print(f"Failed to fetch photos data. Status: {response.status}")
            return None


async def dashboard(url):
    async with aiohttp.ClientSession() as session:
        user_data, post_data, album_data, photos_data = await asyncio.gather(
            user_service(session, url, 1),
            post_service(session, url, 1),
            album_service(session, url, 1),
            photos_service(session, url, 1)
        )

        dashboard_data = {
            "user": user_data,
            "post": post_data,
            "album": album_data,
            "photos": photos_data
        }

        return dashboard_data


if __name__ == "__main__":
    config = Config()
    print("Base URL:", config.url)

    try:
        result = asyncio.run(dashboard(config.url))
        print("\nDashboard Result:")
        print(result)

    except aiohttp.ClientError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"Error occurred: {e}")