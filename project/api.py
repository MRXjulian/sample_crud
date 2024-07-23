from .models import Project
from rest_framework import viewsets, permissions
from .serializer import projectseralizers

class Projectviewset (viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = projectseralizers