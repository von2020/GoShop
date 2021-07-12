from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete 
import datetime
from django.db.models import Sum
from decimal import Decimal
from django.conf import settings
# from accounts.models import CustomerReg

# CURRENCY = settings.CURRENCY



# Create your models here.

class CategoryStatus(models.Model):
    name = models.CharField(max_length=200, verbose_name='category_staus')

    def __str__(self):
        return self.name





class ProductCategory(models.Model):
    parent            = models.ForeignKey('self', related_name='children', on_delete= models.CASCADE, blank=True, null=True)
    name              = models.CharField(max_length=200, verbose_name='category')
    status            = models.ForeignKey(CategoryStatus, on_delete= models.CASCADE, related_name='category_status', blank=False, null=True)
    
    def __str__(self):
        return self.name




class Availability(models.Model):
    name       = models.CharField(max_length=200, verbose_name='availability')

    def __str__(self):
        return self.name

class Condition(models.Model):
    name       = models.CharField(max_length=200, verbose_name='condition')

    def __str__(self):
        return self.name


class Product(models.Model):
    status            = models.ForeignKey(CategoryStatus, on_delete= models.CASCADE, related_name='product_category_status', blank=False, null=True)
    category          = models.ForeignKey(ProductCategory, on_delete= models.CASCADE, related_name='category', blank=False, null=True)
    availabilty       = models.ForeignKey(Availability, on_delete= models.CASCADE, related_name='availability', blank=False, null=True)
    condition         = models.ForeignKey(Condition, on_delete= models.CASCADE, related_name='condition', blank=True, null=True)
    image             = CloudinaryField(default='assets/images/products/img01.jpg', blank='true', null='true')
    image_one         = CloudinaryField(default='assets/images/products/img01.jpg', blank='true', null='true')
    image_two         = CloudinaryField(default='assets/images/products/img01.jpg', blank='true', null='true')
    image_three       = CloudinaryField(default='assets/images/products/img01.jpg', blank='true', null='true')
    image_four        = CloudinaryField(default='assets/images/products/img01.jpg', blank='true', null='true')
    name              = models.CharField(max_length=200, unique=True)
    slug              = models.SlugField(max_length=200, unique=True)
    price             = models.DecimalField(max_digits=10, decimal_places=2)
    special_price     = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity          = models.IntegerField(default=0, null=True, blank=True)
    created_on        = models.DateTimeField(default=timezone.now)
    description       = models.TextField(blank=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("dashboard:product_detail", Kwargs={
    #         'slug': self.slug
    #         })

    # def get_add_to_cart_url(self):
    #     return reverse("dashboard:add-to-cart", Kwargs={
    #         'slug': self.slug
    #         })

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def imageURL_one(self):
        try:
            url = self.image_one.url
        except:
            url = ''
        return url

    def imageURL_two(self):
        try:
            url = self.image_two.url
        except:
            url = ''
        return url

    def imageURL_three(self):
        try:
            url = self.image_three.url
        except:
            url = ''
        return url

    def imageURL_four(self):
        try:
            url = self.image_four.url
        except:
            url = ''
        return url


# class OrderStatus(models.Model):
#     name = models.CharField(max_length=200, verbose_name='order_status')

#     def __str__(self):
#         return self.name



# AUTH_USER_MODEL = User

# class Orders(models.Model):
#     order_status      = models.ForeignKey(OrderStatus, on_delete= models.CASCADE, related_name='order_status', blank=False, null=True)
#     customer          = models.ForeignKey(CustomerReg, on_delete= models.CASCADE, related_name='customer_order', blank=False, null=True)
#     created_on        = models.DateTimeField(default=timezone.now)
#     phone_number      = models.IntegerField(default=0)
#     complete          = models.BooleanField(default=False, null=True)
    
    # hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    

    # class Meta:
    #     ordering = ['-created_on']

    # def __str__(self):
    #     return str(self.id)

    # def get_add_to_cart_url(self):
    #     return reverse("orders:add-to-cart", kwargs={
    #         'slug': self.slug
    #     })

# class OrderItem(models.Model):
#     product      = models.ForeignKey(Product, on_delete= models.CASCADE, related_name='product', blank=False, null=True)
#     order        = models.ForeignKey(Orders, on_delete= models.CASCADE, related_name='order_item', blank=False, null=True)
#     quantity     = models.IntegerField(default=0, null=True, blank=True)
#     total        = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     date_added   = models.DateTimeField(auto_now_add=True)


# class OrderAddress(models.Model):
#     customer     = models.ForeignKey(CustomerReg, on_delete= models.SET_NULL, related_name='customer_address', blank=False, null=True)
#     order        = models.ForeignKey(Orders, on_delete= models.CASCADE, related_name='order_address', blank=False, null=True)
#     adress       = models.CharField(max_length=200, null=True)
#     city         = models.CharField(max_length=200, null=True)
#     state        = models.CharField(max_length=200, null=True)
#     date   = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.address





class Subscription(models.Model):
    email         = models.CharField(max_length=200, null=True)
    date   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    

class PaymentPlan(models.Model):
    subscription         = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.subscription


class OrderManager(models.Manager):

    def active(self):
        return self.filter(active=True)

class Order(models.Model):
    paymentplan = models.CharField(blank=True, max_length=150, default='')
    date = models.DateField(default=timezone.now())
    title = models.CharField(blank=True, max_length=150)
    firstname = models.CharField(blank=True, max_length=150, default='')
    lastname = models.CharField(blank=True, max_length=150, default='')
    company_name = models.CharField(blank=False, max_length=150, default='')
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,default='')
    address = models.CharField(blank=False, max_length=150, default='')
    product_one = models.CharField(blank=True, max_length=150)
    quantity_one      = models.IntegerField(default=0)
    product_two = models.CharField(blank=True, max_length=150)
    quantity_two      = models.IntegerField(default=0)
    product_three = models.CharField(blank=True, max_length=150)
    quantity_three      = models.IntegerField(default=0)
    product_four = models.CharField(blank=True, max_length=150)
    quantity_four      = models.IntegerField(default=0)
    product_five = models.CharField(blank=True, max_length=150)
    quantity_five      = models.IntegerField(default=0)
    product_six = models.CharField(blank=True, max_length=150)
    quantity_six      = models.IntegerField(default=0)
    product_seven = models.CharField(blank=True, max_length=150)
    total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    telephone = models.IntegerField(default=0)
    timestamp = models.DateField(auto_now_add=True)
    one_month = models.BooleanField(default=False)
    image_one         = models.ImageField(upload_to='orders/', default='assets/images/products/img01.jpg')
    two_months = models.BooleanField(default=False)
    image_two         = models.ImageField(upload_to='orders/', default='assets/images/products/img01.jpg')
    three_months = models.BooleanField(default=False)
    image_three         = models.ImageField(upload_to='orders/', default='assets/images/products/img01.jpg')
    four_months = models.BooleanField(default=False)
    image_four         = models.ImageField(upload_to='orders/', default='assets/images/products/img01.jpg')
    five_months = models.BooleanField(default=False)
    image_five         = models.ImageField(upload_to='orders/', default='assets/images/products/img01.jpg')
    six_months = models.BooleanField(default=False)
    image_six         = models.ImageField(upload_to='orders/', default='assets/images/products/img01.jpg')
    ordered = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    objects = models.Manager()
    browser = OrderManager()



    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs):
        order_items = self.order_items.all()
        self.value = order_items.aggregate(Sum('total_price'))['total_price__sum'] if order_items.exists() else 0.00
        # self.final_value = Decimal(self.value) - Decimal(self.discount)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'New Order'

    def get_edit_url(self):
        return reverse('update_order', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('delete_order', kwargs={'pk': self.id})

    # def tag_final_value(self):
    #     return f'{self.final_value} {CURRENCY}'

    # def tag_discount(self):
    #     return f'{self.discount} {CURRENCY}'

    # def tag_value(self):
    #     return f'{self.value} {CURRENCY}'

    @staticmethod
    def filter_data(request, queryset):
        search_name = request.GET.get('search_name', None)
        date_start = request.GET.get('date_start', None)
        date_end = request.GET.get('date_end', None)
        queryset = queryset.filter(title__contains=search_name) if search_name else queryset
        if date_end and date_start and date_end >= date_start:
            date_start = datetime.datetime.strptime(date_start, '%m/%d/%Y').strftime('%Y-%m-%d')
            date_end = datetime.datetime.strptime(date_end, '%m/%d/%Y').strftime('%Y-%m-%d')
            print(date_start, date_end)
            queryset = queryset.filter(date__range=[date_start, date_end])
        return queryset

        class Meta:
            ordering = ['-date']

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, default="")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items', default="")
    qty = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.title}'

    def save(self,  *args, **kwargs):
        self.final_price = self.discount_price if self.discount_price > 0 else self.price
        self.total_price = Decimal(self.qty) * Decimal(self.final_price)
        super().save(*args, **kwargs)
        self.order.save()

    def tag_final_price(self):
        return f'{self.final_price} {CURRENCY}'

    def tag_discount(self):
        return f'{self.discount_price} {CURRENCY}'

    def tag_price(self):
        return f'{self.price} {CURRENCY}'


@receiver(post_delete, sender=OrderItem)
def delete_order_item(sender, instance, **kwargs):
    product = instance.product
    product.qty += instance.qty
    product.save()
    instance.order.save()