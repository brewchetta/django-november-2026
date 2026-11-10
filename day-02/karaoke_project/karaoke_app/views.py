from django.shortcuts import render
from django.http import Http404

songs_list = [
    {
        "id": 1,
        "title": "Never Gonna Give You Up",
        "artist": "Rick Astley",
        "video_id": "6PLatPMoxGw?si=fLqudrUkDO4Y23AY",
    },
    {
        "id": 2,
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "video_id": "yvEcMrstp80?si=-QsGKzZEqtaiyR8p",
    }
]


# HOME
def home(request):
    context = { 'songs': songs_list }
    return render(request, "home.html", context)


def find_song(id):
    return next((s for s in songs_list if s["id"] == id), None)

# SONG_DETAIL
def song_detail(request, id):
    found_song = find_song(id)

    if found_song:
        context = {'song': found_song}
        return render(request, "song_detail.html", context)

    else:
        raise Http404("Could not find that song...")