# Sistema de recomendação de filmes

Com isso vamos utilizar o algoritmo KNN, para  realizar a classificação dos vizinhos mais próximos.

## O que é o KNN ( K Nearest Neighbor) "K-vizinho mais próximo"

O **KNN** é um algoritmo não paramétrico, aonde a estrutura do modelo será determinada pelo dataset utilizado. Este algoritmo também é conhecido como de aprendizado lento ou melhor dizendo, é um algoritmo preguiçoso, o termo certo é “lazy”. Os algoritmos do tipo lazy, não necessitam de dados de treinamento para se gerar o modelo, o que diminui em partes o processo inicial, mas em contrapartida gerará uma necessidade de analise posterior mais apurada. No caso de algoritmos que não necessitam de treinamento, todos os dados obtidos no dataset serão utilizados na fase de teste, resultando em um treinamento muito rápido e em um teste e validação lentos, momento o qual necessitamos estar bem atentos aos resultados gerados.

### Como funciona o algoritmo KNN

Neste algoritmo possuímos uma variável chamada de K, a qual é parte do nome do modelo e também o principal parâmetro a ser selecionado. Este parâmetro direcionará a quantidade de vizinhos (neighborn em inglês). Em casos de modelos binários, aonde possuímos apenas duas classes, em geral aplicasse valores ímpares a K, mas lembre que cada caso é um caso, “No free lunch”. Imagine que temos um valor P1 o qual queremos predizer, entre um grupo de duas classes aonde o valor atribuído a K foi 1 (K=1), primeiro iremos identificar o ponto mais próximo a ele e depois qual a label que o identifica (classe A por exemplo)

![XHTML válido](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1531424125/Knn_k1_z96jba.png)

Após identificar o ponto mais próximo e identificar a label deste ponto (Ex.: Classe A), iremos predizer a que classe o ponto P1 faz parte. Para identificar de fato a que grupo o ponto P1 faz parte, iremos realizar uma votação aonde a maioria irá dizer a que classe este ponto P1 realmente faz parte.

![XHTML válido](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3sSCsz2ohxNRC2NGdIBWLoZM_j4YSeiXUVwFghDQxC1nPPIQX)

Simples, iremos utilizar medida de distância para identificar a distância existente entre o ponto P1 e os demais pontos do meu dataset, como K=1 o algoritmo irá verificar ponto a ponto, caso coloque o valor K=3 ele ira olhar a distância de P1 em relação a 3 pontos. Desta forma termos e distância existente entre P1 e todos os pontos do meu dataset, assim conseguiremos saber a quais pontos P1 é mais próximo, desta forma teremos qual classe ele é mais similar. Assim a “votação” será concluída, e saberemos como classificar P1.

#### Para encontrarmos a distância entre os pontos poderemos utilizar as seguintes medidas

1. Distância Euclidiana
2. Distância de Hamming
3. Distância Manhattan
4. Distância de Markowski

##### Os passos realizados pelo algoritmo são

1. Calcular a distância
2. Encontrar os pontos/vizinhos mais próximos
3. Votar a label para o ponto a ser previsto

![XHTML válido](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1531424125/KNN_final1_ibdm8a.png)

## Getting Started

As dependências desse projeto são:

* **sklearn** - <https://scikit-learn.org/stable/>
* **pandas** - <https://pandas.pydata.org/>

### Installing

Install "nome" with pip (Latest version):

```bash
pip install pandas
```

```bash
pip install sklearn
```

## Authors

* **Horacio Biancardi** - *Initial work*

## License

O projeto é licenciado para Horacio Biancardi
