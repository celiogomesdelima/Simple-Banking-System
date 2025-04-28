# Sistema Bancário em Python 🏦

Este é um projeto de um sistema bancário simples desenvolvido em Python, com funcionalidades básicas como criação de clientes e contas, realização de depósitos, saques e emissão de extratos.

## 📋 Funcionalidades

- Criar clientes (Pessoa Física)
- Criar contas bancárias (Conta Corrente)
- Depositar valores em contas
- Realizar saques (com limites de valor e quantidade de saques)
- Exibir extrato de movimentações
- Listar todas as contas criadas

## 🚀 Tecnologias utilizadas

- Python 3.10+
- Programação Orientada a Objetos (POO)
- Princípios de boas práticas de software (abstração, herança, composição)

## 📂 Estrutura de Classes

- `Cliente`: Classe base para clientes.
- `PessoaFisica`: Herda de `Cliente`.
- `Conta`: Classe base de conta bancária.
- `ContaCorrente`: Herda de `Conta`, com regras específicas de saque.
- `Transacao`: Classe abstrata para transações.
- `Saque` e `Deposito`: Implementam a classe abstrata `Transacao`.
- `Historico`: Armazena as transações de uma conta.

## 🎮 Como executar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Execute o programa:
   ```bash
   python nome_do_arquivo.py
   ```

## 📖 Exemplo de uso

```plaintext
=========== MENU =============
[S] Sacar
[E] Extrato
[D] Depositar
[NC] Nova conta
[LC] Listar Contas
[NU] Novo usuário
[Q] Quit (Sair)
```

- Para criar um novo cliente, selecione `[NU]`.
- Para abrir uma nova conta para um cliente existente, selecione `[NC]`.
- Para movimentações financeiras, utilize `[D]` para depositar, `[S]` para sacar e `[E]` para visualizar o extrato.

## 🔥 Melhorias futuras

- Persistência de dados em arquivos (JSON ou SQLite)
- Interface gráfica (GUI)
- Implementar mais tipos de contas (ex: Conta Poupança)
- Controle de autenticação de usuários

## 🧑‍💻 Autor

Desenvolvido por [Seu Nome Aqui].

---

# 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

