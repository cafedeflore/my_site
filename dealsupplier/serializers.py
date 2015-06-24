# coding=utf-8
__author__ = 'cafedeflore'

from rest_framework import serializers
from models import DealTask

class DealTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealTask
        field = ('env', 'condition', 'proposer', 'system', 'details', 'comment', 'add_time', 'end_time', 'is_solved', 'is_valid')