from rest_framework import serializers

from .models import WorkDownTime, DownTime


class WorkDownTimeSerializer(serializers.ModelSerializer):
    """ Комментарии к производимым каждый день работам"""
    obj = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = WorkDownTime
        fields = ("date", "obj", "comment_one", "comment_two",)


class WorkDownTimeDetailSerializer(serializers.ModelSerializer):
    """Комментарии к работе производимым для определенного объекта"""

    obj = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = WorkDownTime
        fields = ("date", "obj", "comment_one", "comment_two",)


class DownTimeSerializer(serializers.ModelSerializer):
    """Простои оборудования за период времени"""
    type_downtime = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = DownTime
        fields = ("date", "type_downtime", "amount", "smena",)