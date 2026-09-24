print("Sistema Especialista para Diagnóstico de Problemas em Computadores")

print("\nResponda às perguntas utilizando s para SIM ou n para NÃO.")

liga = input("\nO computador liga? (s/n): ").lower()

if liga == "n":
    energia = input("Existe algum sinal de energia? (s/n): ").lower()

    if energia == "n":
        print("\nDiagnóstico: possível problema na fonte de alimentação.")
        print("Recomendação: verificar cabo de energia e fonte.")

    else:
        print("\nDiagnóstico: possível falha na inicialização.")
        print("Recomendação: procurar assistência técnica.")

else:
    video = input("O computador apresenta imagem? (s/n): ").lower()

    if video == "n":
        print("\nDiagnóstico: possível problema na memória RAM ou cabo de vídeo.")
        print("Recomendação: verificar a memória RAM e os cabos de vídeo.")

    else:
        lento = input("O computador está muito lento? (s/n): ").lower()

        if lento == "s":
            print("\nDiagnóstico: possível problema de armazenamento ou memória.")
            print("Recomendação: verificar espaço de armazenamento e memória RAM.")

        else:
            print("\nDiagnóstico: nenhum problema específico identificado.")

print("\nDiagnóstico finalizado.")
