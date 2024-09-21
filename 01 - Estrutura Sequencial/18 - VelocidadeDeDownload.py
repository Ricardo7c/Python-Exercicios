# Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('Digite o tamanho do arquivo em MBs: '))
velocidade = float(input('Digite a velocidade da internet em Mbps: '))
internet = velocidade/8
tempo_segundos = arquivo/internet
tempo_minutos = tempo_segundos/60
print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")