from django.http import HttpResponse


def views():
    return HttpResponse("Hello, world from Polls.")
def index():
        return "Index here."