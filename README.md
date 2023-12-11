# Minha API

Este projeto foi desenvolvido a partir da matéria de **Desenvolvimento Full Stack Básico** para entrega da primeira Sprint do curso Pós graduação de **Desenvolvimento Full Stack** da **PUC RIO**

O objetivo é ilustrar e disponibilizar o projeto feito por mim.

---
## Como executar 

É preciso ter todas as libs python listadas no `requirements.txt` instaladas.
Depois de copiar o repositório, é preciso ir ao diretório raiz, pelo terminal, para poder executar os comandos apresentados abaixo.

> É extremamente indicado o uso de ambientes virtuais como o [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, apresentadas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Enquanto estiver desenvolvendo é indicado executar usando o parâmetro reload, que reiniciará o servidor
automaticamente depois de uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.