from django.shortcuts import render, redirect
from .forms import CatMemeForm
from .models import CatMeme


def memes_index(request):
    context = { 'memes': CatMeme.objects.all() }
    return render(request, 'memes_index.html', context)


def memes_create(request):
    if request.method == "POST":
        # accept request.FILES which represents the image file we've uploaded
        form = CatMemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('memes_index')
        context = { 'form': form }
        return render(request, 'memes_create.html', context)

    context = { 'form': CatMemeForm() }
    return render(request, 'memes_create.html', context)