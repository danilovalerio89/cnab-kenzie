from django.shortcuts import render
from utils.format_list_to_obj import format_list_to_obj
from utils.formatData import formatData

from transactions.serializers import TransactionSerializer


def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES["file"]

        file = formatData(uploaded_file)
        obj = format_list_to_obj(file)

        for item in obj:
            serializer = TransactionSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()

    return render(request, "cnab.html")
