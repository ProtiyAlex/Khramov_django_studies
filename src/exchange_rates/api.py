import json

from django.http import JsonResponse

from .services import AlphavantageResponse, Convert


def get_convert(request):
    convert = Convert(json.loads(request.body)["from"], json.loads(request.body)["to"])

    return JsonResponse(AlphavantageResponse(**convert.start()).results.dict())
