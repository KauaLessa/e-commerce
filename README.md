# e-commerce
An object-oriented online retail platform with classes for products, users, and transactions, supporting features like shopping carts and order tracking.

# Instruções de execução:

## 1. Primeiro, crie um ambiente virtual:
```bash
python -m venv nome_do_ambiente
```

## 2. Em seguida, ative o ambiente virtual:
```bash
source nome_do_ambiente/bin/activate
```

## 3. Uma vez dentro do ambiente virtual, instale o Django
```bash
pip install django
```

## 4. Instale o Pillow:
```bash
python -m pip install Pillow
```

## 5. Agora, clone o repositório:
```bash
git clone https://github.com/KauaLessa/e-commerce
``` 

## 6. Finalmente, dentro do diretório raiz do projeto, execute o seguinte comando:
```bash
python manage.py runserver
```
O projeto agora deve estar executando.

# Importante:
O banco de dados já possui um usuário admin armazenado.

Suas credencias são:

username: admin

senha: password

## ID do produto

Uma vez dentro da página de um produto, é possível verificar o seu id através da url. 

### Exemplo:

http://127.0.0.1:8000/product/1/

O id do produto é 1

# Padrões de projeto
4 padrões de projeto foram implementados. São 4 módulos no total, localizados no caminho products/dp

## 1. Command
O padrão de projeto command foi implementado na execução de tarefas que tangem o efetuamento de pedidos
e manipulação do carrinho de maneira geral. O objetivo da implementação desse padrão de projeto foi separar
a lógica de manipulação do banco de dados necessária para executar certas operações, assim como a facilidade
de extensão dessas operações, através da implementação de novos commands. 

## 2. Observer
O padrão Observer foi implementado com o objetivo de suprir a necessidade de atualizar os carrinhos dos
usuários uma vez que o preço de um produto contido em algum carrinho fora modificado pelo administrador.
A implementação se deu através da extenção de classes já existentes. As classes ***Product*** e ***Cart*** foram
extendidas nas subclasses Subject e Observer, respectivamente.

## 3. Chain of Responsability (cor)
Chain of Responsability foi utilizado para gerir o processo de efetivação de um pedido. Este padrão de
projeto foi implementado pois uma série de verificações devem ser feitas para que de fato o pedido seja
realizado. A cadeia verifica informações de pagamento, localização, estado do carrinho, entre outras.

## 4. Facade
Facade foi utilizado para facilitar a inicialização e utilização completa da cadeia de responsabilidade.
A utilização da cadeia completa requer uma série de instanciamentos e chamadas de métodos, portanto a 
classe ***CompleteHandlerChain*** serve como uma fachada, cuidando desse processo de preparação
necessário para utilizar da cadeia completa.
