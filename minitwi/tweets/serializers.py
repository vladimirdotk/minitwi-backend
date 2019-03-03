from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Tweet
        fields = ('id', 'text', 'created', 'owner_id')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    tweets = serializers.HyperlinkedRelatedField(
        many=True, view_name='tweet-detail', read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'password', 'tweets')
