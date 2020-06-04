from django.db import models
from djgeojson.fields import PointField

# Create your models here.
class Record(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    host_id = models.IntegerField(blank=True, null=True)
    host_name = models.TextField(blank=True, null=True)
    neighbourhood_group = models.TextField(blank=True, null=True)
    neighbourhood = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    longitude = models.TextField(blank=True, null=True)  # This field type is a guess.
    room_type = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)  # This field type is a guess.
    minimum_nights = models.IntegerField(blank=True, null=True)
    number_of_reviews = models.IntegerField(blank=True, null=True)
    last_review = models.DateField(blank=True, null=True)
    reviews_per_month = models.IntegerField(blank=True, null=True)
    calculated_host_listings_count = models.IntegerField(blank=True, null=True)
    availability_365 = models.IntegerField(blank=True, null=True)
    django_id = models.AutoField(primary_key=True)
    geom = PointField()

    # this string is used to represent the objects in the admin tab
    def __str__(self):
        return str(self.django_id)+"_"+str(self.name)

    # class Meta:
    #     managed = False
    #     db_table = 'AB_NYC_2019'