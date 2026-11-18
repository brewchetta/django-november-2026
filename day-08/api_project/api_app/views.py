from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OceanTide
from .serializers import OceanTideSerializer


# WELCOME #
@api_view(["GET"])
def welcome(request):
    return Response({"message": "Welcome!"}, status=status.HTTP_200_OK)


# GET ALL / POST NEW #
@api_view(["GET", "POST"])
def ocean_tide_list(request):

    # GET ALL
    if request.method == "GET":
        tides = OceanTide.objects.all()
        # for multiple items you need many=True
        serializer = OceanTideSerializer(tides, many=True)
        # serializer.data will turn the data into a dictionary/list
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST NEW
    if request.method == "POST":
        serializer = OceanTideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({ "errors": serializer.errors }, status=status.HTTP_400_BAD_REQUEST)


# GET ONE #
@api_view(["GET"])
def ocean_tide_detail(request, id):
    try:
        tide = OceanTide.objects.get(id=id)
    except OceanTide.DoesNotExist:
        return Response({ 'error': '404: Does not exist' }, status=status.HTTP_404_NOT_FOUND)

    serializer = OceanTideSerializer(tide)
    return Response(serializer.data, status=status.HTTP_200_OK)