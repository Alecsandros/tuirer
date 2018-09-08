from django.shortcuts import render
from tuites.models import Tuite
from django.views.generic import CreateView, RedirectView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from tuites.forms import PostTuiteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class PostTuiteView(LoginRequiredMixin, CreateView):
    model = Tuite
    template_name = 'post_tuite.html'
    form_class = PostTuiteForm
    success_url = reverse_lazy('tuites:post_tuite')
    

    def get_initial(self):
        return {
            'user': self.request.user
        }


    def form_valid(self, form):
        messages.success(
            self.request,
            'Você postou um Turite!'
        )
        return super().form_valid(form)

# Create your views here.

def post_tuite(request):
    context = {}
    if request.method == 'POST':
        print('Enviando o formulário')
        print(request.POST)
        content = request.POST.get('content', None)
        print(content)
        if content == '':
            context['error'] = 'Tuite não pode estar vazio'
        else:
            print(request.user)
            print('Formulário válido, postar!')
            Tuite.objects.create(
                content=content,
                author=request.user,
            )
            context['sucess'] = 'Tuite enviado com sucesso'
        
    return render(request, 'post_tuite.html', context)


class ListTuiteView(generic.ListView):
    template_name = 'home.html'
    model = Tuite
    context_object_name = 'tuites'



class SingleTuiteView(generic.DetailView):
    template_name = 'single_tuite.html'
    model = Tuite
    context_object_name = 'tuite'


class LikeTuiteView(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        tuite_pk = kwargs.get('pk')

        tuite = Tuite.objects.get(pk=tuite_pk)
        url = tuite
        
        user_already_liked = self.request.user.liked_tuites.filter(
            pk__in=[tuite_pk]).exists()

        if user_already_liked:
            self.request.user.liked_tuites.remove(tuite)
            messages.success(
                self.request,
                'Você descurtiu o Tuite!'
            )
            return reverse('tuites:tuite', args=[tuite_pk])
            
        self.request.user.liked_tuites.add(tuite)
        messages.success(self.request, 'Você curtiu este Tuite!')
        return reverse('tuites:tuite', args=[tuite_pk])