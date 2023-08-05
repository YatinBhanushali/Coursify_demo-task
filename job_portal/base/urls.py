from django.urls import path
from .views import home, emp, CustomLogin

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('', home, name='home'),
    path('emp/', emp, name='emp'),

]