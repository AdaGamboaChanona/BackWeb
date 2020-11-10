from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import DashboardModel
from .serializers import DashboardSerializer
# Create your views here.
class generalDashboard(APIView):
    def get(self,request):
        lista_Usuario = DashboardModel.objects.all()
        serializer = DashboardSerializer(lista_Usuario,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = DashboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class EspecificoDashboard(APIView):
    def get_object(self,pk):
        try:
            return DashboardModel.objects.get(pk=pk)
        except DashboardModel.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        usuario = self.get_object(pk)
        serializer = DashboardSerializer(usuario)
        return Response(serializer.data)
    
    def put(self,request,pk):
        usuario = self.get_object(pk)
        serializer = DashboardSerializer(usuario,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    
    def delete(self,request,pk):
        usuario= self.get_object(pk)
        usuario.delete()
        return Response(status=204)
