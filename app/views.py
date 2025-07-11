from django.shortcuts import render

introducao = [
    {
        "titulo": "História",
        "conteudo": "Em 22 de setembro de 1994, a NBC exibia o primeiro episódio de Friends, série criada por David Crane e Marta Kauffman que se tornou um fenômeno mundial. A trama sobre seis amigos na casa dos 20 anos que lutam para encontrar estabilidade emsua vida ganhou o mundo, e transformou o sexteto formado por Jennifer Aniston, Courteney Cox, Lisa Kudrow, Matt LeBlanc, Matthew Perry e David Schwimmer ícones da TV.",
        "imagem": "app/img/friends-frame"
    }
]

atores = [
    {
    "nome": "Jennifer Aniston",
    "idade": 56,
    "id": 1,
    "local_nasc": "Sherman Oaks, Los Angeles, Califórnia, EUA",
    "imagem": "app/img/cast-rachel.webp"
    },

    {
    "nome": "David Schwimmer",
    "idade": 58,
    "id": 2,
    "local_nasc": "Flushing, Queens, Nova York, EUA",
    },

    {
    "nome": "Courteney Cox",
    "idade": 61,
    "id": 3,
    "local_nasc": " Birmingham, Alabama, EUA",
    },

    {
    "nome": "Lisa Kudrow",
    "idade": 62,
    "id": 4,
    "local_nasc": "Encino, Los Angeles, EUA",
    },

    {
    "nome": "Matt LeBlanc",
    "idade": 57,
    "id": 5,
    "local_nasc": "Newton, Massachusetts, EUA",
    },

    {
    "nome": "Matthew Perry",
    "idade": 54,
    "id": 6,
    "local_nasc": "Williamstown, Massachusetts, EUA",
    }
]

context = {
    "atores": atores,
    "introducao": introducao,
}

def index(request):
    return render(request, 'app/index.html')

def elenco(request):
    return render(request, 'app/elenco.html', context)

def sobre(request):
    return render(request, 'app/sobre.html')

def ator(request, id_ator):
    return render(request, 'app/ator.html', atores[id_ator - 1])