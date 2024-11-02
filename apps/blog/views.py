from django.shortcuts import render

def blog_form(request):
    return render(request, "blog/blog_form.html")