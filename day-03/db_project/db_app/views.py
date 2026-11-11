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


# detail using slug and get_object_or_404 ##########################################

from .dictionary_api import retrieve_word
from django.shortcuts import get_object_or_404

def word_detail_by_slug(request, word):
    try:
        found_word = WordDefinition.objects.get(word=word)
        context = { 'found_word': found_word }
        return render(request, 'word_detail.html', context)
    except:
        # use API to find the word if it exists
        data = retrieve_word(word)

        if data:
            # get the definition and use examples
            definition = data["senses"][0]["definition"]
            use = "; ".join(data["senses"][0]["examples"])
            # save it to the db
            new_word = WordDefinition(word=word, definition=definition, use=use)
            new_word.save()
            # render the new_word
            context = { 'found_word': new_word }
            return render(request, 'word_detail.html', context)
        else:
            raise Http404("That word does not exist...")