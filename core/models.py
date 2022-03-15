from django.conf import settings
from django.db import models
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    # ("DB_Value", "Displayed_Text")
    ("S", "Shirt"),
    ("SW", "Sport wear"),
    ("SO", "Outwear"),
)

LABEL_CHOICES = (
    # ("DB_Value", "Displayed_Text")
    ("P", "primary"),
    ("S", "secondary"),
    ("D", "danger"),
)

class Item(models.Model):
    '''
    All Items
    '''
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

class OrderItem(models.Model):
    '''
    Link between Items and Orders
    '''
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Order(models.Model):
    '''
    All Orders and Cart Items
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username