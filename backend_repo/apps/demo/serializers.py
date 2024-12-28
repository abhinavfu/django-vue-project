# TODO There's certainly more than one way to do this task, so take your pick.
from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','text','timestamp','user']
        # fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','text','timestamp','post','user']



