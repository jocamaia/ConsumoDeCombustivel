
#CALCULANDO A MÉDIA DE VIAGEM:
print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print('## CALCULANDO A MÉDIA DE VIAGEM ##')
print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')

#QUANTOS KM/L O CARRO FAZ:
km_l= float(input("Digite o consumo do veiculo em litros : "))


#INFORME QUANTAS HORAS É A VIAGEM:
hora= float(input('Digite a quantidade de hora que foi a viagem: '))

#INFORME A VELOCIADE DO VEICULO NO TRAJETO:
km_h= int(input('Digite a média da velocidade do veiculo na viagem: '))

#CALCULAR (HORA*KM_H)/KM_L :
calculo= (hora*km_h)/km_l

#VALOR DA GASOLIMA
gasolina= float(input("DIGITE O PREÇO DO COMBUSTIVEL: "))

#CALCULO DE QUANTO GASTOU EM R$:
pagar= calculo*gasolina

print ('seu gasto é:''%.3f'% calculo,'LITROS' )
print('seu gasto em R$:','%.2f'% pagar)







print ('------------------------------------')
print ('////////////////////////////////////')
print ('            NOTA FISCAL             ')
print ('Posto Setta CNPJ: 03.028.906/0001-02')
print ('AV Desenbargador Santos 22 Centro PB')
print ('Código    Descrição               Qtde UN V1 Unit  V1 Iten ')
print ("320102002 Gasolina V-POVER Bico   30   L   7 160 ",   "%.2f"%    pagar  )
print ('Qtde. total de itens                                    1')
print (" Valor total (R$) ",                                    "%.2f"% pagar)
print ('Valor a Pagar  (R$)',                                "%.2f"%    pagar)
print ('FORMA DE PAGAMENTO                                    VALOR PAGO (R$)')
print ('QR LINX - PIX',                                       "%.2F"%       pagar  )
print ('               Consulte pela chave de acesso em  ')
print ('       http://hongo logação.sefaz.es.gov.br/ConsultaNFCe')
print ('CONSUMIDOR-')
print ('            ///////////////////// 27/03/2023 21:04 ')
