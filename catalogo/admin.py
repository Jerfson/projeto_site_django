from django.contrib import admin
from django.utils.html import format_html
from .models import ConfiguracaoSite, Depoimento, Diferencial, ImagemReboque, MensagemContato, Reboque


@admin.register(ConfiguracaoSite)
class ConfiguracaoSiteAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    fieldsets = (
        ('Identidade', {
            'fields': (
                'nome_empresa',
                'slogan',
                'texto_principal',
                'tamanho_fonte_titulo',
                'tamanho_fonte_subtitulo',
                'imagem_principal',
                'imagem_principal_mobile',
                'opacidade_hero',
            )
        }),
        ('Contato e WhatsApp', {
            'fields': ('telefone', 'email', 'endereco', 'texto_botao', 'link_botao')
        }),
        ('Menu', {
            'fields': (
                'mostrar_link_inicio',
                'mostrar_link_modelos',
                'mostrar_link_contato',
                'mostrar_link_admin',
            )
        }),
        ('Seção — Produtos', {
            'fields': ('produtos_eyebrow', 'chamada_produtos'),
        }),
        ('Seção — Sobre / Diferenciais', {
            'fields': (
                'mostrar_secao_sobre',
                'sobre_eyebrow',
                'sobre_titulo',
                'sobre_texto',
            ),
        }),
        ('Seção — Depoimentos', {
            'fields': (
                'mostrar_depoimentos',
                'depoimentos_eyebrow',
                'depoimentos_titulo',
            ),
        }),
        ('Seção — Contato (Página Inicial)', {
            'fields': (
                'modo_contato',
                'contato_eyebrow',
                'contato_titulo',
                'contato_texto',
                'contato_passo1_titulo',
                'contato_passo1_texto',
                'contato_passo2_titulo',
                'contato_passo2_texto',
                'contato_passo3_titulo',
                'contato_passo3_texto',
            ),
        }),
        ('Formulário de Orçamento', {
            'fields': ('form_titulo', 'form_subtitulo', 'form_botao'),
        }),
        ('Página de Detalhe do Reboque', {
            'fields': (
                'mostrar_faixa_detalhes',
                'detalhe_eyebrow',
                'detalhe_preco_info',
                'detalhe_contato_titulo',
                'detalhe_contato_texto',
                'detalhe_passo1_titulo',
                'detalhe_passo1_texto',
                'detalhe_passo2_titulo',
                'detalhe_passo2_texto',
                'detalhe_passo3_titulo',
                'detalhe_passo3_texto',
            ),
        }),
        ('Rodapé', {
            'fields': ('rodape_tagline',),
        }),
        ('Tema', {
            'fields': ('tema_padrao',),
        }),
    )


class ImagemReboqueInline(admin.TabularInline):
    model = ImagemReboque
    extra = 1
    readonly_fields = ('preview_imagem',)

    def preview_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="height:80px;border-radius:4px;">', obj.imagem.url)
        return '—'
    preview_imagem.short_description = 'Prévia'


@admin.register(Reboque)
class ReboqueAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'capacidade', 'disponivel', 'destaque')
    list_filter = ('disponivel', 'destaque')
    search_fields = ('nome', 'resumo', 'descricao')
    prepopulated_fields = {'slug': ('nome',)}
    readonly_fields = ('preview_imagem',)
    inlines = [ImagemReboqueInline]

    def preview_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="height:160px;border-radius:6px;margin-top:6px;">', obj.imagem.url)
        return '—'
    preview_imagem.short_description = 'Prévia'

    def get_fieldsets(self, request, obj=None):
        return (
            (None, {'fields': ('nome', 'slug', 'resumo', 'descricao')}),
            ('Imagem principal', {'fields': ('imagem', 'preview_imagem')}),
            ('Detalhes', {'fields': ('preco', 'capacidade', 'dimensoes', 'disponivel', 'destaque')}),
        )


@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'interesse', 'criada_em', 'lida')
    list_filter = ('lida', 'criada_em')
    search_fields = ('nome', 'telefone', 'email', 'mensagem')
    readonly_fields = ('criada_em',)


@admin.register(Diferencial)
class DiferencialAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ordem', 'ativo')
    list_editable = ('ordem', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('titulo', 'texto')


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao', 'ordem', 'ativo')
    list_editable = ('ordem', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome', 'localizacao', 'texto')
