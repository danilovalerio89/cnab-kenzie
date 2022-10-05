import ipdb
from django.core.files.uploadedfile import InMemoryUploadedFile


def formatData(data: InMemoryUploadedFile):
    format_data = data.read().decode()

    data_list = format_data.split("\n")
    if data_list[-1] == "":
        data_list.pop()
        return data_list

    return data_list
