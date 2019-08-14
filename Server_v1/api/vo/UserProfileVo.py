# coding:utf-8

from rest_framework import serializers
from manager.model.UserProfileModel import UserProfileModel
from django.contrib.auth.models import User


class UserVo(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_login', 'first_name', 'last_name')


class UserProfileVo(serializers.ModelSerializer):
    user = UserVo()

    class Meta:
        model = UserProfileModel
        fields = ('nick', 'ding_talk_account', 'user')
        depth = 1
