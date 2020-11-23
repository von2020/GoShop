from django.contrib import admin
from blog.models import Post, Comment, Category
from dashboard.models import Product, ProductCategory
from accounts.models import EmploymentStatus, CustomerReg
from contact.models import ContactUs

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on',)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug','price','category',)
    list_filter = ("category",)
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

class CustomerRegAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email', 'date_sent',)
    list_filter = ("date_sent",)
    search_fields = ['firstname','lastname','email', 'date_sent']
    # prepopulated_fields = {'slug': ('email',)}

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'message','date_sent',)
    list_filter = ("date_sent",)
    search_fields = ['name','email', 'message', 'date_sent']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(CustomerReg, CustomerRegAdmin)
admin.site.register(ContactUs, ContactUsAdmin)


