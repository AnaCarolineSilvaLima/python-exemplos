import random
alunos=["João", "Maria", "Pedro", "Ana", "Luicas", "Mariana"]
print(f"Lista: {alunos}")
# Embaralhar a Lista
random.shuffle(alunos)
print(f"Lista embaralhada: {alunos}")
# Ordenar a Lista Crescente 
alunos.sort()
print(f"Lista crescente: {alunos}")
# Ordena e Lista Decrescente
alunos.sort(reverse=True)
print(f"Lista Decrescente:Ç {alunos}")
