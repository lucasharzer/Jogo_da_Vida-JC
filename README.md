# Jogo da Vida de John Conway

# Descrição 

Um jogo criado em 1970 por John Horton Conway, matemático britânico, que reproduz as alterações e mudanças em grupos de seres vivos (autômato celular).
- Não possui jogador, pois a evolução do jogo é definido pelo estado inicial das células;
- Tabela bidimensional;
- Células que assumem dois possíveis estados: viva ou morta;
- cada célula interage com oito vizinhas.

# Regras Simples do Jogo

- Primeira Regra: Qualquer célula viva com menos de 2 vizinhos vivos morre de solidão;
- Segunda Regra: Qualquer célula viva com mais de 3 vizinhos vivos morre de superpopulação;
- Terceira Regra: Qualquer célula morta com exatamente 3 vizinhos vivos se torna uma célula viva;
- Quarta Regra: Qualquer célula viva com 2 ou 3 vizinhos vivos continua no mesmo estado para a próxima geração.

# Observações sobre o código

- Feito em Python;
- tabela bidimensional com 40 linhas e 40 colunas;
- Uso do módulo tkinter para criar interface gráfica (não é necessário instalação);

