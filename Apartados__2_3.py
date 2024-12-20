import os
from PyPDF2 import PdfReader
from langchain.schema import Document
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS

# Carpeta con archivos PDF
pdf_folder = "/home/bigdata/code/rags/pdf"  # Cambia esto por la ruta de tus archivos PDF

# Extraer texto de archivos PDF
def extract_text_from_pdfs(pdf_folder):
    documents = []
    for file_name in os.listdir(pdf_folder):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, file_name)
            reader = PdfReader(pdf_path)
            text = "".join(page.extract_text() for page in reader.pages if page.extract_text())
            documents.append(Document(page_content=text, metadata={"source": file_name}))
    return documents

# Cargar documentos y crear embeddings
documents = extract_text_from_pdfs(pdf_folder)
if documents:
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embeddings)

    # Realizar una búsqueda
    query = "¿Cuál es el contenido principal de los documentos?"
    results = vector_store.similarity_search(query)

    print("Resultados de la búsqueda:")
    for result in results:
        print(f"Documento: {result.metadata['source']}")
        print(result.page_content[:500], "\n")
else:
    print("No se encontraron archivos PDF en la carpeta proporcionada.")


import os
from PyPDF2 import PdfReader
from langchain.schema import Document
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS
import gradio as gr

# Extraer texto de archivos PDF
def extract_text_from_pdfs(pdf_folder):
    documents = []
    for file_name in os.listdir(pdf_folder):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, file_name)
            reader = PdfReader(pdf_path)
            text = "".join(page.extract_text() for page in reader.pages if page.extract_text())
            documents.append(Document(page_content=text, metadata={"source": file_name}))
    return documents

# Configuración inicial
pdf_folder = "/home/bigdata/code/rags/pdf"
documents = extract_text_from_pdfs(pdf_folder)
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.from_documents(documents, embeddings)

# Función de búsqueda
def search_query(query):
    results = vector_store.similarity_search(query)
    return "\n\n".join([f"Documento: {result.metadata['source']}\n{result.page_content[:500]}" for result in results])

# Interfaz Gradio
iface = gr.Interface(
    fn=search_query,
    inputs="text",
    outputs="text",
    title="Búsqueda en PDFs",
    description="Ingresa una consulta y encuentra la información en archivos PDF."
)

iface.launch()
