from company.models import Company


def request(request):
    context_extras = {}
    if request.user.is_authenticated:
        context_extras = {"company": Company.objects.get(id=request.session["company_id"])}

    return context_extras
