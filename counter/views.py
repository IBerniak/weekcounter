from django.shortcuts import render, redirect
from .forms import DateForm
from .utils import calculate_weeks, convert_date_string


def input_date(request):
    """
    Handles a view for the date form
    """
    if request.method == "POST":
        form = DateForm(request.POST)

        if form.is_valid():
            # To catch and send the inputed date with no database nor message broker
            inputed_date = form.data.dict()["calculated_date"]
            return redirect("weeks", inputed_date)

    else:
        form = DateForm()

    return render(request, "counter/input_date.html", {"form": form})


def result_in_weeks(request, inputed_date):
    """
    Handles a view for the result of a calculation
    """
    datetime_date = convert_date_string(inputed_date)
    weeks = calculate_weeks(datetime_date)
    return render(request, "counter/weeks.html", {"weeks": weeks, "date": inputed_date})
