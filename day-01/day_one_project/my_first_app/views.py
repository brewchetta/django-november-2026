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

menu = {
    1: {
        "id": 1,
        "name": "Cheese Pizza",
        "description": "It's just pizza with cheese, the price is the only thing to get excited about",
        "price": 0.01
    },
    2: {
        "id": 2,
        "name": "Meatlovers Pizza",
        "description": "It's for people who love meat",
        "price": 8.99
    },
    3: {
        "id": 3,
        "name": "Grandma Slice",
        "description": "Slices made by various grandmas",
        "price": 4.99
    },
}

def menu_list(request):
    context = { "pizzas": [ menu[pizza_key] for pizza_key in menu] }
    return render(request, "menu_list.html", context)


from django.http import Http404

def menu_detail(request, id):
    found_pizza = menu.get(id)

    if found_pizza:
        context = { "found_pizza": found_pizza }
        return render(request, "menu_detail.html", context)

    else:
        raise Http404("404: That pizza doesn't exist....")


def calculator(request, num1, num2, operation):
    result = None

    if operation == "plus":
        result = num1 + num2
    elif operation == "minus":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 / num2

    context = { "num1": num1, "num2": num2, "result": result, "operation": operation }
    return render(request, "calculator.html", context)

# all html lives in a special `templates` folder we need to create