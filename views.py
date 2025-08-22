from django.shortcuts import render
def main_points(request):
    points = [
        "fast and affordable",
        "24/7 customer support",
        "wide range of options"
    ]
    return render(request, "main_points.html", {"points":points})