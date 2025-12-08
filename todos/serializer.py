from rest_framework import serializers
from django.utils import timezone
from .models import Task,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Task
        fields = ['id','name','description','status','category','due_date','updated_at','user']

        def validate_due_date(self,value):
            if value < timezone.now():
                raise serializers.ValidationError({'Due_date': 'Hozirgi vaqtdan keyinni tanlang'})
            
            return value

class FilterTaskSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    status = serializers.CharField(required=False)
    create_at = serializers.DateField(required=False)  