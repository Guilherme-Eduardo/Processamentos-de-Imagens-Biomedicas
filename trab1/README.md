
# Trabalho 1 - Disciplina de Processamento de Imagens Biomédicas

Professor: Lucas Ferrari

Aluno: Guilherme Eduardo Gonçalves da Silva

GRR20231950

## Requisitos

(OPCIONAL): Criação de um ambiente virtual:
```python3 -m venv -my-venv```

Instalação de bibliotecas do python:
```pip install numpy matplotlib scikit-learn```

Executar script com:
```python3 script.py > resultados.txt``` 

ou 

```python3 script.py```

Isso fará com que o script gere as imagens e os resultados dos cálculos solicitados.

O arquivo com as conclusões/considerações dos resultados estão em ```conclusoes.md```


## Enunciado

Você está trabalhando em um empresa de imagens biológicas que faz análises com microscópio. O seu supervisor te entregou três arquivos texto (compactados) com as análises de uma rede neural (Yolov4) que detecta células nas imagens. Os nomes dos arquivos estão no padrão: XYZ_Yolov4_5000_dados_celulas.txt, onde XYZ é o tamanho da imagem testada, neste caso 512, 608 e 800. O 5000 se refere a época de treinamento.

O arquivo contém informações de detecção com diversos thresholds, a informação está nas linhas com o formato:  " for conf_thresh = 0.00, TP = 265, FP = 123, FN = 6, average IoU = 52.99 %", por exemplo. Nesta linha está indicado o threshold aplicado 0.0%, a quantidade de verdadeiros positivos, falsos positivos e verdadeiros negativos para o threshold escolhido. Os valores de threshold variam de 0.0 até 0.95 Seu trabalho é montar um script que extraia as informações dos três arquivos e calcule as métricas Sensibilidade/Recall, Precisão e F1-Score  e gere um gráfico Precision-Recall para cada um dos tamanhos das imagens e calcule o AUC. Faça um arquivo texto com a indicação de qual dos tamanhos de imagem e threshold devem ser escolhidos e, sucintamente, descreva o porquê. 

A entrega final é um arquivo compactado com o script para interpretar o arquivo texto e fazer os cálculos solicitados, os três arquivos com os gráficos de cada tamanho de imagem e o arquivo texto com a indicação do melhor tamanho de imagem e threshold. Não esqueça de indicar como utilizar o seu script.

Neste site tem uma descrição das curvas ROC, curva Precision-Recall e AUC:

Link: https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/


