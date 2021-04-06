# Rest API - Peliculas - Flask

![](portada.png)

### Requisitos

- Python 3.6 o superior

### Ejecutar aplicación con Docker Compose

```bash
docker-compose up -d
```

### Acceder a la aplicación

```bash
http://localhost:5000/peliculas
```

## Instalación Manual [sin docker (+ mysql server local)]

```
python3 -m venv env
activate en Unix or MacOS: 👉🏻 source env/bin/activate
activate en Windows (cmd.exe): 👉🏻 env\Scripts\activate.bat
activate en Windows (PowerShell): 👉🏻 env\Scripts\Activate.ps1

pip install -r requirements.txt
```

```sql sin docker (+ mysql server local)
CREATE DATABASE db_api_python;
```

### Crear tabla [sin docker (+ mysql server local)]

```sql
CREATE TABLE db_api_python.peliculas (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(150) NULL,
  estreno VARCHAR(20) NULL,
  director VARCHAR(100) NULL,
  reparto VARCHAR(250) NULL,
  genero VARCHAR(125) NULL,
  sinopsis VARCHAR(250) NULL,
  PRIMARY KEY (id));

CREATE TABLE db_api_python.usuarios{
  id INT NOT NULL AUTO_INCREMENT,
  usuario VARCHAR(70) NULL,
  clave VARCHAR(100) NULL,
  PRIMARY KEY (id);
}


INSERT INTO db_api_python.peliculas (nombre, estreno, director, reparto, genero, sinopsis) VALUES ('El Padrino', '1972', 'Francis Ford Coppola', 'Marlon Brando, Al Pacino, James Caan', 'Drama', 'La historia de una familia de la mafia siciliana en Nueva York. El hijo mayor, Michael Corleone, regresa a casa después de la guerra para asumir el negocio familiar. Pero su padre, Don Vito Corleone, no está dispuesto a ceder el control de la familia a su hijo. Mientras tanto, Michael se ve envuelto en una guerra entre las familias de la mafia y la policía.');

```

### Ejecutar aplicación [sin docker (+ mysql server local)]

```bash
python app.py
```
