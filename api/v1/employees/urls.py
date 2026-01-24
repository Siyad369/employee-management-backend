from django.urls import path
from api.v1.employees import views

urlpatterns = [
    path('employees/', views.EmployeeListAPIView.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetailAPIView.as_view()),
]