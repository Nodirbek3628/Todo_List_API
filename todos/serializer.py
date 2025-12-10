from rest_framework import serializers
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Task,Category,CustomUser

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(max_length=128)
    class Meta:
        model = CustomUser
        fields = ['username','password','confirm','email','first_name','last_name',]

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError('password cofirmga  bilan mos emas')
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('confirm')
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()

        return user



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