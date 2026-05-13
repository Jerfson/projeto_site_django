from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ConfiguracaoSite(models.Model):
    nome_empresa = models.CharField('nome da logo', max_length=120, default='Jerfson Reboques', blank=True)
    slogan = models.CharField('título', max_length=180, default='Reboques fortes, sob medida e prontos para trabalhar', blank=True)
    texto_principal = models.TextField(
        'subtítulo',
        default='Fabricamos e vendemos reboques para transporte, trabalho e lazer, com acabamento resistente e atendimento direto pelo WhatsApp.',
        blank=True,
    )
    tamanho_fonte_titulo = models.PositiveIntegerField('tamanho da fonte do título', default=72)
    tamanho_fonte_subtitulo = models.PositiveIntegerField('tamanho da fonte do subtítulo', default=20)
    imagem_principal = models.ImageField('imagem principal (desktop)', upload_to='site/', blank=True)
    imagem_principal_mobile = models.ImageField('imagem principal (mobile)', upload_to='site/', blank=True, help_text='Opcional. Se vazio, usa a imagem desktop no mobile também.')
    opacidade_hero = models.FloatField('opacidade do overlay da hero (0.0 a 1.0)', default=0.5, help_text='0.0 = transparente, 1.0 = totalmente escuro')
    telefone = models.CharField('telefone/WhatsApp', max_length=30, blank=True)
    email = models.EmailField('e-mail', blank=True)
    endereco = models.CharField('endereço', max_length=180, blank=True)
    texto_botao = models.CharField('texto do botão principal', max_length=60, default='Chamar no WhatsApp', blank=True)
    link_botao = models.URLField('link do botão principal', blank=True)
    chamada_produtos = models.CharField('chamada dos produtos', max_length=160, default='Modelos disponíveis', blank=True)
    sobre_titulo = models.CharField('título sobre', max_length=120, default='Construído para durar', blank=True)
    sobre_texto = models.TextField(
        'texto sobre',
        default='Cada reboque pode receber medidas, pintura, madeira, grade e acabamento conforme a necessidade do cliente.',
        blank=True,
    )
    mostrar_secao_sobre = models.BooleanField('mostrar seção sobre/diferenciais', default=True)
    mostrar_depoimentos = models.BooleanField('mostrar depoimentos', default=True)
    mostrar_faixa_detalhes = models.BooleanField('mostrar faixa técnica nos detalhes', default=True)
    mostrar_link_inicio = models.BooleanField('mostrar link início no menu', default=True)
    mostrar_link_modelos = models.BooleanField('mostrar link modelos no menu', default=True)
    mostrar_link_contato = models.BooleanField('mostrar link contato no menu', default=True)
    mostrar_link_admin = models.BooleanField('mostrar link do admin no menu', default=True)

    # Seção de produtos
    produtos_eyebrow = models.CharField('rótulo seção produtos', max_length=60, default='Reboques', blank=True)

    # Seção sobre
    sobre_eyebrow = models.CharField('rótulo seção sobre', max_length=60, default='Oficina e acabamento', blank=True)

    # Seção depoimentos
    depoimentos_eyebrow = models.CharField('rótulo seção depoimentos', max_length=60, default='Clientes', blank=True)
    depoimentos_titulo = models.CharField('título seção depoimentos', max_length=120, default='Quem comprou recomenda', blank=True)

    MODO_CONTATO_CHOICES = [
        ('formulario', 'Formulário de orçamento'),
        ('whatsapp', 'Botão WhatsApp'),
    ]
    modo_contato = models.CharField(
        'modo da seção de contato',
        max_length=20,
        choices=MODO_CONTATO_CHOICES,
        default='formulario',
    )

    # Seção contato (página inicial)
    contato_eyebrow = models.CharField('rótulo seção contato', max_length=60, default='Orçamento', blank=True)
    contato_titulo = models.CharField('título seção contato', max_length=120, default='Conte o reboque que você precisa', blank=True)
    contato_texto = models.TextField(
        'texto seção contato',
        default='Informe uso, medidas desejadas e acabamento. A resposta pode vir com opções de modelo, personalização e próximos passos para fechar a compra.',
        blank=True,
    )
    contato_passo1_titulo = models.CharField('passo 1 — título', max_length=120, default='Você envia a necessidade', blank=True)
    contato_passo1_texto = models.CharField('passo 1 — texto', max_length=220, default='Transporte, medidas, carga e uso principal.', blank=True)
    contato_passo2_titulo = models.CharField('passo 2 — título', max_length=120, default='Montamos a melhor opção', blank=True)
    contato_passo2_texto = models.CharField('passo 2 — texto', max_length=220, default='Modelo, acabamento, acessórios e disponibilidade.', blank=True)
    contato_passo3_titulo = models.CharField('passo 3 — título', max_length=120, default='Orçamento direto', blank=True)
    contato_passo3_texto = models.CharField('passo 3 — texto', max_length=220, default='Negociação pelo contato informado no formulário.', blank=True)

    # Formulário de orçamento
    form_titulo = models.CharField('título do formulário', max_length=120, default='Solicitação de orçamento', blank=True)
    form_subtitulo = models.CharField('subtítulo do formulário', max_length=220, default='Quanto mais detalhes você enviar, mais certeira fica a resposta.', blank=True)
    form_botao = models.CharField('texto do botão do formulário', max_length=80, default='Enviar pedido de orçamento', blank=True)

    # Página de detalhe do reboque
    detalhe_eyebrow = models.CharField('rótulo página de detalhe', max_length=60, default='Reboque disponível', blank=True)
    detalhe_preco_info = models.CharField('texto info preço (detalhe)', max_length=220, default='Solicite orçamento para medidas, acabamento e disponibilidade.', blank=True)
    detalhe_contato_titulo = models.CharField('título contato (detalhe)', max_length=120, default='Tenho interesse neste reboque', blank=True)
    detalhe_contato_texto = models.TextField(
        'texto contato (detalhe)',
        default='Envie seus dados e diga se quer alguma alteração de medida, pintura, madeira ou acessório. A solicitação fica salva no painel.',
        blank=True,
    )
    detalhe_passo1_titulo = models.CharField('detalhe passo 1 — título', max_length=120, default='Informe o interesse', blank=True)
    detalhe_passo1_texto = models.CharField('detalhe passo 1 — texto', max_length=220, default='O formulário já pode ir com este modelo como referência.', blank=True)
    detalhe_passo2_titulo = models.CharField('detalhe passo 2 — título', max_length=120, default='Ajuste sob medida', blank=True)
    detalhe_passo2_texto = models.CharField('detalhe passo 2 — texto', max_length=220, default='Explique mudanças de tamanho, carga ou acabamento.', blank=True)
    detalhe_passo3_titulo = models.CharField('detalhe passo 3 — título', max_length=120, default='Resposta rápida', blank=True)
    detalhe_passo3_texto = models.CharField('detalhe passo 3 — texto', max_length=220, default='Retorno pelo contato informado no formulário.', blank=True)

    # Rodapé
    rodape_tagline = models.CharField('tagline do rodapé', max_length=120, default='Venda e fabricação de reboques', blank=True)

    # Tema
    TEMA_CHOICES = [('dark', 'Escuro (padrão)'), ('light', 'Claro')]
    tema_padrao = models.CharField('tema padrão do site', max_length=5, choices=TEMA_CHOICES, default='dark')

    class Meta:
        verbose_name = 'configuração do site'
        verbose_name_plural = 'configuração do site'

    def __str__(self):
        return self.nome_empresa or self.slogan or 'Configuração principal do site'


