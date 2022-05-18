## Prerequisitos
    1. Python 3.8
    2. Java para rodar o H2
    3. Rodar o requirements.txt
        $ pip install -r requirements.txt
    4. Arquivo CSV deve se chamar movielist.csv e estar na raiz junto com o arquivo run.py

## Run
    1. Database
        $ java -cp .\myApp\database\h2-2.1.212.jar org.h2.tools.Server -tcp -tcpAllowOthers -tcpPort 5234 -baseDir .. -ifNotExists
    2. Aplicacao
        $ python run.py

## Test
    1. A URL provavelmente vai ser http://127.0.0.1:5000, criei um endpoint get chamado premio, logo só rodar no navegador http://127.0.0.1:5000/premio ou fazer um get pelo postman na mesma url
    2. Para rodar com outro movielist.csv só derrubar a aplicação com ctrl+c, substituir o csv da raiz e subir novamente