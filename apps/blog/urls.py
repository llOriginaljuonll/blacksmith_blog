from django.urls import path
from .views import blog_form

app_name = "blog"

urlpatterns = [
    path('blog_form/', blog_form, name="blog-form"),
]
