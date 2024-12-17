# Proyecto RAGs

## Descripción

Este repositorio contiene diferentes implementaciones de sistemas RAG (Retrieved Augmented Generation) utilizando componentes de procesamiento de lenguaje natural y bases de datos vectoriales. Se desarrollarán múltiples notebooks que abordan diferentes aspectos de la creación y uso de RAGs.

## Apartados

El proyecto se divide en los siguientes apartados:

1. **RAG en inglés**: Implementación que crea un vector store a partir de datos extraídos de una página web.
2. **RAG en castellano**: Desarrollo de un sistema que crea un vector store a partir de uno o varios archivos PDF.
3. **GUI para RAG**: Creación de una interfaz gráfica de usuario para interactuar con uno de los RAGs anteriores.
4. **RAG dockerizado contra Mongo Atlas**: Implementación de un sistema RAG que utiliza Docker para conectarse a MongoDB Atlas.

## Requisitos

Asegúrate de tener instalado lo siguiente:

- Python 3.10 o superior
- [Docker](https://www.docker.com/products/docker-desktop)
- Acceso a MongoDB Atlas (para el apartado 4)

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu-usuario/proyecto-rags.git
   cd proyecto-rags
   ```

2. Crea un archivo `requirements.txt` con las siguientes dependencias necesarias para los RAGs:

   ```plaintext
   langchain
   langchain-community
   pymongo
   sentence-transformers
   faiss-cpu
   dnspython
   ```

3. Asegúrate de tener un archivo `.env` para las credenciales de MongoDB (solo necesario para el apartado 4):

   ```plaintext
   MONGO_URL="mongodb+srv://<username>:<password>@<cluster_url>/<database>?retryWrites=true&w=majority"
   ```

## Uso

### Apartado 1: RAG en inglés

- Navega al notebook correspondiente y ejecuta las celdas para crear un vector store a partir de una página web.

### Apartado 2: RAG en castellano

- Abre el notebook para crear un vector store utilizando uno o más archivos PDF y sigue las instrucciones proporcionadas.

### Apartado 3: GUI para RAG

- Ejecuta el script correspondiente para lanzar la interfaz gráfica que permitirá interactuar con el RAG seleccionado.

### Apartado 4: RAG dockerizado contra Mongo Atlas

1. **Construir la imagen Docker:**

   Desde el directorio raíz del proyecto, ejecuta:

   ```bash
   docker build -t rag-mongo-atlas .
   ```

2. **Ejecutar el contenedor Docker:**

   Si utilizas un archivo de entorno, ejecuta:

   ```bash
   docker run --env-file .env rag-mongo-atlas
   ```

   Sin el archivo de entorno:

   ```bash
   docker run rag-mongo-atlas
   ```

## Contribución

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea tu branch (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y confirma (`git commit -m 'Añadir nueva funcionalidad'`).
4. Haz push a tu branch (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.
