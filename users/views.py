from django.shortcuts import render, redirect
from .forms import PeopleForm
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import People

# def people(request):
#     if request.method == 'POST':
#         form = PeopleForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return render(request, 'people.html', context={'form': form})
#     return render(request, 'people.html', context={'form': PeopleForm()})


class PeopleView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'people.html', context={'form': PeopleForm()})

    def post(self, request, *args, **kwargs):
        form = PeopleForm(request.POST)
        if form.is_valid:
            form.save()
        return render(request, 'people.html', context={'form': form})


class AboutVew(TemplateView):
    template_name = 'test.html'

    def get_context_data(self, **kwargs):
        context = super(AboutVew, self).get_context_data(**kwargs)
        context['text'] = 'hello Armenia'
        people = People.objects.all()
        context["peoples"] = people
        return context


class PeopleCreatView(CreateView):
    model = People
    form_class = PeopleForm
    template_name = 'people.html'

    def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     form.instance.timestamp = datetime.now()
        form.save()
        return redirect('about')

    def success_url(self):
        return redirect('people')
