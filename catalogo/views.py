from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from .forms import MensagemContatoForm
from .models import ConfiguracaoSite, Depoimento, Diferencial, Reboque


def _site_config():
    return ConfiguracaoSite.objects.first()


def _enviar_email_contato(mensagem):
    destino = getattr(settings, 'EMAIL_DESTINO', '')
    if not destino or not settings.EMAIL_HOST_USER:
        return
    assunto = f'Novo contato: {mensagem.nome}'
    corpo = (
        f'Nome: {mensagem.nome}\n'
        f'Telefone: {mensagem.telefone}\n'
        f'E-mail: {mensagem.email or "—"}\n'
        f'Interesse: {mensagem.interesse or "—"}\n\n'
        f'Mensagem:\n{mensagem.mensagem}'
    )
    try:
        send_mail(assunto, corpo, settings.EMAIL_HOST_USER, [destino], fail_silently=True)
    except Exception:
        pass


def home(request):
    config = _site_config()
    reboques = Reboque.objects.filter(disponivel=True)
    diferenciais = Diferencial.objects.filter(ativo=True)
    depoimentos = Depoimento.objects.filter(ativo=True)

    if request.method == 'POST':
        form = MensagemContatoForm(request.POST)
        if form.is_valid():
            mensagem = form.save()
            _enviar_email_contato(mensagem)
            messages.success(request, 'Mensagem enviada. Entraremos em contato em breve.')
            return redirect('home')
    else:
        form = MensagemContatoForm()

    return render(request, 'catalogo/home.html', {
        'config': config,
        'reboques': reboques,
        'diferenciais': diferenciais,
        'depoimentos': depoimentos,
        'form': form,
    })


def reboque_detalhe(request, slug):
    config = _site_config()
    reboque = get_object_or_404(Reboque.objects.prefetch_related('galeria'), slug=slug, disponivel=True)
    diferenciais = Diferencial.objects.filter(ativo=True)
    form = MensagemContatoForm(initial={'interesse': reboque.nome})

    if request.method == 'POST':
        form = MensagemContatoForm(request.POST)
        if form.is_valid():
            mensagem = form.save()
            _enviar_email_contato(mensagem)
            messages.success(request, 'Mensagem enviada. Entraremos em contato em breve.')
            return redirect(reboque.get_absolute_url())

    return render(request, 'catalogo/detalhe.html', {
        'config': config,
        'reboque': reboque,
        'diferenciais': diferenciais,
        'form': form,
    })
