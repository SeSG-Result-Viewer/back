## Instruções para instalar as dependências

+ O código abaixo cria um ambiente virtual.

```
python -m venv venv
```

+ O código abaixo ativa o ambiente virtual criado.

```
venv\Scripts\activate.bat
```

+ Verfifique se está dentro da venv, caso não esteja, basta abrir um novo terminal (solução para VSCode).
+ O próximo código irá instalar as dependências dentro da venv.

```
pip install -r requirements.txt
```

+ Este código inicia o servidor.

```
uvicorn main:app --reload
```

---

> Os códigos comentados no arquivo main.py estão em implementação, junto ao banco de dados, então para não gerar erro, deixamos assim.