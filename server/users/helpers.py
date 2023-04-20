import hashlib

ALLOWED_IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'gif', 'jpe', 'png', 'webp']


def ImageHashPath(instance, filename):
    hash_obj = hashlib.sha256(instance.username.encode())
    hash_obj.update(filename.encode())

    hash_hex = hash_obj.hexdigest()

    return 'profile_pics/{0}'.format(hash_hex) + '.' + filename.split('.')[-1]
