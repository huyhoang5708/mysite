from . import views
from django.urls import path
from . import models
urlpatterns = [
    path("", views.posts, name="posts"),
    path('<slug:product_slug>', views.product_detail),

]