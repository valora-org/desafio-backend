from rest_framework import serializers 
from user_auth.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Player
        fields = ["id","password","email","picture"]
        extra_kwargs = {
            'picture': {'required':False},
            'password': {'write_only':True}
        }
    
    def create(self,validated):
        username = validated.get('email')
        instance = Player.objects.create_user(**validated,username=username)


        return instance
    
    def validate(self,attrs):
        valid = super().validate(attrs)

        return valid