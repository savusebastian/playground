from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    url_picture = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    active = models.BooleanField()
    # id_restaurant = models.ForeignKey(
    #     'Restaurant',
    #     on_delete=models.CASCADE,
    # )
    # id_bar = models.ForeignKey(
    #     'Bar',
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    url_picture = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    id_category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    # id_bar = models.ForeignKey(
    #     'Bar',
    #     on_delete=models.CASCADE,
    # )
    active = models.BooleanField()

    def __str__(self):
        return self.name


# class Currency(models.Model):
#     name = models.CharField(max_length=50)


class Table(models.Model):
    code = models.CharField(max_length=50)
    total = models.PositiveSmallIntegerField()
    active = models.BooleanField()


class Restaurant(models.Model):
    id_product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    id_table = models.ForeignKey(
        'Table',
        on_delete=models.CASCADE,
    )
    id_basket = models.ForeignKey(
        'Basket',
        on_delete=models.CASCADE,
    )


class Bar(models.Model):
    id_product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    id_table = models.ForeignKey(
        'Table',
        on_delete=models.CASCADE,
    )
    id_basket = models.ForeignKey(
        'Basket',
        on_delete=models.CASCADE,
    )


class Basket(models.Model):
    id_product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
    )
    active = models.BooleanField()
    obs = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=50)
    url_picture = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    id_category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    id_subcategory = models.ForeignKey(
        'Subcategory',
        on_delete=models.CASCADE,
    )
    active = models.BooleanField()
    destination = models.BooleanField()
    price = models.PositiveSmallIntegerField()
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.name
