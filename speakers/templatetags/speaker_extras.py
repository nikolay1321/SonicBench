from django import template

from speakers.models import Speaker

register = template.Library()

@register.filter
def rms_power(value):
    return f"{value} W RMS"

@register.simple_tag
def total_speakers():
    return Speaker.objects.count()