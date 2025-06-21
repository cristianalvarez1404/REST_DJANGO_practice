from rest_framework import serializers
from .models import Advocate

class AvocateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Advocate
    fields = "__all__"