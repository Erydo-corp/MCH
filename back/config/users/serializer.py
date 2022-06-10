from rest_framework import serializers
from models import Users


class UserVolontereeSerualizer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    education = serializers.CharField()
    phone = serializers.CharField()
    description = serializers.CharField()
    photo = serializers.ImageField()

    class Meta:
        model = Users



