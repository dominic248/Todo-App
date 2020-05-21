from rest_framework import viewsets
from .serializers import *
from ..models import Todo
from rest_framework.response import Response
from rest_framework import views,status, exceptions
from django.db.models import Q

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todo.objects.all()
    lookup_field='id'

    def get_queryset(self, *args, **kwargs):
        queryset = super(TodoViewSet, self).get_queryset(*args, **kwargs)
        qs=Todo.objects.filter(user=self.request.user)
        query=self.request.GET.get('s')
        if query is not None:
            qs=qs.filter(
                Q(todo__icontains=query)
            ).distinct()
        return qs

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"detail": "Auth not provided."}, status=400)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # print(instance.user.id,request.user.pk)
        if not request.user.is_authenticated:
            return Response({"detail": "Auth not provided."}, status=400)
        elif int(instance.user.id)!=int(request.user.pk):
            return Response({"detail": "Not found."}, status=400)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_authenticated:
            return Response({"detail": "Auth not provided."}, status=400)
        elif int(instance.user.id)!=int(request.user.pk):
            return Response({"detail": "Not found."}, status=400)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT) 

    def retrieve(self, request, *args, **kwargs): 
        instance = self.get_object()
        if not request.user.is_authenticated:
            return Response({"detail": "Auth not provided."}, status=400)
        elif int(instance.user.id)!=int(request.user.pk):
            return Response({"detail": "Not found."}, status=400)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
