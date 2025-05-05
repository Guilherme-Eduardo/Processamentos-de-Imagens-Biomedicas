# Guilherme Eduardo Gonçalves da Silva
# GRR20231950
# Trabalho de Introdução
# Processamento de Imagens Biomédicas


import matplotlib.pyplot as plt
import numpy as np
from pydicom import dcmread
import cv2
import math
import os


def convert (data):
    # Lendo o arquivo DICOM
    ds = dcmread (data)

    #Extrai as informações (pixels)
    current_data = ds.pixel_array
    
    return current_data


def normalize_data (data):
    hist = cv2.calcHist ([data], [0], None, [256], [0,256])

    #cdf = current_data.cumsum()
    #main_normalized = cdf * current_data.max() / cdf.max()
    
    # Normaliza o histograma
    hist = cv2.normalize(hist, hist).flatten()
    return hist



def main ():
    # Carrega os arquivos para leitura
    with open("No_Pneumothorax_files.txt", "r") as arquivo:
        no_pneumothorax = [line.strip() for line in arquivo if line.strip()]

    with open("Pneumothorax_files.txt", "r") as arquivo:
        pneumothorax = [line.strip() for line in arquivo if line.strip()]

    #Concatena os 2 arquivos em um único array
    all_data = pneumothorax + no_pneumothorax


    # Vetor com a classe real dados (1 = pos / 0 = neg)
    all_labels = []
    for path in pneumothorax:
        all_labels.append(1)
    for path in no_pneumothorax:
        all_labels.append(0)
    
    # Dicionário de métodos com os tipos de correlações
    methods = {
        "CORREL": cv2.HISTCMP_CORREL,
        "CHISQR": cv2.HISTCMP_CHISQR,
        "INTERSECT": cv2.HISTCMP_INTERSECT,
        "BHATTACHARYYA": cv2.HISTCMP_BHATTACHARYYA
    }

    # Vetores de 4 posição. Cada posição representa um metodo que será incrementado
    tp = [0] * 4
    tn = [0] * 4
    fp = [0] * 4
    fn = [0] * 4

    for i in range(len(all_data)):
        main_data = convert(all_data[i])	
        main_normalized = normalize_data(main_data)
        main_class = all_labels[i]

        for method_index, (method_name, method_code) in enumerate(methods.items()):
            if method_code in [cv2.HISTCMP_CORREL, cv2.HISTCMP_INTERSECT]:
                best_score = -1
            else:
                best_score = float('inf') # Valor infinito (P/ CHISQR e BHATTACHARYYA). Para esses métodos, valor negativo é melhor
            predicted_class = -1

            for j in range(len(all_data)):
                if i == j:
                    continue              # Não compara com ele mesmo
                #Dados que iremos realizar a comparação com o dado principal do laço
                second_data = convert(all_data[j])
                data_normalized = normalize_data(second_data)
                data_class = all_labels[j]
                
                # Correlação usando CORREL, CHISQR CHI SQUARE, INTERSECT INTERSECTION e BHATTACHARYYA Bhattacharyya distance
                score = cv2.compareHist(main_normalized, data_normalized, method_code) # method_code = dicionario -> valor das correlações

                # Lógica depende do tipo de métrica
                if method_code in [cv2.HISTCMP_CORREL, cv2.HISTCMP_INTERSECT]:
                    # Se o score do segundo dado for maior, o predict da classe será baseado na sua propria classe (second_data -> j)
                    if score > best_score:
                        best_score = score
                        predicted_class = data_class
                else:
                    if score < best_score:
                        best_score = score
                        predicted_class = data_class
            # Realiza a comparação das métricas (Correlações)
            if predicted_class == 1 and main_class == 1:    #Verdadeiro Positivo
                tp[method_index] += 1
            elif predicted_class == 1 and main_class == 0:  # Falso Positivo
                fp[method_index] += 1
            elif predicted_class == 0 and main_class == 1:  # Falso Negativo
                fn[method_index] += 1
            elif predicted_class == 0 and main_class == 0:  # Verdadeiro Negativo
                tn[method_index] += 1
    
    #calcula sensibilidade
    #calcula especificada
    #Saida na matriz de confusao
    #Joga a saída no arquivo de resultados
    with open ("Resultados.txt",  'a') as results:
        for i, method_name in enumerate(methods.keys()):        
            sensibility = tp[i] / (tp[i] + fn[i])
            specificity = tn[i] / (tn[i] + fp[i])     

            results.write(f"\n{method_name}\n")
            results.write(f"TP = {tp[i]}, FP = {fp[i]}, FN = {fn[i]}, TN = {tn[i]}\n")
            results.write(f"Sensibilidade (Recall): {sensibility:.2f}\n")
            results.write(f"Especificidade: {specificity:.2f}\n")        
            results.write("\nMatriz de Confusão:\n")
            results.write(f"          Previsto\n")
            results.write(f"         |  1  |  0 \n")
            results.write(f"   ------|----------\n")
            results.write(f"   Real 1| {tp[i]:3} | {fn[i]:3}\n")
            results.write(f"   Real 0| {fp[i]:3} | {tn[i]:3}\n")
            results.write("\n")
            results.write(100*"#")
        

if __name__ == "__main__":
    main()



