from django import template

register = template.Library()

@register.filter
def addstr(arg1, arg2):
    """
        concatenate arg1 & arg2
    """
    return str(arg1) + str(arg2)

@register.filter
def replaceSpace(arg1):
    return arg1.replace(" ", "+")