from django.shortcuts import render
from .models import Post
from .forms import FeedbackForm
from django.http import HttpResponseRedirect


def get_feedback(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            name = form.cleaned_data['author']
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            datePosted = form.cleaned_data['datePosted']

            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeedbackForm()

    return render(request, 'base\create.html', {'form': form})

# Create your views here.
def home(request):
    return render(request, 'base\home.html')

def works(request):
    return render(request, 'base\works.html')


def feedback(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'base\\feedback.html', context)


    