from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
US_STATES = ((None, ''),('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

class User(models.Model):
    first_name = models.CharField(max_length=250, default=None)
    last_name = models.CharField(max_length=250, default=None)
    street = models.CharField(max_length=250, default=None)
    city = models.CharField(max_length=250, default=None)
    state = models.CharField(max_length=2, choices=US_STATES,default=None)
    zip_code  = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(00000)], default=None)
    phone_number = models.IntegerField(validators=[MinValueValidator(0000000000), MaxValueValidator(9999999999)], default=None)


class Item(models.Model):
    item_name = models.CharField(max_length=250, default=None)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=00000.00)
    stock_quantity = models.IntegerField(default=None)
    description = models.TextField(blank=True, default=None)
    photo = models.ImageField(upload_to='images')
