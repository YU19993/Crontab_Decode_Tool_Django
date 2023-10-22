from rest_framework import serializers

class CronExpressionSerializer(serializers.Serializer):
    expression = serializers.CharField(max_length=100)
