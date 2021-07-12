from django.db import models
from django.contrib.auth.models import User
from dashboard.models import Order
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class EmploymentStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name='emp_name')
    short_name = models.CharField(max_length=20, verbose_name='emp_short_name')
    # created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_name

class CustomerRegManager(BaseUserManager):
    def create_user(self, email, firstname,lastname, phone_number, work_address, salary,date_sent, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            phone_number=phone_number,
            work_address=work_address,
            salary=salary,
            date_sent=date_sent
            )
        

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, lastname, work_address, salary, phone_number, date_sent, password=None):
        user = self.create_user(email, firstname=firstname, lastname=lastname, work_address=work_address, salary=salary, phone_number=phone_number, date_sent=date_sent,  password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

AUTH_USER_MODEL = User

class CustomerReg(AbstractBaseUser):
    email             = models.EmailField(verbose_name='email address',max_length=255,unique=True,default='')
    firstname         = models.CharField(max_length=200,default='')
    lastname          = models.CharField(max_length=200,default='')
    employment_status = models.BooleanField(default=False, null=True)
    phone_number      = models.IntegerField(default=0)
    work_address      = models.CharField(max_length=200,default='')
    salary            = models.IntegerField(default=0)
    date_sent         = models.DateTimeField(auto_now_add=True)
    bank_statement    = models.FileField(upload_to='documents/%Y/%m/%d', default='')
    government_id     = models.FileField(upload_to='documents/%Y/%m/%d', default='')
    work_id           = models.FileField(upload_to='documents/%Y/%m/%d',default='')
    order             = models.ForeignKey(Order, on_delete= models.CASCADE, related_name='order', blank=True, null=True)
    is_active         = models.BooleanField(default=True)
    is_admin          = models.BooleanField(default=False)
    
    objects = CustomerRegManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'phone_number', 'work_address', 'salary','date_sent']

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None): 
        return True

    def has_module_perms(self, app_label): 
        return True

    @property
    def is_staff(self):
        return self.is_admin










