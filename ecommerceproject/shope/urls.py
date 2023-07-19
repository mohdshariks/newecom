from django.urls import path
from . import views
app_name='shope'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    path('', views.demo, name="demo"),
]

