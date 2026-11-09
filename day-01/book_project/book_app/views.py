from django.shortcuts import render

top_five = [
    {
        "id": 1,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "description": "There was an alchemist and the alchemist was alchemizing.",
    },
    {
        "id": 2,
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel Garcia Marquez",
        "description": "It was really lonely for 100 years.",
    },
    {
        "id": 3,
        "title": "The Devil in the White City",
        "author": "Erik Larson",
        "description": "Oh no murder!",
    },
    {
        "id": 4,
        "title": "Angel of Darkness",
        "author": "Caleb Carr",
        "description": "It was very dark and we saw an angel.",
    },
    {
        "id": 5,
        "title": "The Alienist",
        "author": "Caleb Carr",
        "description": "Watch out for aliens. I want to believe.",
    },
]

def home(request):
    context = { "top_five": top_five }
    return render(request, "home.html", context)