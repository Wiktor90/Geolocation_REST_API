from django.shortcuts import render
from .models import Geodata
from .serializers import GeodataSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json

key = 'a1147aae52811d3d1207a8eb63d775e2'


def get_ip_geodata(ip, key):
    url = f'http://api.ipstack.com/{ip}?access_key={key}'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers)
    payload = json.loads(response.text)
    return payload


@api_view(['GET'])
def api_set_up(request):
    api_urls = {
        'List': '/geodata-list/',
        'Detail-View': 'geodata-details/',
        'Create': 'geodata-create/',
        'Update': 'geodata-update/',
        'Delete': 'geodata-delete/',
    }

    return Response(api_urls)


@api_view(['GET'])
def geo_list(requet):
    geodata = Geodata.objects.all().order_by('id')
    serializer = GeodataSerializer(geodata, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def geo_details(reqest, pk):
    geodata = Geodata.objects.get(id=pk)
    serializer = GeodataSerializer(geodata, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def geo_create(request):
    if request.method == 'POST':
        data = request.data
        geodata = get_ip_geodata(data['ip'], key)

        geo_dict = {
            "ip": geodata['ip'],
            "continent_name": geodata['continent_name'],
            "country_code": geodata['country_code'],
            "city": geodata['city'],
            "latitude": geodata['latitude'],
            "longitude": geodata['longitude']
        }

        serializer = GeodataSerializer(data=geo_dict)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


@api_view(['PUT'])
def geo_update(request, pk):
    geodata = Geodata.objects.get(id=pk)
    serializer = GeodataSerializer(instance=geodata, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def geo_delete(reqest, pk):
    geodata = Geodata.objects.get(id=pk)
    geodata.delete()
    return Response('Resource deleted successfully.')
