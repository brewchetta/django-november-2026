from django.shortcuts import render

# views is basically your controller actions

def home(request):
    # home.html is the actual template we will show the user
    return render(request, "home.html")

def about(request):
    # about.html is the actual template we will show the user
    return render(request, "about.html")

# all html lives in a special `templates` folder we need to create