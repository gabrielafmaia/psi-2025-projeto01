from django.shortcuts import render, get_object_or_404
from .models import Site, Inicio, CarrosselItem, Elenco, Ator, Sobre, SecaoSobre

# introducao = {
#     "titulo": "História",
#     "subtitulo": "A sitcom de sucesso",
#     "conteudo": "Em 22 de setembro de 1994, a NBC exibia o primeiro episódio de Friends, série criada por David Crane e Marta Kauffman que se tornou um fenômeno mundial. A trama sobre seis amigos que lutam para encontrar estabilidade em sua vida ganhou o mundo, e transformou o sexteto formado por Jennifer Aniston, Courteney Cox, Lisa Kudrow, Matt LeBlanc, Matthew Perry e David Schwimmer ícones da TV. O impacto cultural conquistado por Friends fez da série uma das mais amadas da história da televisão. Seus personagens são lembrados até hoje pelos fãs, enquanto seus episódios ficam em constante reexibição em centenas de países, sendo disponibilizados em plataformas de streaming e ainda figurando entre os programas mais assistidos, décadas após o seu fim.",
#     "primeira_foto": "app/img/photo-one.jpg",
#     "segunda_foto": "app/img/photo-two.jpg",
#     "terceira_foto": "app/img/photo-three.jpg",
# }

# atores = [
#     {
#         "nome": "Jennifer Aniston",
#         "personagem": "Rachel Green",
#         "idade": 56,
#         "id": 1,
#         "local_nasc": "Califórnia, EUA",
#         "imagem": "app/img/cast-rachel.webp",
#         "descricao": "Jennifer Aniston nasceu o 11 de fevereiro de 1969 em Sherman Oaks, Califórnia, EUA. É atriz e produtora, conhecida pelo seu trabalho em Friends (1994), Cake: Uma Razão para Viver (2014) e Família do Bagulho (2013).",
#     },

#     {
#         "nome": "Courteney Cox",
#         "personagem": "Monica Geller",
#         "idade": 61,
#         "id": 2,
#         "local_nasc": "Alabama, EUA",
#         "imagem": "app/img/cast-monica.webp",
#         "descricao": "Courteney Cox nasceu o 15 de junho de 1964 em Birmingham, Alabama, EUA. É atriz e produtora, conhecida pelo seu trabalho em Friends (1994), Pânico (1996) e Pânico 3 (2000).",
#     },

#     {
#         "nome": "Lisa Kudrow",
#         "personagem": "Phoebe Buffay",
#         "idade": 62,
#         "id": 3,
#         "local_nasc": "Califórnia, EUA",
#         "imagem": "app/img/cast-phoebe.webp",
#         "descricao": "Lisa Kudrow nasceu o 30 de julho de 1963 em Los Angeles, Califórnia, EUA. É atriz e produtora, conhecida pelo seu trabalho em Friends (1994), The Comeback (2005) e O Oposto do Sexo (1998).",
#     },

#     {
#         "nome": "David Schwimmer",
#         "personagem": "Ross Geller",
#         "idade": 58,
#         "id": 4,
#         "local_nasc": "Nova York, EUA",
#         "imagem": "app/img/cast-ross.webp",
#         "descricao": "David Schwimmer nasceu o 2 de novembro de 1966 em Nova Iorque, EUA. É ator e diretor, conhecido pelo seu trabalho em Friends (1994), Seis Dias, Sete Noites (1998) e Irmãos de Guerra (2001).",
#     },

#     {
#         "nome": "Matt LeBlanc",
#         "personagem": "Joey Tribbiani",
#         "idade": 57,
#         "id": 5,
#         "local_nasc": "Massachusetts, EUA",
#         "imagem": "app/img/cast-joey.webp",
#         "descricao": "Matt LeBlanc nasceu o 25 de julho de 1967 em Newton, Massachusetts, EUA. É ator e produtor, conhecido pelo seu trabalho em Friends (1994), Perdidos no Espaço: O Filme (1998) e Episodes (2011).",
#     },

#     {
#         "nome": "Matthew Perry",
#         "personagem": "Chandler Bing",
#         "idade": 54,
#         "id": 6,
#         "local_nasc": "Massachusetts, EUA",
#         "imagem": "app/img/cast-chandler.webp",
#         "descricao": "Matthew Perry nasceu o 19 de agosto de 1969 em Massachusetts, EUA. Era ator e produtor e foi conhecido pelo seu trabalho em Friends (1994), Studio 60 on the Sunset Strip (2006) e Meu Vizinho Mafioso (2000). Faleceu o 28 de outubro de 2023.",
#     }
# ]

# sobre = [
#     {
#         "titulo": "Sobre o site",
#         "conteudo": "Este site foi desenvolvido como parte do nosso primeiro projeto na disciplina de Programação de Sistemas para Internet, com objetivo de colocar em prática os conhecimentos adquiridos em sala de aula sobre desenvolvimento de sites dinâmicos. Para isso, utilizamos o framework Django.",
#     },

#     {
#         "titulo": "Autores",
#         "subtitulo": "Beatriz & Gabriela",
#         "conteudo": "As responsáveis pelo desenvolvimento deste website são <i>Anna Beatriz Faustino Gomes</i> e <i>Gabriela de Freitas Maia</i>, ambas discentes do curso técnico integrado em Informática para Internet do campus São Paulo do Potengi.",
#     },

#     {
#         "titulo": "Créditos",
#         "conteudo": "Todas as informações e imagens utilizadas neste site foram obtidas a partir de fontes de acesso público na internet, sendo utilizadas com fim exclusivamente educacional.",
#     }
# ]

def index(request):
    context = {
        'inicio': Inicio.objects.first(),
        'carrossel_itens': CarrosselItem.objects.all(),
        'site': Site.objects.first(),
    }
    return render(request, 'app/index.html', context)

def elenco(request):
    context = {
        'atores': Ator.objects.all(),
        'elenco': Elenco.objects.first(),
        'site': Site.objects.first(),
    }
    return render(request, 'app/elenco.html', context)

def sobre(request):
    context = {
        'sobre': Sobre.objects.first(),
        'secoes_sobre': SecaoSobre.objects.all(),
        'site': Site.objects.first(),
    }
    return render(request, 'app/sobre.html', context)

def ator(request, id_ator):
    ator = get_object_or_404(Ator, id=id_ator)
    context = {
        'ator': ator,
    }
    return render(request, 'app/ator.html', context)