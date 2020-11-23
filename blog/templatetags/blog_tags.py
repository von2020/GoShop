from django import template
from blog.models import Post


register = template.Library()

@register.simple_tag
def get_recent_posts(num=8):
    return Post.objects.all().order_by('-created_on')[:num]



