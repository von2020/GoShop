from django.contrib import admin
from blog.models import Post, Comment, Category
from dashboard.models import Product, ProductCategory, CategoryStatus, Condition, Availability, Order, OrderItem, Subscription, PaymentPlan
from accounts.models import EmploymentStatus, CustomerReg
from contact.models import Message 
from sales.models import SalesReport

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on',)
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug','price','special_price','category', 'condition', 'availabilty')
    list_filter = ("category",)
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

class CustomerRegAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email', 'date_sent',)
    list_filter = ("date_sent",)
    search_fields = ['firstname','lastname','email', 'date_sent']
    # prepopulated_fields = {'slug': ('email',)}

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'message','date_sent',)
    list_filter = ("date_sent",)
    search_fields = ['name','email', 'message', 'date_sent']



class SalesReportAdmin(admin.ModelAdmin):
    list_display = ('product','amount', 'date')
    list_filter = ("date",)
    search_fields = ['date','product', 'amount']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(CategoryStatus)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(CustomerReg, CustomerRegAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(PaymentPlan)
admin.site.register(SalesReport, SalesReportAdmin)
admin.site.register(Condition)
admin.site.register(Availability)
admin.site.register(Subscription)


