import matplotlib.pyplot as plt
import numpy as np
from pydicom import dcmread
import cv2
import math


def convert (data):
    # Leio o arquivo DICOM
    ds = dcmread (all_data[i])

    #Extrai as informações (pixels)
    current_data = ds.pixel_array
    
    return current_data


def normalize_data (data):
    current_data = cv2.calcHist ([data], [0], None, [256], [0,256])

    cdf = current_data.cumsum()
    current_normalized = cdf * current_data.max() / cdf.max()
    
    # Normaliza o histograma
    #hist = cv2.normalize(hist, hist).flatten()
    return current_normalized

# Carrega os arquivos para leitura
with open("No_Pneumothorax_files.txt", "r") as arquivo:
    no_pneumothorax = arquivo.read().splitlines()

with open("Pneumothorax_files.txt", "r") as arquivo:
    pneumothorax = arquivo.read().splitlines()

#Concatena os 2 arquivos em um único array
all_data = no_pneumothorax + pneumothorax

#Inicialização de variáveis
best_correl = 0
sensibility = 0
precision = 0 


for i in range(len(all_data)):
    current_data = convert(all_data[i])	
    current_normalized = normalize_data(current_data)

    for j in range(len(all_data)):
        if i == j:
            continue
        
        compare_data = convert(all_data[j])
        data_normalized = normalize_data(compare_data)
        
        # Correlação usando HISTCMP_CORREL
        current_correl = cv2.compareHist(current_normalized, data_normalized, cv2.HISTCMP_CORREL)
        
        # Verifica a correlação entre a classe
        if current_correl > best_correl:
            best_correl = current_correl
    

	


