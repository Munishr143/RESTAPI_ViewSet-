from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class ProductCrudVS(ViewSet):
    def list(self, request):
        PQS=Product.objects.all()
        PSD=ProductMS(PQS, many=True)
        return Response(PSD.data)

    def retrieve(self, request, pk):
        SPO=Product.objects.filter(P_Id=pk)
        if SPO:
            SPD=ProductMS(SPO[0])
            return Response(SPD.data)
        else:
            return Response({'failure':'The Product is not there'})
    
    def create(self, request):
        SD=ProductMS(data=request.data)
        if SD.is_valid():
            SD.save()
            return Response({'success':'The Product is Created'})
        else:
            return Response({'failure':'The Product is Not Created'})
        
    def update(self, request, pk):
        SPO=Product.objects.get(P_Id=pk)
        SPD=ProductMS(SPO, data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'success':'The Product is Updated'})
        else:
            return Response({'failure':'The Product is Not Updated'})
        
    def partial_update(self, request, pk):
        SPO=Product.objects.get(P_Id=pk)
        SPD=ProductMS(SPO, data=request.data, partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'success':'The Product is Updated'})
        else:
            return Response({'failure':'The Product is Not Updated'})
        
    def destroy(self, request, pk):
        Product.objects.get(P_Id=pk).delete()
        return Response({'success':'The Product is Deleted'})
