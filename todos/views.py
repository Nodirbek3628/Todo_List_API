from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .serializer import CategorySerializer, TaskSerializer, FilterTaskSerializer
from .models import Task, Category


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
            filter_serializer = FilterTaskSerializer(
                data=self.request.query_params
            )

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

