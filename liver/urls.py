from django.urls import path
from . import views

urlpatterns = [ path('', views.menu, name='menu'),
                path('form/<int:id_form>/', views.form, name='form'),
                path('calculation/<int:id_type>', views.calculate, name='calculate'),
                path('details/', views.details, name='details')]