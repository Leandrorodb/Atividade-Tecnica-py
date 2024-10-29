# Verificar a existência da letra 'a' e contar suas ocorrências
def contar_a(s):
    return s.lower().count('a')

# String a ser verificada
texto = input("Informe uma string para verificar a letra 'a': ")

# Contagem
quantidade_a = contar_a(texto)
print(f"A letra 'a' (ou 'A') aparece {quantidade_a} vezes na string.")
