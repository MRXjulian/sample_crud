from rest_framework import serializers
from .models import Project

class projectseralizers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'n_identification', 'stock', 'namep')

