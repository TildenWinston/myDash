from .models import Post
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('login/index.html')
    context = {
        'posts': Post.objects.order_by('-date')
        if request.user.is_authenticated else []
    }
    return HttpResponse(template.render(context, request))
