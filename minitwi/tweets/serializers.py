from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    owner_id = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Tweet
        fields = ('id', 'text', 'created', 'owner_id')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tweets = serializers.HyperlinkedRelatedField(
        many=True, view_name='tweet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'tweets')
