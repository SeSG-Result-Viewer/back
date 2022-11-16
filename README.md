## Instruções para instalar as dependências

+ Primeiramente, crie um ambiente virtual.
```
python -m venv venv
```

+ Ative o ambiente virtual criado.
  + Se estiver usando o CMD, utilize o comando abaixo:
    ```
    venv\Scripts\activate.bat
    ```
    
  + Caso esteja usando o PowerShell, utilize o seguinte comando:
    ```
    venv\Scripts\activate.ps1
    ```

+ Verfifique se está dentro da venv, pois o próximo código irá instalar as dependências.
```
pip install -r requirements.txt
```

+ Para iniciar o servidor, utilize o seguinte comando:
```
uvicorn main:app --reload
```
