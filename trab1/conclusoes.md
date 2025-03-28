# Trabalho 1 para a disciplina de Processamento de Imagens Biomédicas

Professor: Lucas Ferrari

Aluno: Guilherme Eduardo Gonçalves da Silva

GRR20231950

## Resultados

### Saída gerada:

Resultados Finais:

- Melhor AP: **0.1560419229962485**
- Melhor tamanho de imagem em relação ao AP: **Modelos/512_yolov4_5000_dados_celulas.txt**
- Melhor tamanho de imagem baseado em F1-score: **0.8859813084112149** em **Modelos/800_yolov4_5000_dados_celulas.txt** - Threshold: **0.75**

## Conclusões

Conforme os resultados obtidos por meio do script e dos gráficos de Precision-Recall, observa-se que o melhor tamanho da imagem foi de 800, pois com um valor de threshold de 0.75, obteve um F1-score próximo de 0.886, que significa que nesse ponto houve um equilíbrio entre precision e recall superior aos demais valores.

A curva de Precision-Recall é uma medida útil para comparar o desempenho da classe positiva quando os dados estão desequilibrados [1]. Além disso, se importa menos com a classe negativa frequente [2]. Uma pontuação de 1.0 representa um modelo com habilidade perfeita.

A análise da melhor imagem depende de como os nossos dados estão suportados (equilibrados ou desequilibrados).

Podemos realizar o cálculo de AP(Average Precision), o qual é um resumo da curva de precisão-recall (PR) em um único valor que representa a média de todas as precisões [1]. Os valores variam de 0 até 1, ou seja, quanto maior a métrica, melhor o desempenho do modelo em diferentes limites.

Porém, os valores de AP calculados foram abaixos, o qual podem indicar baixo número de thresholds, desequilíbrio de classes, entre outros fatores.

Portanto, as imagens de tamanho 800 com threshold de 0.75 são as mais indicadas, pois apresentou melhores valores de equilibrio entre Precision-Recall.



Referência:
[1] - https://docs.kolena.com/metrics/average-precision/#:~:text=Average%20precision%20(AP)%20summarizes%20a,and%20AP%20scores%20of%201.


