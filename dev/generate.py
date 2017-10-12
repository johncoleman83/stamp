#!/usr/bin/python3
"""
generates DB from Getty API
https://api.gettyimages.com/swagger/ui/index#!/OAuth/ResourceOwner_Post
"""
import json
import requests
"""
import models
User = models.User
Place = models.Place
storage = models.storage
"""


def save_to_json_file(my_obj, filename):
    """saves JSON to file"""
    with open(filename, mode='w', encoding='utf-8') as f_io:
        f_io.write(json.dumps(my_obj))

def make_request():
    """ request to api """

    url = ("https://api.gettyimages.com/v3/search/images?exclude_nudity=true&f"
           "ields=allowed_use%2Casset_family%2Ccall_for_image%2Ccollection_id%"
           "2Ccollection_name%2Cid%2Creferral_destinations%2Cthumb%2Ctitle&lic"
           "ense_models=royaltyfree&phrase=religion&sort_order=most_popular")
    headers = {
        "Accept": "application/json",
        "Api-Key": "j6ycu2phdbt7r6jyfxv72mhe",
        "Authorization":
        ("Bearer QbqVGdhjHv7vkbauc8sU0Y/JUsAeD9Rh2xMfmKadfHzK4ameCKakaOiLTlydJ"
         "BiVScJ7d1zbIjiKVWFSvguKhjJ7DSi9YCV8iKX00pMSJIAzlV6nzOXbpG+F7vlpg+Jqv"
         "rFu/1uXYx79wOT05xc6GBRVpGOWS5PIMNofeKPHhKc=|77u/YWxtbUwyNEFKbHB5N0tS"
         "TDVHbGQKMzAyMTQKCjRTYkJEQT09CjZTM0JEQT09CjAKajZ5Y3UycGhkYnQ3cjZqeWZ4"
         "djcybWhlCjE2Mi4yMTcuNzUuMTM3CjAKMzAyMTQKCjMwMjE0CjAKCgo=|3|2|1")
        }
    r = requests.get(url, headers=headers)
    r_data = r.json()
    images = r_data.get("images")
    save_to_json_file(images, './images_json/religion.json')


if __name__ == "__main__":
    """
    MAIN App
    """
    make_request()
