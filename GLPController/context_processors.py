from controller.models import Company


def request(request):
    context_extras = {}
    if request.user.is_authenticated:
        context_extras = {"company": Company.objects.get()}

    return context_extras
