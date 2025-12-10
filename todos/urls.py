from django.urls import path
from .views import CategoryViewSets,TaskViewSets,RegisterView


urlpatterns = [
    path('auth/register/',RegisterView.as_view()),
    path('todos/',TaskViewSets.as_view({'get':'list','post':'create'})),
    path('todos/<int:pk>/',TaskViewSets.as_view({'get':'retrieve','delete':'destroy','put':'update'})),
    path('category/',CategoryViewSets.as_view({'get':'list','post':'create'}))
]
