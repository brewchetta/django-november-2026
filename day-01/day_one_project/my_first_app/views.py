from django.shortcuts import render

# views is basically your controller actions

def home(request):
    # home.html is the actual template we will show the user
    return render(request, "home.html")


def about(request):
    # about.html is the actual template we will show the user
    return render(request, "about.html")


from datetime import datetime, timedelta, time, date

def context(request):
    # calculate days until xmas
    today = date.today()
    target_date = date(today.year, 12, 25)
    delta = target_date - today

    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    midnight = datetime.combine(tomorrow, time.min)
    time_remaining = midnight - now
    hours_remaining, remainder = divmod(time_remaining.seconds, 3600)
    minutes_remaining, _ = divmod(remainder, 60)

    # add to context
    context = {
        "days_until_xmas": delta.days,
        "hours_remaining": hours_remaining,
        "minutes_remaining": minutes_remaining,
        "xmas_image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR807tlVh-iMBFUYA3y0vXTRcTvmrojZV7VkmupPjyPWw&s=10"
    }
    # return with context
    return render(request, "context.html", context)

def contacts(request):
    context = {
        'some_variable': { "name": "subdictionary" },
        'current_time': datetime.now(),
        "our_contacts": [
            "IT: 123-4567",
            "HR: 987-6543",
            "Boss: 555-4444",
            "Janitor: 999-8888",
        ]
    }
    return render(request, "contacts.html", context)

# all html lives in a special `templates` folder we need to create