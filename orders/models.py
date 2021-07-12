from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from dashboard.models import Product


# Create your models here.

