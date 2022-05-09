from rest_framework import viewsets
from .serializers import ProfileSerializer, SiteSerializer, TagsSerializer
from .models import Site,Tags,Profile

class ProfileViewSet (viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class SiteViewSet (viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class TagsViewSet (viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer