from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('month/<int:year>/<int:month>/', views.month_view, name='month_view'),
    path('add_task/', views.add_task, name='add_task'),
    path('tasks/', include('tasks.urls')),
     path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
