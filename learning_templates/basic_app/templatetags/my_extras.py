from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

@register.filter(name='vidya')
def vidya(value,arg):
    return value.join("priya")


# while registering arg1)what u call it in templatetag arg2)name of the function
# register.filter('cut',cut)
