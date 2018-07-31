from django.shortcuts import render
from tuites.models import Tuite
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from tuites.forms import PostTuiteForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PostTuiteView(LoginRequiredMixin, CreateView):
    model = Tuite
    template_name = 'post_tuite.html'
    form_class = PostTuiteForm
    success_url = reverse_lazy('post_tuite')
    

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