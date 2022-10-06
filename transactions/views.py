import ipdb
from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from stores.models import Store
from stores.serializers import StoreSerializer
from utils.format_list_to_obj import format_list_to_obj
from utils.formatData import formatData

from transactions.models import Transaction


def upload(request: Request):
    if request.method == "POST":
        uploaded_file = request.FILES["file"]

        file = formatData(uploaded_file)
        obj = format_list_to_obj(file)

        for item in obj:
            store_obj = {
                "store_name": item["store_name"],
                "store_owner": item["store_owner"],
                "cpf": item["cpf"],
            }
            transaction_obj = {
                "type": item["type"],
                "value": item["value"],
                "date": item["date"],
                "card": item["card"],
                "hour": item["hour"],
            }

            store, _ = Store.objects.get_or_create(**store_obj)

            transaction = Transaction(**transaction_obj, store=store)
            transaction.save()

    return render(request, "cnab.html")
