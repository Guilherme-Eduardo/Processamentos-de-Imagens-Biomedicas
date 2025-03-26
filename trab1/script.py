####################################################################################

# Trabalho 1 para a disciplina de Processamento de Imagens Biomédicas
# Professor: Lucas Ferrari
# Aluno: Guilherme Eduardo Gonçalves da Silva
# GRR20231950

####################################################################################

import os
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import auc


# Função para extrair informações de uma linha do arquivo
# Armazenadas em um dicionário
def data_extraction(line):
    data = {}
    line = line.strip()
    parts = line.split(",")
    for part in parts:
        if "=" in part:
            chave, valor = part.split("=", 1)
            chave = chave.strip()
            valor = valor.strip().replace("%", "")
            data[chave] = valor
    return data

# Função que converte os valores de string para float
def text_to_float(data):
    for key, value in data.items():
        data[key] = float(value)
    return data

# Função responsável por realizar os cálculos de métricas
def calc(data, thresholds, sensi, precision, F1_score):
    tp = data["TP"]
    fn = data["FN"]
    fp = data["FP"]

    #Calculos para geração do grafico
    sensibility = tp / (tp + fn)
    prec = tp / (tp + fp)
    f1 = 2 * ((prec * sensibility) / (prec + sensibility))

    #Imprime os calculos para serem jogadas na STDOUT
    print_values(data["for conf_thresh"], sensibility, prec, f1, tp, fn, fp)

    #Inserindo os valores nos vetores
    thresholds.append(data["for conf_thresh"])
    sensi.append(sensibility)
    precision.append(prec)
    F1_score.append(f1)

def print_values (threshold, sensi, precision, F1_score, tp, fn, fp):
    print (f"Threshold: {threshold}")
    print (f"Sensibility/Recall: {tp} / ({tp} + {fn}) = {sensi}")
    print (f"Precision: {tp} / ({tp} + {fp}) {precision}")
    print (f"F1-score: 2 * ({precision} * {sensi} / {precision} + {sensi}) = {F1_score}")


# Função para geração dos graficos
def generate_graph(sensi, precision, size_image ):

    name = f"Grafico_Precision_Recall_{size_image}.png"
    
    # Calcula o AUC para a curva Precision-Recall
    auc_value = auc(sensi, precision)

    plt.figure()    
    plt.plot(sensi, precision, 'o-', label='Curva Precision-Recall')
    plt.xlabel('Recall (Sensibilidade)')
    plt.ylabel('Precision (Precisão)')
    plt.title(f"Gráfico Precision-Recall - AUC = {auc_value}")
    plt.legend(loc='best')    
    plt.savefig(name)
        
    return auc_value

####################################################################################

def main():
    files_name = [
        os.path.join("Modelos", "512_yolov4_5000_dados_celulas.txt"),
        os.path.join("Modelos", "608_yolov4_5000_dados_celulas.txt"),
        os.path.join("Modelos", "800_yolov4_5000_dados_celulas.txt")
    ]

    size_image = [512,608,800]
    count = 0
    token = "conf_thresh"
    max_auc = 0
    max_f1 = 0
    best_threshold = 0
    best_image_auc = ""
    best_image_f1 = ""
    best_current_f1 = 0
    best_current_threshold = 0

    # Vetores para armazenar os resultados
    thresholds = []
    sensi = []
    precision = []
    F1_score = []

    # Laço para repetir o processo em todos os arquivos
    for file_name in files_name:
        with open(file_name, 'r') as file:
            print (f"Extraindo informações do arquivo: {file_name}")
            for line in file:
                if token in line:
                    data = data_extraction(line)
                    converted_data = text_to_float(data)
                    calc(converted_data, thresholds, sensi, precision, F1_score)

                    #Resgata o melhor valor de F1-score para a imagem atual
                    if F1_score[-1] > best_current_f1:
                        best_current_f1 = F1_score[-1]
                        best_current_threshold = thresholds[-1]

                    #Resgata o melhor valor de F1-score para todas as imagens
                    if F1_score[-1] > max_f1:
                        max_f1 = F1_score[-1]
                        best_threshold = thresholds[-1]
                        best_image_f1 = file_name

        auc = generate_graph(sensi, precision, size_image[count])
        if auc > max_auc:
            max_auc = auc
            best_image_auc = file_name

        count += 1
        thresholds.clear()
        sensi.clear()
        precision.clear()
        F1_score.clear()  
        print("")
        print (f"Melhor resultado - threshold: {best_current_threshold} -  F1-Score: {best_current_f1}")
        print (f"AUC: {auc}\n")  
        print (100 * "*")
        print ("")
        best_current_f1 = 0
        best_current_threshold = 0

    #Conclusão dos resultados
    print("\nResultados Finais:")
    print(f"Melhor AUC: {max_auc}")
    print(f"Melhor tamanho de imagem em relação ao AUC: {best_image_auc}")
    print(f"Melhor tamanho de imagem baseado em F1-score: {max_f1} em {best_image_f1} - Threshold: {best_threshold}")
    
if __name__ == "__main__":
    main()
