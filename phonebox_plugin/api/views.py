from rest_framework.routers import APIRootView
from .. import filters
from ..models import Number, VoiceCircuit
from . import serializers
from django.conf import settings
from packaging import version


from netbox.api.viewsets import NetBoxModelViewSet as ModelViewSet


class PhoneBoxPluginRootView(APIRootView):
    """
    phonebox_plugin API root view
    """
    def get_view_name(self):
        return 'PhoneBox'


class NumberViewSet(ModelViewSet):
    queryset = Number.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.NumberSerializer
    filterset_class = filters.NumberFilterSet

class VoiceCircuitsViewSet(ModelViewSet):
    queryset = VoiceCircuit.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.VoiceCircuitSerializer
    filterset_class = filters.VoiceCircuitFilterSet
