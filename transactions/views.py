from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from utils.format_list_to_obj import format_list_to_obj
from utils.formatData import formatData

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


def upload(request: Request):
    if request.method == "POST":
        uploaded_file = request.FILES["file"]

        file = formatData(uploaded_file)
        obj = format_list_to_obj(file)

        for item in obj:
            serializer = TransactionSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()

    return render(request, "cnab.html")


class TransactionView(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
