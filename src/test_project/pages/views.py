from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    print(request.user)
    # return HttpResponse("<h1>hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title":"abc  this is about for some me",
        "this_is_true":True,
        "my_number": 1234,
        "my_list":[123,456,312,"Abc"],
        "my_html": "<h1>Hello world</h1>"

    }
    return render(request,"about.html",my_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html",{})
