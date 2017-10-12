#!/usr/bin/python3
"""
generates DB from Getty API
"""
import json
import models
User = models.User
Image = models.Image
storage = models.storage


def load_from_json_file(filename):
    """creates json object from file"""
    with open(filename, mode='r', encoding='utf-8') as f_io:
        my_dict = json.loads(f_io.read())
        f_io.close()
    return my_dict


def store_to_db():
    """ stores JSON to db """
    files = [
        './images_json/lizards.json',
        './images_json/dogs.json',
        './images_json/nature.json',
        './images_json/stained_glass.json',
        './images_json/faces.json',
        './images_json/business.json',
        './images_json/goats.json',
        './images_json/religion.json'
    ]
    num = 1
    for filename in files:
        json = load_from_json_file(filename)
        last_name = filename.split('/')[2].split('.')[0]
        u_kwargs = {
            'email': '{}@notreal.com'.format(num),
            'password': 'testpass',
            'first_name': 'not_real_{}'.format(num),
            'last_name': '{} lover'.format(last_name)
        }
        new_u = User(**u_kwargs)
        new_u.save()
        for i in json:
            i_kwargs = {
                "url": i.get('display_sizes')[0].get('uri'),
                "title": i.get('title'),
                "family": i.get('asset_family'),
                "collection": i.get('collection_name')
            }
            new_i = Image(**i_kwargs)
            new_i.save()
            new_i.users.append(new_u)
            new_u.images.append(new_i)
            new_i.save()
            new_u.save()
        num += 1


if __name__ == "__main__":
    """
    MAIN App
    """
    store_to_db()
    storage.save()
