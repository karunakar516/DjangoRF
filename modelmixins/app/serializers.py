from rest_framework.serializers import ModelSerializer
from .models import Employee
class EmployeeSeializer(ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"