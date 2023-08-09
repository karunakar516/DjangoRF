from .models import Cricketer
from rest_framework.serializers import ModelSerializer
class CricketerSerializer(ModelSerializer):
    class Meta:
        model=Cricketer
        fields="__all__"