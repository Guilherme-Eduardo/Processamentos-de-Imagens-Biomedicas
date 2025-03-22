
# Trabalho 1 para a disciplina de Processamento de Imagens Biomédicas

Professor: Lucas Ferrari

Aluno: Guilherme Eduardo Gonçalves da Silva

GRR20231950

## Resultados

### Saída gerada:
Resultados Finais:

- Melhor AUC: **0.15933919569563806**
- Melhor tamanho de imagem em relação ao AUC: **Modelos/512_yolov4_5000_dados_celulas.txt**
- Melhor tamanho de imagem baseado em F1-score: **0.8859813084112149** em **Modelos/800_yolov4_5000_dados_celulas.txt** - Threshold: **0.75**

## Conclusões

Conforme os resultados obtidos por meio do script e dos gráficos de Precision-Recall, observa-se que o melhor tamanho da imagem foi de 800, pois com um valor de threshold de 0.75, obteve um F1-score próximo de 0.886, que significa que nesse ponto houve um equilíbrio entre precision e recall superior aos demais valores.

Um fato curioso é que a imagem 800 apresentou um valor de AUC PR (Área sob a curva - Precision/Recall) igual a 0.1476183345937469. Dessa forma, sendo o segundo valor entre as três imagens.

A AUC PR é uma medida útil para comparar o desempenho da classe positiva quando os dados estão desequilibrados ([1]). Além disso, se importa menos com a classe negativa frequente. Uma pontuação de 1.0 representa um modelo com habilidade perfeita.

A análise da melhor imagem depende de como os nossos dados estão suportados (equilibrados ou desequilibrados), porém não podemos afirmar se está desequilibrado, pois está faltando o número de TN (Verdadeiro Negativo).

Os baixos valores de AUC PR podem indicar baixo número de thresholds, desequilíbrio de classes, entre outros.

Portanto,  se o critério for o equilíbrio entre precisão e recall, as imagens de tamanho 800 com threshold de 0.75 são as mais indicadas; se o critério for a performance global medida pelo AUC PR, as imagens de tamanho 512 apresentam uma leve vantagem.

OBS: AUC ROC = Dados mais equilibrados
     AUC PR = Dados mais desequilibrados[1]



Referência:
[1] - https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc?hl=pt-br#:~:text=modelo%20hipot%C3%A9tico%20perfeito.-,%C3%81rea%20sob%20a%20curva%20(AUC),classificar%C3%A1%20positivo%20maior%20que%20negativo.

https://neptune.ai/blog/f1-score-accuracy-roc-auc-pr-auc

