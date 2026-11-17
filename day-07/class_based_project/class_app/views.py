from django.shortcuts import render, redirect, get_object_or_404

# View is the most generic class based view
from django.views import View 
from django.views.generic import TemplateView

from datetime import date
from .models import VideoGame
from .forms import VideoGameForm


# HOME FUNCTIONAL VIEW #

def home(request):
    context = { 'current_date': date.today() }
    return render(request, 'home.html', context)


# HOME CLASS BASED VIEW #

# template views are just built to serve a template
class HomeView(TemplateView):
    template_name = "home.html"
    extra_context = { 'current_date': date.today() }
    # extra_content is just context


# ABOUT CLASS BASED VIEW #

class AboutView(TemplateView):
    template_name = "about.html"


# VIDEOGAMES LIST FUNCTIONAL VIEW #

def videogames_list(request):
    context = { 'videogames': VideoGame.objects.all() }
    return render(request, 'videogames_list.html', context)

# VIDEOGAMES LIST CLASS BASED VIEW #

# view is super generic and essentially uses instance methods for get / post / patch / put / delete
# to do the same general work as a functional view
class VideogameListView(View):

    def get(self, request, *args, **kargs):
        context = { 'videogames': VideoGame.objects.all() }
        return render(request, 'videogames_list.html', context)


# VIDEOGAMES CREATE CLASS BASED VIEW #
class VideogameCreateView(View):

    # this is what happens on a GET request (go to the page)
    def get(self, request, *args, **kargs):
        context = { 'form': VideoGameForm() }
        return render(request, 'videogame_form.html', context)

    # this is what happens on a POST request (submit the form)
    def post(self, request, *args, **kargs):
        form = VideoGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videogames_list')
        else:
            context = { 'form': form }
            return render(request, 'videogame_form.html', context)


# VIDEOGAMES EDIT CLASS BASED VIEW #
class VideogameEditView(View):

    def get(self, request, id):
        vg = get_object_or_404(VideoGame, id=id)
        context = { 'form': VideoGameForm(instance=vg) }
        return render(request, 'videogame_form.html', context)

    def post(self, request, id):
        vg = get_object_or_404(VideoGame, id=id)
        form = VideoGameForm(request.POST, instance=vg)
        if form.is_valid():
            form.save()
            return redirect('videogames_list')
        else:
            context = { 'form': form }
            return render(request, 'videogame_form.html', context)