class Reboque(models.Model):
    nome = models.CharField(max_length=140)
    slug = models.SlugField(unique=True, blank=True)
    resumo = models.CharField(max_length=220, blank=True)
    descricao = models.TextField('descrição', blank=True)
    preco = models.DecimalField('preço', max_digits=10, decimal_places=2, null=True, blank=True)
    imagem = models.ImageField(upload_to='reboques/')
    capacidade = models.CharField(max_length=80, blank=True)
    dimensoes = models.CharField('dimensões', max_length=80, blank=True)
    destaque = models.BooleanField(default=False)
    disponivel = models.BooleanField('disponível', default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-destaque', '-criado_em']
        verbose_name = 'reboque'
        verbose_name_plural = 'reboques'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.nome)
            slug = base
            n = 1
            while Reboque.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('reboque_detalhe', kwargs={'slug': self.slug})


class ImagemReboque(models.Model):
    reboque = models.ForeignKey(Reboque, related_name='galeria', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='reboques/galeria/')
    legenda = models.CharField(max_length=120, blank=True)

    class Meta:
        verbose_name = 'imagem do reboque'
        verbose_name_plural = 'imagens do reboque'

    def __str__(self):
        return self.legenda or f'Imagem de {self.reboque}'


class Diferencial(models.Model):
    titulo = models.CharField(max_length=120)
    texto = models.CharField(max_length=220)
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem', 'titulo']
        verbose_name = 'diferencial'
        verbose_name_plural = 'diferenciais'

    def __str__(self):
        return self.titulo


class Depoimento(models.Model):
    nome = models.CharField(max_length=120)
    texto = models.TextField()
    localizacao = models.CharField('localização', max_length=120, blank=True)
    ativo = models.BooleanField(default=True)
    ordem = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['ordem', 'nome']
        verbose_name = 'depoimento'
        verbose_name_plural = 'depoimentos'

    def __str__(self):
        return self.nome


class MensagemContato(models.Model):
    nome = models.CharField(max_length=120)
    telefone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    interesse = models.CharField('interesse', max_length=140, blank=True)
    mensagem = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    class Meta:
        ordering = ['-criada_em']
        verbose_name = 'mensagem de contato'
        verbose_name_plural = 'mensagens de contato'

    def __str__(self):
        return f'{self.nome} - {self.telefone}'
