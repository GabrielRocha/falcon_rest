### Falcon + Python + SQLAlchemy

#### Problema proposto
* Selecionar, no máximo, os três amigos mais próximos de um determinado amigo.
* Cada amigos vive em uma posição específica (latitude e longitude).
	* Para os propósitos deste problema o mundo é plano e a latitude e a longitude são coordenadas cartesianas em um plano.
* Também cada amigo mora em uma posição diferente (dois amigos nunca estão na mesma latitude e longitude).

#### Tecnologias
* Falcon => http://falconframework.org
* Python2.7 => https://www.python.org
* SQLAlchemy => http://www.sqlalchemy.org
* Sqlite3 => https://www.sqlite.org

#### MakeFile
Com o proposito de facilitar a utilização da API foi criado um makefile. As opções oferecidas são: **install**, **start**, **stop** e **test**

##### Instalação de dependencias
Todas as dependencias do projeto serão instaladas. A lista pode ser acessada no arquivo **requirements.txt**
```
$ make install
```

##### Inicializar API
Inicializará um servidor web com a API no endereço http://localhost:8000
```
$ make start
```

##### Rotas
* /amigos/
	* Retorna, em json, todos os amigos cadastrados na API
* /amigos?id=1
	* Retorna somente o amigo com o id especificado
* /amigos_proximos?id=1
	* Lista os 3 amigos mais próximos do que foi especificado

#### Finalizar API
Para todos os processos da API
```
$ make stop
```

#### Testes
Executa toda as baterias de testes automatizados da API
```
$ make test
```