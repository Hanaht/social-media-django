from django import template


register = template.Library()

@register.filter(name='select_item')
def select_item(item_set, value):
    for item in item_set:
        if item.username == value:
            return True

    return False