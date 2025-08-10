# Mini-Raid: Sistema de Recuperação de Dados com RAID Simplificado 🛡️💾

Mini-Raid é um projeto educacional que demonstra os princípios básicos de redundância e recuperação de dados usando conceitos de RAID (Redundant Array of Independent Disks). O sistema usa operações XOR para calcular paridade e recuperar dados perdidos ou corrompidos.

## 🔍 Funcionalidades Principais

- **Cálculo de Paridade**: Gera dados de redundância usando XOR entre três arquivos
- **Recuperação Automática**: Detecta e recupera arquivos perdidos ou corrompidos
- **Sistema Autocontido**: Tudo em um único script Python sem dependências externas
- **Interatividade**: Permite simular falhas e ver a recuperação em tempo real

## ⚙️ Como Funciona

O sistema implementa um conceito simplificado de RAID que usa paridade distribuída:

```
p1 (dados) ⊕ p2 (dados) ⊕ p3 (dados) = paridade
```

Quando um arquivo é perdido, ele pode ser recuperado usando:
```
arquivo_perdido = arquivo1 ⊕ arquivo2 ⊕ paridade
```

## 🚀 Como Usar

### Pré-requisitos
- Python 3.x instalado

### Passo a Passo

1. **Preparar os arquivos de dados**:
   ```bash
   echo "011101000110001101101000011000010111010100101100001000000111010001100101001000000111011001100101011010100110111100100000011001000110010101110000011011110110100101110011" > parte1.txt
   echo "01101111 01101100 01100001 00101100 00100000 01110100 01110101 01100100 01101111 00100000 01100010 01100101 01101101 00100000 01100011 01101111 01101110 01110100 01101001 01100111 01101111" > parte2.txt
   echo "01101111 01101001 01100101 00100000 01110110 01101111 01100011 11000011 10101010 00100000 11000011 10101001 00100000 01101111 00100000 01100110 01100001 01101101 01101111 01110011 01101111" > parte3.txt
   ```

2. **Executar o sistema**:
   ```bash
   python Mini-Raid.py
   ```

3. **Seguir as instruções**:
   ```
   Calculando paridade....
   paridade calculada

   Tudo pronto, se quiser pode testar
   apagando um arquivo e tocando em <ENTER>
   ```

4. **Simular falha** (opcional):
   - Apague um dos arquivos (`parte1.txt`, `parte2.txt` ou `parte3.txt`)
   - Pressione ENTER para iniciar a recuperação

5. **Verificar resultados**:
   - O sistema detectará o arquivo faltante
   - Recuperará o conteúdo usando a paridade
   - Recriará o arquivo automaticamente

## 🧠 Conceitos Técnicos

- **Paridade XOR**: Método eficiente para cálculo de redundância
- **RAID Nível 5 Adaptado**: Princípio de paridade distribuída simplificado
- **Recuperação de Dados**: Algoritmo que reconstroi dados faltantes
- **Tratamento de Falhas**: Sistema detecta automaticamente arquivos ausentes

## 📝 Notas de Implementação

O projeto opera em três etapas principais:

1. **Leitura e preparação dos dados**:
   ```python
   with open("parte1.txt", "r") as arquivo1:
       p1 = arquivo1.read().strip().replace(' ','')
   ```

2. **Cálculo de paridade**:
   ```python
   def calcular_paridade(p1, p2, p3):
       paridade = ""
       for p, q, r in zip(p1, p2, p3):
           bit_paridade = int(p) ^ int(q) ^ int(r)
           paridade += str(bit_paridade)
       return paridade
   ```

3. **Recuperação de dados**:
   ```python
   def recuperar(op):
       if op ==1:
           rec = calcular_paridade(p2, p3, paridade)
       # ... outras recuperações
   ```

## 🌟 Possíveis Melhorias (To-Do)

- [ ] Suporte para mais de 3 arquivos
- [ ] Interface gráfica
- [ ] Verificação de integridade contínua
- [ ] Suporte a arquivos binários reais (não apenas representações textuais)
- [ ] Criptografia integrada

## 📜 Licença

Este projeto está licenciado sob a MIT License - sinta-se à vontade para usar e modificar!

---

**Divirta-se explorando o mundo de RAID e recuperação de dados!** 💻🔧  
Se encontrar problemas, abra uma issue no GitHub. Contribuições são bem-vindas!
