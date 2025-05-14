
# 🏃‍♂️ Projeto: Sistema de Atletas (OOP em Python)

Este projeto demonstra os conceitos de Programação Orientada a Objetos (POO) em Python, usando uma hierarquia de classes para representar diferentes tipos de atletas: **Corredores**, **Nadadores**, **Ciclistas** e o **TriAtleta**, que combina as três modalidades.

## 🧠 Conceitos Aplicados

- Herança
- Herança múltipla
- Polimorfismo
- Encapsulamento
- Uso de `super()`

## 📦 Estrutura das Classes

### `Atleta` (Classe base)
- Atributos:
  - `nome`
  - `aposentado` (booleano)
  - `aquecimento` (booleano)
- Métodos:
  - `Aquecer()`: Simula o aquecimento do atleta.
  - `Aposentar()`: Marca o atleta como aposentado.

### `Corredor`, `Nadador`, `Ciclista` (Subclasses)
Cada classe herda de `Atleta` e implementa um método específico:
- `correr()` — para `Corredor`
- `nadar()` — para `Nadador`
- `ciclismo()` — para `Ciclista`

Esses métodos verificam:
- Se o atleta está aposentado
- Se o atleta está aquecido
- E então executam a ação correta

### `TriAtleta`
Herda de `Corredor`, `Nadador` e `Ciclista`, representando um atleta que pratica as três modalidades. Com isso, pode acessar todos os métodos herdados (`correr`, `nadar`, `ciclismo`).

## ✅ Exemplo de Uso

```python
atleta1 = TriAtleta("João")

atleta1.correr()       # Deve pedir para aquecer
atleta1.Aquecer()      # Atleta se aquece
atleta1.nadar()        # Pode nadar
atleta1.Aposentar()    # Atleta se aposenta
atleta1.ciclismo()     # Não pode competir após aposentar
```

## 📚 Requisitos
- Python 3.x

## 🤝 Contribuição
Wesley Luiz Moreira da Silva
Paulo Rafael Brandão Santos
