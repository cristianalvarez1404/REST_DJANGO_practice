from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import Advocate
from .serializers import AdvocateSerializer
from django.db.models import Q

# GET /advocates
# POST /advocates
# GET /advocates/:id
# PUT /advocates/:id
# PATCH /advocates/:id
# DELETE /advocates/:id

@api_view(["GET","POST"])
def endpoints(request):
  data = ['/advocates','advocates/:username']
  return Response(data)

@api_view(["GET","POST"])
def advocate_list(request):
  #Handles GET requests
  if request.method == "GET":
    query = request.GET.get('query')
    
    if query == None:
      query = ''

    # advocates = Advocate.objects.all()
    # advocates = Advocate.objects.filter(username__icontains=query)
    # advocates = Advocate.objects.filter(username__icontains=query,bio__icontains=query)
    advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
    serializer = AdvocateSerializer(advocates,many=True)
    return Response(serializer.data)
  
  if request.method == "POST":
    advocate = Advocate.objects.create(
      username = request.data["username"],
      bio= request.data["bio"]
    )
    serializer = AdvocateSerializer(advocate,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def add_advocate(request):
  advocate = Advocate.objects.create(
    username = request.data["username"],
    bio = request.data["bio"]
  )
  return Response('added')

@api_view(["GET","PUT","DELETE"])
def advocate_detail(request,username):
  advocate = Advocate.objects.get(username=username)
  
  if request.method == "GET":
    serializer = AdvocateSerializer(advocate,many=False)
    return Response(serializer.data)
  
  if request.method == "PUT":
    advocate.username = request.data["username"]
    advocate.bio = request.data["bio"]
    advocate.save()

    serializer = AdvocateSerializer(advocate,many=False)
    return Response(serializer.data)

  if request.method == "DELETE":
    advocate.delete()
    return Response({"message":"deleted"})