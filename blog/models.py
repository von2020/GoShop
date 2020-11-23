from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomerReg
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='category')

    def __str__(self):
        return self.name




STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    category          = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='category', blank=False, null=True)
    image             = models.ImageField(upload_to='blog/')
    title             = models.CharField(max_length=200, unique=True)
    slug              = models.SlugField(max_length=200, unique=True)
    author            = models.ForeignKey(CustomerReg, on_delete= models.CASCADE,related_name='author')
    content           = models.TextField(blank=True)
    created_on        = models.DateTimeField(auto_now_add=True)
    status            = models.IntegerField(choices=STATUS, default=0)
    # liked             = models.ManyToManyField(CustomerReg, default=None, blank=True, related_name='Liked')
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',related_query_name='hit_count_generic_relation')



    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user  = models.ForeignKey(CustomerReg, on_delete=models.CASCADE)
    post  = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)


class Comment(models.Model):
    post       = models.ForeignKey(Post, related_name="comments",on_delete=models.CASCADE, blank=False)
    name       = models.CharField(max_length=200, unique=True)
    body       = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)









