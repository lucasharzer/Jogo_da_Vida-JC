# Jogo da Vida de John Conway

# Descrição 

Um jogo criado em 1970 por John Horton Conway, matemático britânico, que reproduz as alterações e mudanças em grupos de seres vivos com um modelo de evolução temporal (autômato celular).

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
- Tabela bidimensional com 40 linhas e 40 colunas;
- As células vivas (células em verde) já foram determinadas no código; 
- Uso do módulo tkinter para criar interface gráfica (não é necessário instalação);

# Comandos

Instalar dependências:
```bash
pip install -r requirements.txt
```

Executar código:
```bash
python jogo.py
```

# Resultado

<span align="center">
    <img src="https://user-images.githubusercontent.com/85804895/134363025-db0e73f7-be87-4e96-98c4-6f5e0f2d4fdc.gif">
</span>

<span align="center">
    <img src="https://user-images.githubusercontent.com/85804895/134362858-4bcd93f9-23f1-4a53-a8f3-dc4dbed9572d.png", width=900>
</span>

# Referências

- https://labdegaragem.com/profiles/blogs/jogo-da-vida-de-conway-em-python (Jogo da Vida simples em Python com tkinter)
- https://guiadoestudante.abril.com.br/estudo/conheca-john-conway-o-matematico-que-criou-o-jogo-da-vida/ (informações sobre o jogo e o criador)
- https://www.marcogomes.com/gameoflife/html/ (exemplo do jogo)
