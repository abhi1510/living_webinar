import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, attribute, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(attribute)
    qs = instance.__class__.objects.filter(slug=slug)
    if qs.exists():
        new_slug = '{}-{}'.format(slug, random_string_generator(size=4))
        return unique_slug_generator(instance, attribute, new_slug)
    return slug
