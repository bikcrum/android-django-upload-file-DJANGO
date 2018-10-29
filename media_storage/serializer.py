from rest_framework import serializers
from .models import Recording

class RecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        # fields = ('name','path')
        fields = '__all__'
