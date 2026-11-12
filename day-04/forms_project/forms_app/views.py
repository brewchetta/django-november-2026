from django.shortcuts import render, redirect # make sure you import redirect!
from .models import Movie, Character
from django.shortcuts import get_object_or_404

def home(request):
    # we can get query parameters this way
    search_term = request.GET.get('search')
    limit = request.GET.get('limit')
    movie_query_set = Movie.objects.all()

    # filter the movies based on the search term
    if search_term:
        movie_query_set = movie_query_set.filter(title__contains=search_term)

    if limit:
        parsed_limit = int(limit)
        movie_query_set = movie_query_set[:parsed_limit]

    # load context and return
    context = { 'movies': movie_query_set }
    return render(request, 'home.html', context)

# MOVIE DETAIL #####################################

def movie_detail(request, title_slug):
    found_movie = get_object_or_404(Movie, title_slug=title_slug)

    context = { 'movie': found_movie }
    return render(request, 'movie_detail.html', context)

# MOVIE CREATE #####################################

from .forms import MovieForm

def movie_create(request):
    # POST -- processes the submitted form
    if request.method == "POST":
        # new instance of the form with data from the POST request
        form = MovieForm(request.POST)
        # check if the form passes validations
        if form.is_valid():
            # save the form's data to the db
            form.save()
            return redirect('home')
        else:
            context = {'form': form}
            return render(request, 'movie_create.html', context)


    # GET -- shows the form
    # create a blank form in context
    context = { 'form': MovieForm() }
    return render(request, 'movie_create.html', context)

# MOVIE EDIT ######################################

def movie_edit(request, title_slug):
    # get the movie or else 404
    movie = get_object_or_404(Movie, title_slug=title_slug)

    # handle post (submitted the form)
    if request.method == "POST":
        # instance=movie ensures we update in the db
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', movie.title_slug)
        else:
            context = { "form": form, "movie": movie }
            return render(request, 'movie_edit.html', context)

    # instance=movie will prefill the form with the current movie's info
    context = { "form": MovieForm(instance=movie), "movie": movie }
    return render(request, 'movie_edit.html', context)


# MOVIE DELETE ###################################

def movie_delete(request, title_slug):
    movie = get_object_or_404(Movie, title_slug=title_slug)

    # on post request (submitted the form)
    if request.method == "POST":
        # delete move and redirect home
        movie.delete()
        return redirect('home')

    # otherwise show the confirm delete page
    context = { 'movie': movie }
    return render(request, 'movie_delete.html', context)


# CHARACTER CREATE ###############################

from .forms import CharacterForm

def character_create(request):
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context = { 'form': CharacterForm() }
            return render(request, 'character_create.html', context)

    context = { 'form': CharacterForm() }
    return render(request, 'character_create.html', context)


# CHARACTER EDIT ################################

def character_edit(request, id):
    character = get_object_or_404(Character, id=id)

    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', character.movie.title_slug)
        else:
            context = { 'form': form }
            return render(request, 'character_edit.html', context)

    context = { 'form': CharacterForm(instance=character) }
    return render(request, 'character_edit.html', context)

# CHARACTER DELETE ###############################

def character_delete(request, id):
    character = get_object_or_404(Character, id=id)

    if request.method == "POST":
        character.delete()
        return redirect('movie_detail', character.movie.title_slug)

    context = { 'character': character }
    return render(request, 'character_delete.html', context)