# imports
from rest_framework import serializers
from hrwapp1.models import Record

# serializer
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            'django_id',
            'id',
            'name',
            'host_id',
            'host_name',
            'neighbourhood_group',
            'neighbourhood',
            'latitude',
            'longitude',
            'room_type',
            'price',
            'minimum_nights',
            'number_of_reviews',
            'last_review',
            'reviews_per_month',
            'calculated_host_listings_count',
            'availability_365',
            'geom',
        ]
