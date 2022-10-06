import ipdb
from rest_framework import serializers
from rest_framework.views import Request, Response, status

from stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"
        read_only_fields = ["id"]

    def create(self, validated_data: list) -> Response:

        ...
