func_1 = 1000
func_2 = 770
func_3 = 2700

lucro_1 = 0
lucro_2 = 0
lucro_3 = 0

meta = 1000

if func_1 >= 1000 and func_1 <= 1999:
    lucro_1 = 0.10
elif func_1 >= 2000:
    lucro_1 = 0.15
else:
    lucro = 0

comissao1 = func_1 * lucro_1

if func_2 >= 1000 and func_2 <= 1999:
    lucro_2 = 0.10
elif func_2 >= 2000:
    lucro_2 = 0.15
else:
    lucro = 0

comissao2 = func_2 * lucro_2

if func_3 >= 1000 and func_3 <= 1999:
    lucro_3 = 0.10
elif func_3 >= 2000:
    lucro_3 = 0.15
else:
    lucro = 0

comissao3 = func_3 * lucro_3

print(f"O funcionário 1 receberá: {comissao1}.\nO funcionário 2 receberá: {comissao2}.\nO funcionário 3 receberá: {comissao3}")

