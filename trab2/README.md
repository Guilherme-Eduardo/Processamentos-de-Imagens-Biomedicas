
# Trabalho 2 (Introdução) - Disciplina de Processamento de Imagens Biomédicas

Professor: Lucas Ferrari

Aluno: Guilherme Eduardo Gonçalves da Silva

GRR20231950

## Requisitos

A pasta das Imagens (Train/) precisa estar na raiz do projeto

Criação de um ambiente virtual:
```python3 -m venv -my-venv```

Instalação de bibliotecas do python:
```pip install -r requirements.txt ``

Executar o código com:
```python3 main.py`` 



A saída criará um arquivo "Resultados.txt" com os valores de sensibilidade, especificidade e matriz de confusão dos 4 métodos utilizados

## Enunciado

Para realizar esse trabalho faça o download da base siim_small vista em aula.

  ```wget -c https://s3.amazonaws.com/fast-ai-imagelocal/siim_small.tgz```

Os arquivos Pneumothorax_files.txt e No_Pneumothorax_files.txt possuem uma lista de 15 arquivos de cada uma das classes (Pneumothorax e No Pneumothorax). A ideia é você construir um classificador que receba uma das imagens de teste e compare com as outras 29 restantes. Repita esse processo para as 30 imagens até que todas tenham sido utilizadas para teste. Calcule a matriz de confusão, a sensibilidade e a especificidade para cada um dos 4 métodos abaixo implementados no OpenCV:

- CV_COMP_CORREL Correlation
- CV_COMP_CHISQR Chi-Square
- CV_COMP_INTERSECT Intersection
- CV_COMP_BHATTACHARYYA Bhattacharyya distance


Considere a classe Pneumothorax como positiva e a outra Negativa, portanto se a imagem é de Pneumothorax e método indicou a outra classe será considerado um Falso Negativo.
Entregar um arquivo compactado com o programa fonte, um arquivo texto com as métricas e a matriz de confusão de cada método e um Readme com instruções para execução do programa. Utilizar o caminho parcial das imagens descritos nos arquivos.
OBS: NÃO É NECESSÁRIO ENVIAR AS IMAGENS!!