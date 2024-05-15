def remover_itens_estoque(inventario, quantidade_minima):
  inventario_atualizado = {item: quantidade for item, quantidade in inventario.items() if quantidade >= quantidade_minima}
  return inventario_atualizado

inventario = {"mouse": 26, "monitor": 13, "Pendrive": 83, "teclado": 5, "fone de ouvido": 40}
quantidade_minima = 10

inventario_atualizado = remover_itens_estoque(inventario, quantidade_minima)

print("Inventário atualizado:")
print(inventario_atualizado)
