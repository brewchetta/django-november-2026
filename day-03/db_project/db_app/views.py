from django.shortcuts import render
# always need to import the model before we use it
from .models import WordDefinition

def index(request):
    # get all WordDefinition items from db
    all_words = WordDefinition.objects.all()
    # add them to context
    context = { "all_words": all_words }
    return render(request, 'index.html', context)


# detail using try/except ################################################

from django.http import Http404

def word_detail_old(request, id):
    try:
        found_word = WordDefinition.objects.get(id=id) # this will DoesNotExist error if it doesn't exist
        context = { 'found_word': found_word }
        return render(request, 'word_detail.html', context)

    except WordDefinition.DoesNotExist: # this will only trigger with a DoesNotExist
        raise Http404("That definition was not found")


# detail using get_object_or_404 ##########################################

from django.shortcuts import get_object_or_404

def word_detail(request, id):
    found_word = get_object_or_404(WordDefinition, id=id)
    context = { 'found_word': found_word }
    return render(request, 'word_detail.html', context)


# FOR THIS AFTERNOON: how to query the db and if it doesn't exist we add it to the db