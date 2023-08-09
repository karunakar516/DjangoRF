from rest_framework.serializers import ModelSerializer
from .models import Intern
class InternSerializer(ModelSerializer):
    class Meta:
        model=Intern
        fields="__all__"
'''
We can just Use HyperLinkedModelSerializer to replace ids with their hyperlinks
'''