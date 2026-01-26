print("Calcular salario trabajador")
horas = int(input("Horas trabajadas: "))
importe_hora = int(input("Importe hora: "))
km = int(input("Kilometros viajados: "))
horas_extra = 0
salario_base = 0
salario_extra = 0
salario_final = 0
dieta = ""
retencion = ""
iva = 0
if (horas > 36):
    horas_extra = horas - 36
    salario_base = importe_hora * 36
    salario_extra = (importe_hora + 1.5) * horas_extra
else:
    horas_extra = 0
    salario_extra = 0
    salario_base = importe_hora * horas
if (km > 101 and km < 900):
    dieta = "NACIONAL"
elif (km > 900):
    dieta = "INTERNACIONAL"
else:
    dieta = "PROVINCIAL"
salario_final = salario_base + salario_extra
if (salario_final <= 250):
    retencion = "0%"
elif (salario_final > 250 and salario_final <= 500):
    retencion = "20%"
else:
    retencion = "50%"
iva = salario_final * 0.16
salario_neto = salario_final - iva
print("HORAS TRABAJADAS....", horas)
print("IMPORTE HORA.....", importe_hora)
print("KILOMETROS.....", km)
print("Dietas....", dieta)
print("Retencion.....", retencion)
print("Horas extra....", horas_extra)
print("SALARIO BASE.....", salario_base)
print("Salario EXTRA....", salario_extra)
print("Salario Bruto....", salario_neto)
print("Iva: ", iva)
print("Salario final.....", salario_final)

    
    