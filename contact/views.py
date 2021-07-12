from django.shortcuts import render, redirect
from  dashboard.models import ProductCategory
from blog.views import postList
from blog.models import Post, Like
from contact.models import Message
from accounts.forms import MessageForm


# Create your views here.
def emailsent(request):
    return render(request, 'dashboard/emailsent.html')

def contact(request):
    cats = ProductCategory.objects.all()
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/contact/contact-us')
    else:
        return render(request, 'dashboard/contact.html', {'cats': cats, 'form': form})

# def like_post(request):
#     user = request.user
#     if request.method == 'POST':
#         post_id = request.POST.get("post_id")
#         post_obj = Post.objects.get(id=post_id)

#         if user in post_obj.liked.all():
#             post_obj.liked.remove(user)
#         else:
#             post_obj.liked.add(user)

#         like, created = Like.objects.get_or_create( post_id=post_id)
        
#         if not created:
#             if like.value == 'Like':
#                 like.value == 'Unlike'
#             else:
#                 like.value == 'Like'
#                 like.save()

#     return redirect("/blog/all-posts")
