from django.shortcuts import render

introducao = {
    "titulo": "História",
    "subtitulo": "A sitcom de sucesso",
    "conteudo": "Em 22 de setembro de 1994, a NBC exibia o primeiro episódio de Friends, série criada por David Crane e Marta Kauffman que se tornou um fenômeno mundial. A trama sobre seis amigos que lutam para encontrar estabilidade em sua vida ganhou o mundo, e transformou o sexteto formado por Jennifer Aniston, Courteney Cox, Lisa Kudrow, Matt LeBlanc, Matthew Perry e David Schwimmer ícones da TV. O impacto cultural conquistado por Friends fez da série uma das mais amadas da história da televisão. Seus personagens são lembrados até hoje pelos fãs, enquanto seus episódios ficam em constante reexibição em centenas de países, sendo disponibilizados em plataformas de streaming e ainda figurando entre os programas mais assistidos, décadas após o seu fim.",
    "primeira_foto": "app/img/photo-one.jpg",
    "segunda_foto": "app/img/photo-two.jpg",
    "terceira_foto": "app/img/photo-three.jpg",
}

atores = [
    {
        "nome": "Jennifer Aniston",
        "personagem": "Rachel Green",
        "idade": 56,
        "id": 1,
        "local_nasc": "Califórnia, EUA",
        "imagem": "app/img/cast-rachel.webp",
    },

    {
        "nome": "Courteney Cox",
        "personagem": "Monica Geller",
        "idade": 61,
        "id": 2,
        "local_nasc": "Alabama, EUA",
        "imagem": "app/img/cast-monica.webp",
    },

    {
        "nome": "Lisa Kudrow",
        "personagem": "Phoebe Buffay",
        "idade": 62,
        "id": 3,
        "local_nasc": "Califórnia, EUA",
        "imagem": "app/img/cast-phoebe.webp",
    },

    {
        "nome": "David Schwimmer",
        "personagem": "Ross Geller",
        "idade": 58,
        "id": 4,
        "local_nasc": "Nova York, EUA",
        "imagem": "app/img/cast-ross.webp",
    },

    {
        "nome": "Matt LeBlanc",
        "personagem": "Joey Tribbiani",
        "idade": 57,
        "id": 5,
        "local_nasc": "Massachusetts, EUA",
        "imagem": "app/img/cast-joey.webp",
    },

    {
        "nome": "Matthew Perry",
        "personagem": "Chandler Bing",
        "idade": 54,
        "id": 6,
        "local_nasc": "Massachusetts, EUA",
        "imagem": "app/img/cast-chandler.webp",
    }
]

sobre = [
    {
        "titulo": "Sobre o site",
        "conteudo": "<p class='w3-justify'>Este site foi desenvolvido como parte do nosso primeiro projeto na disciplina de Programação de Sistemas para Internet, com objetivo de colocar em prática os conhecimentos adquiridos em sala de aula sobre desenvolvimento de sites dinâmicos. Para isso, utilizamos o framework Django.</p>",
    },

    {
        "titulo": "Autores",
        "subtitulo": "Beatriz & Gabriela",
        "conteudo": "<p class='w3-justify'>As responsáveis pelo desenvolvimento deste website são <i>Anna Beatriz Faustino Gomes</i> e <i>Gabriela de Freitas Maia</i>, ambas discentes do curso técnico integrado em Informática para Internet do campus São Paulo do Potengi.</p>",
    },

    {
        "titulo": "Créditos",
        "conteudo": "<p class='w3-justify mb-0'>Todas as informações e imagens utilizadas neste site estão disponíveis para uso público na internet e foram utilizadas com fim exclusivamente educacional.</p>",
    }
]

context = {
    "introducao": introducao,
    "atores": atores,
    "sobre": sobre,
}

def index(request):
    return render(request, 'app/index.html', context)

def elenco(request):
    return render(request, 'app/elenco.html', context)

def sobre(request):
    return render(request, 'app/sobre.html', context)

def ator(request, id_ator):
    return render(request, 'app/ator.html', atores[id_ator - 1])