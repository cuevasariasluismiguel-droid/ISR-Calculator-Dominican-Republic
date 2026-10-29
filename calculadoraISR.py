
salario_mensual = float(input("Ingrese su salario mensual: "))

salario_anual = salario_mensual * 12

if salario_anual <= 416220:
    isr_anual = 0

elif salario_anual <= 624329:
    isr_anual = (salario_anual - 416220) * 0.15

elif salario_anual <= 867123:
    isr_anual = 31216 + (salario_anual - 624329) * 0.20

else:
    isr_anual = 79776 + (salario_anual - 867123) * 0.25

isr_mensual = isr_anual / 12

print("\n--- RESULTADO DEL ISR ---")
print(f"Salario bruto mensual: RD$ {salario_mensual:,.2f}")
print(f"Salario bruto anual: RD$ {salario_anual:,.2f}")
print(f"ISR anual: RD$ {isr_anual:,.2f}")
print(f"ISR mensual estimado: RD$ {isr_mensual:,.2f}")
print(f"Salario neto mensual: RD$ {salario_mensual - isr_mensual:,.2f}")
print(f"Salario neto anual: RD$ {salario_anual - isr_anual:,.2f}")