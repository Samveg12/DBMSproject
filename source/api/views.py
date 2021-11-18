from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from source.models import Emails
from country.models import countries,disaster,Helpline,finaltable,History

from source.api.serializers import counriesSerializer,finalSerializer

@api_view(['GET'])

def api_detail(request,slug):
    try:
        apii=countries.objects.get(name=slug)
    except countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        serializer=counriesSerializer(apii)
        return Response(serializer.data)
@api_view(['GET'])

def dis_detail(request,slug):
    try:
        apii=finaltable.objects.filter(city=slug)

    except finaltable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        print(apii)
        for i in range(0,len(apii)):
            serializer=finalSerializer(apii[0])
            return Response(serializer.data)

@api_view(['PUT'])

def update_api(request,slug):
    try:
        apii=countries.objects.get(name=slug)
    except countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=="PUT"): 
        serializer=counriesSerializer(apii,data=request.data)
        data={}
        if(serializer.is_valid()):
            serializer.save()
            data["success"]="update successfull"
            return(Response(data=data))
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])

def delete_api(request,slug):
    try:
        apii=countries.objects.get(name=slug)
    except countries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=="DELETE"): 
        serializer=apii.delete()
        data={}
        if serializer:
            data['success']="delete successful"
        else:
            data['failure']="delete failed"
        return(Response(data=data ))
        
@api_view(['POST'])

def create_api(request):
    s= countries()
    if(request.method=="POST"):
        serializer=counriesSerializer(s,data=request.data)
        data={}
        if(serializer.is_valid()):
            serializer.save()
            return(Response(serializer.data,status=status.HTTP_201_CREATED))
        return(Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST))


