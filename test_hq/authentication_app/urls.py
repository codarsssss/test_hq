from django.urls import path, include

app_name = 'courses_app'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
