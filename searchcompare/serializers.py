# coding=utf-8
__author__ = 'cafedeflore'

from rest_framework import serializers
from models import CommentRecord

class CommentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentRecord
        field = ('keyword', 'choice', 'comments')