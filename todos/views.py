from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework import status
from .serializer import CategorySerializer, TaskSerializer, FilterTaskSerializer,RegisterSerializer,UserSerializer
from .models import Task, Category


class RegisterView(APIView):

    def post(self,request:Request)->Response:
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user_json = UserSerializer(user).data

            return Response(user_json,status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSets(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TaskViewSets(ModelViewSet): 
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    filter_backends = [SearchFilter]
    search_fields = ['name', 'status']   
    def get_queryset(self):
        queryset = Task.objects.all()

        if self.action == 'list':
            filter_serializer = FilterTaskSerializer(data=self.request.query_params)

            if filter_serializer.is_valid(raise_exception=True):
                name = filter_serializer.data.get('name')
                status = filter_serializer.data.get('status')
                create_at = filter_serializer.data.get('create_at')  

                if name:
                    queryset = queryset.filter(name__icontains=name)

                if status:
                    queryset = queryset.filter(status=status)

                if create_at:
                    queryset = queryset.filter(create_at__date=create_at)

        return queryset

