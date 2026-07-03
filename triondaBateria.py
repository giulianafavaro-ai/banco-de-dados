# Definindo as variáveis para teste (você pode alterar os valores abaixo)
bateria_atual = 10
bola_em_jogo = True

# Processamento das condições
if bateria_atual < 15 and bola_em_jogo == True:
    # Condição 1
    print("ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação.")

elif bateria_atual < 15 and bola_em_jogo == False:
    # Condição 2
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")

else:
    # Condição 3 (Caso Geral: bateria >= 15)
    print("Sistema Trionda operando normalmente. Bateria ok.")
