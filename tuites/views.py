from django.shortcuts import render
from tuites.models import Tuite

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