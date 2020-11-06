from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import DashboardModel
from .serializers import DashboardSerializer
# Create your views here.
class ListDashboard(APIView):
    def get(self,request):
        dash = DashboardModel.objects.all()
        dash_json = DashboardSerializer(dash,many=True)
        return Response(dash_json.data)
    
    def post(self,request):
        dash_json = DashboardSerializer(data=request.data)
        if dash_json.is_valid():
            dash_json.save()
            return Response(dash_json.data, status=201)
        return Response(dash_json.errors, status=400)

class DetailDashboard(APIView):
    def get_object(self,pk):
        try:
            return DashboardModel.objects.get(pk=pk)
        except DashboardModel.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        dash = self.get_object(pk)
        dash_json = DashboardSerializer(dash)
        return Response(dash_json.data)
    
    def put(self,request,pk):
        dash = self.get_object(pk)
        dash_json = DashboardSerializer(dash,data=request.data)
        if dash_json.is_valid():
            dash_json.save()
            return Response(dash_json.data)
        return Response(dash_json.errors,status=400)
    
    def delete(self,request,pk):
        dash= self.get_object(pk)
        dash.delete()
        return Response(status=204)
