itens = [
  {"nome": "caneta", "valor": 70.0, "estoque": 200},
  {"nome": "lápis", "valor": 0.80, "estoque": 47},
  {"nome": "caderno", "valor": 80.0, "estoque": 100},
  {"nome": "borracha", "valor": 1.20, "estoque": 60}
]

itens_em_promocao = []

for item in itens:
  if item["valor"] > 60.0 and item["estoque"] > 50:
      novo_valor = item["valor"] * 0.8
      item_em_promocao = {
          "nome": item["nome"],
          "valor": (item["valor"], novo_valor),
          "estoque": item["estoque"]
      }
      itens_em_promocao.append(item_em_promocao)

for item in itens_em_promocao:
  print(item)