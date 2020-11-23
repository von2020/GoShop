from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post, Category, Like
from urllib.parse import quote_plus
from hitcount.views import HitCountDetailView
from accounts.models import CustomerReg


app_name = 'blog'

# Create your views here.
def postList(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    cats = Category.objects.all()
    user_count = CustomerReg.objects.count()
    user = request.user
    return render(request, 'blog/blog.html',{'post_list': post_list, 'cats': cats, 'user': user, 'user_count': user_count,})



# def post_detail(request, slug):
#     cats = Category.objects.all()
#     post = get_object_or_404(Post, slug=slug)
#     post_image = quote_plus(post.image.url)
#     post_title = quote_plus(post.title)
#     context = {
#         "title": post.title,
#         "post": post,
#         "post_image": post_image,
#         "post_title": post_title,
#         "cats": cats,
#     }
#     return render(request, "blog/post_detail.html", context)

class PostDetail(HitCountDetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug = 'slug'
    count_hit = True
    
        
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
        'cats' : Category.objects.all(),
        'user_count' : CustomerReg.objects.count(),
        
        })
        return context


def category(request, category):
    category = Post.objects.filter(category_id=category)
    cats = Category.objects.all()
    return render(request, 'blog/category.html',{'category': category, 'cats': cats})



    

# def count(request):
