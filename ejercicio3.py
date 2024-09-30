horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
tarifa_hora = float(input("Ingrese la tarifa por hora: "))
antiguedad_anios = int(input("Ingrese los años de antigüedad en la empresa: "))
total_ventas = float(input("Ingrese el total de ventas realizadas (si aplica): "))

salario_base = horas_trabajadas * tarifa_hora

if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        salario_base += horas_extras * (tarifa_hora * 1.5)

if antiguedad_anios >= 5:
        bono_antiguedad = 0.05 * salario_base

else:
        bono_antiguedad = 0

if total_ventas > 1000:
        comision_ventas = 0.02 * (total_ventas - 1000)
else:
        comision_ventas = 0

salario_bruto = salario_base + bono_antiguedad + comision_ventas

if salario_bruto <= 1000:
        descuento = 0.1 * salario_bruto
elif salario_bruto <= 2000:
        descuento = 0.1 * 1000 + 0.05 * (salario_bruto - 1000)
else:
        descuento = 0.1 * 1000 + 0.05 * 1000 + 0.03 * (salario_bruto - 2000)

salario_neto = salario_bruto - descuento

print("\nResumen del salario:")
print(f"Salario base: ${salario_base:.2f}")
print(f"Bono por antigüedad: ${bono_antiguedad:.2f}")
print(f"Comisión por ventas: ${comision_ventas:.2f}")
print(f"Descuentos: ${descuento:.2f}")
print(f"Salario neto final: ${salario_neto:.2f}")
