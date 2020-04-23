from rest_framework import serializers

from .models import Work, DownTime, ObjectDownTime, TypeDownTime


class DownTimeSerializer(serializers.ModelSerializer):
    """Простои оборудования за период времени"""

    # type_downtime = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = DownTime
        fields = "__all__"


class TypeDownTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDownTime
        fields = "__all__"


class ObjectDownTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ObjectDownTime
        fields = ("name",)


# class ObjectDownTimeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ObjectDownTime
#         fields = "__all__"


class WorkSerializer(serializers.ModelSerializer):
    """ Комментарии к производимым каждый день работам"""

    # obj = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # obj = ObjectDownTimeSerializer()

    type = TypeDownTimeSerializer(read_only=True, many=True)
    obj = ObjectDownTimeSerializer()

    class Meta:
        model = Work
        fields = "__all__"

# class WorkDownTimeDetailSerializer(serializers.ModelSerializer):
#     """Комментарии к работе производимым для определенного объекта"""
#
#     obj = serializers.SlugRelatedField(slug_field="name", read_only=True)
#
#     class Meta:
#         model = WorkDownTime
#         fields = ("date", "obj", "comment_one", "comment_two",)
