from django.shortcuts import render, redirect, get_object_or_404

# View is the most generic class based view
from django.views import View 
from django.views.generic import TemplateView

from datetime import date
from .models import VideoGame, Movie
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


class ModelListView(View):
    model = None
    template_name = None
    model_name = ''

    def get(self, request, *args, **kargs):
        context = { self.model_name: self.model.objects.all() }
        return render(request, self.template_name, context)


# VIDEOGAMES LIST CLASS BASED VIEW #

# view is super generic and essentially uses instance methods for get / post / patch / put / delete
# to do the same general work as a functional view
class VideogameListView(ModelListView):
    model = VideoGame
    template_name = 'videogames_list.html'
    model_name = 'videogames'


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


from django.views.generic import ListView

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'
    context_object_name = 'movies'

# it will also assume you want to name the list of movies `object_list`
# context_object_name will rename it to whatever you'd like in context


from django.views.generic import DetailView

class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movie_detail.html'


# from .forms import MovieForm
# from django.views.generic.edit import FormView

# class MovieCreateView(FormView):
#     template_name = 'movie_form.html'
#     form_class = MovieForm
#     success_url = '/movies'

#     # ensure that the form is saved
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class MovieEditView(FormView):
#     template_name = 'movie_form.html'
#     form_class = MovieForm
#     success_url = '/movies'

#     # extra method that helps to find and load the instance for the form
#     # kwargs == keyword arguments: instance=movie_1
#     def get_form_kwargs(self):
#         kargs = super().get_form_kwargs()
#         kargs['instance'] = get_object_or_404(Movie, pk=self.kwargs['pk'])
#         return kargs

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


from django.views.generic.edit import CreateView, UpdateView, DeleteView

class MovieCreateView(CreateView):
    model = Movie
    fields = '__all__'
    template_name = 'movie_form.html'
    success_url = '/movies'


class MovieEditView(UpdateView):
    model = Movie
    fields = '__all__'
    template_name = 'movie_form.html'
    success_url = '/movies'