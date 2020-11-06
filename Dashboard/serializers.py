from rest_framework import serializers
from .models import DashboardModel

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardModel
        fields =('__all__')