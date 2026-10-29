# Desafio Nível 1 — PDV com Descontos (Python)

## O que o código faz

Este projeto implementa a lógica de um sistema de Ponto de Venda (PDV) em Python puro, sem o uso de bibliotecas externas, que calcula descontos progressivos para clientes de uma loja, farmácia ou supermercado. O sistema processa múltiplas vendas em sequência, aplicando descontos automáticos baseados na idade do cliente e no valor da compra, valida entradas negativas e, ao encerrar o expediente, exibe o resumo financeiro consolidado do dia.

## Como ele faz (Passo a Passo)

1. **Inicialização do histórico**: Cria uma lista vazia (`historico_compras`) para armazenar todas as vendas válidas realizadas no dia.
2. **Loop de atendimento**: Inicia um laço de repetição (`while True`) que permite registrar várias compras seguidas até que o operador digite `0` no valor da compra.
3. **Leitura e validação de entradas**: Recebe o valor da compra (`float`) e a idade do cliente (`int`). Caso qualquer um dos valores seja negativo, exibe um aviso na tela e reinicia o ciclo (`if` + `continue`) pedindo os dados novamente.
4. **Regra 1 (Desconto por idade)**: Verifica se a idade do cliente é maior ou igual a 65 anos (`idade >= 65`). Se verdadeiro, aplica 20% de desconto sobre o valor original.
5. **Regra 2 (Desconto por valor)**: Verifica se o valor **já com o desconto de idade aplicado** é estritamente maior que R$ 100,00 (`valor_com_desconto > 100`). Se verdadeiro, aplica um desconto extra de 10% sobre esse valor atualizado.
6. **Exibição e registro**: Mostra no console o valor final da compra formatado em reais (`R$ 0.00`) e adiciona os dados da venda (`valor_original`, `idade`, `desconto_concedido`, `valor_com_desconto`) na lista `historico_compras` utilizando o método `.append()`.
7. **Fechamento de caixa (Resumo do Dia)**: Quando o usuário digita `0`, o programa encerra o loop, percorre a lista de compras com um laço `for` para somar os totais e exibe:
   - Quantidade de compras registradas;
   - Total bruto (soma dos valores originais);
   - Total de descontos concedidos;
   - Total final (soma dos valores com desconto).

## Como rodar

No terminal, dentro da pasta `nivel_1`, execute o comando:

```bash
python pdv.py
```

## Tabela de exemplos (Casos de Teste)

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |
