from django.db import models
from django.conf import settings
from django.shortcuts import reverse

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_category_url(self):
        return reverse('core:category', kwargs={'slug': self.name})


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    pre_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    image = models.ImageField(blank=True, null=True, default='no-image.png')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:product', kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse('core:add-to-cart', kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    item = models.ManyToManyField(Item)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"


class Order(models.Model):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    order_item = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
