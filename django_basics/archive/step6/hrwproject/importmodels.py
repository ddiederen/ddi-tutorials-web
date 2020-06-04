# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AbNyc2019(models.Model):
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

    class Meta:
        managed = False
        db_table = 'AB_NYC_2019'
