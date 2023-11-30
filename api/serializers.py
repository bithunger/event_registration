from rest_framework import serializers
from events.models import Event
from user_dashboard.models import UserEvent
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password




# register serializers
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
        )
    username = serializers.CharField(required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
        )

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'required': True, 'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        user.set_password(validated_data['password'])
        user.save()

        return user
    
    


# event serializers
class EventSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Event
        fields = '__all__'
        
     
        

# User event register Serializer
class UserEventRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEvent
        fields = '__all__'




# User event Serializer
class UserEventSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()
    user_event_details = serializers.SerializerMethodField()
    
    class Meta:
        model = UserEvent
        fields = ('id', 'status', 'user_details', 'user_event_details')
        # depth = 1
        
    def get_user_details(self, obj):
        user = obj.user
        return {
            'id': user.id,
            'firstname': user.username,
            'lastname': user.username,
            'username': user.username,
            'email': user.email,
        }
    
    def get_user_event_details(self, obj):
        event = obj.user_event
        return {
            'id': event.id,
            'title': event.title,
            'description': event.description,
            'slots': event.slots,
        }
        