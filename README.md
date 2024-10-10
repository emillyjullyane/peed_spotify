# Implementação de uma Estrutura de Playlist com Listas Duplamente Encadeadas e Circulares

Contexto:

Você está criando um sistema de gerenciamento de playlists de música, onde cada playlist é representada por uma lista duplamente encadeada de músicas. Cada música possui informações como nome, artista e duração. O sistema deve permitir o gerenciamento eficiente das músicas da playlist, com operações como adicionar, remover e mover músicas.

Além disso, o sistema também deve permitir que o modo de repetição seja ativado, tornando a playlist circular. Nesse modo, quando o usuário atinge a última música e tenta avançar, ele automaticamente volta para a primeira música da playlist, criando um ciclo contínuo.

## Parte 1: Implementação da Lista Duplamente Encadeada

1. Implemente uma lista duplamente encadeada para representar a playlist. Cada nó deve conter as informações de uma música (nome, artista e duração) e ponteiros para o próximo e o anterior nó.

2. Crie métodos para:

a. Adicionar uma nova música no final da playlist.

b. Remover uma música específica da playlist, dado o nome da música.

c. Mover uma música de uma posição para outra na playlist.

d. Listar todas as músicas na ordem atual da playlist.

## Parte 2: Conversão para Lista Circular

3. Implemente uma função para ativar o modo de repetição, transformando a lista duplamente encadeada em uma lista circular duplamente encadeada.

a. Ao ativar o modo de repetição, o último nó da lista deve apontar para o primeiro, e o primeiro nó deve apontar para o último, formando um ciclo.

4. Crie um método para percorrer a playlist no modo circular, onde ao chegar à última música e avançar, o ponteiro automaticamente volta para a primeira música.

## Parte 3: Funcionalidades Adicionais e Interatividade

5. Adicione funcionalidades interativas, como:

a. Avançar para a próxima música.

b. Retroceder para a música anterior.

c. Ativar/desativar o modo de repetição (circular).


Exemplo:

> Adicionar música: "Bohemian Rhapsody - Queen - 5:55"

> Adicionar música: "Stairway to Heaven - Led Zeppelin - 8:02"

> Adicionar música: "Hotel California - Eagles - 6:30"

> Listar músicas:

1. Bohemian Rhapsody - Queen - 5:55

2. Stairway to Heaven - Led Zeppelin - 8:02

3. Hotel California - Eagles - 6:30


> Mover música "Hotel California" para a posição 1

> Listar músicas:

1. Hotel California - Eagles - 6:30

2. Bohemian Rhapsody - Queen - 5:55

3. Stairway to Heaven - Led Zeppelin - 8:02


> Ativar modo de repetição (playlist circular)

> Avançar para próxima música:

"Bohemian Rhapsody - Queen - 5:55"

> Avançar para próxima música:

"Stairway to Heaven - Led Zeppelin - 8:02"

> Avançar para próxima música:

"Hotel California - Eagles - 6:30"

> Avançar para próxima música:

"Bohemian Rhapsody - Queen - 5:55" (playlist reinicia)
