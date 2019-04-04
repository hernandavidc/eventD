from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static

import random

register = template.Library()

@register.simple_tag
def random_bg_event():
    num = random.randint(0,4)
    if num == 0:
        url = static('images/b_event1.jpg')
    elif num == 1:
        url = static('images/b_event2.jpg')
    elif num == 2:
        url = static('images/b_event3.jpg')
    else:
        url = static('images/b_event4.jpg')

    return url