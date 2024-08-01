import pandas as pd
import os

def get_size_of_row(row):
    """Calcula el tamaño de una fila en bytes."""
    return sum(row.astype(str).apply(lambda x: len(x.encode('utf-8'))))

def split_dataframe(df, chunk_size_mb):
    """Divide el DataFrame en trozos más pequeños que no superen el tamaño especificado."""
    chunk_size_bytes = chunk_size_mb * 1024 * 1024  # Convertir MB a bytes
    chunks = []
    current_chunk = []
    current_chunk_size = 0

    for _, row in df.iterrows():
        row_size = get_size_of_row(row)
        if current_chunk_size + row_size > chunk_size_bytes:
            chunks.append(pd.DataFrame(current_chunk))
            current_chunk = []
            current_chunk_size = 0
        current_chunk.append(row)
        current_chunk_size += row_size

    if current_chunk:
        chunks.append(pd.DataFrame(current_chunk))
    
    return chunks

def main(input_csv, output_prefix, chunk_size_mb=80):
    # Cargar el archivo CSV
    df = pd.read_csv(input_csv)

    # Ordenar por la columna "id"
    df = df.sort_values(by="id")

    # Dividir el DataFrame en varios CSVs pequeños
    chunks = split_dataframe(df, chunk_size_mb)

    # Guardar cada chunk en un archivo CSV separado
    for i, chunk in enumerate(chunks):
        output_file = f"{output_prefix}_part_{i+1}.csv"
        chunk.to_csv(output_file, index=False)
        print(f"Guardado: {output_file}")

if __name__ == "__main__":
    input_csv = "data.csv"  # Nombre del archivo CSV de entrada
    output_prefix = "output"  # Prefijo para los archivos CSV de salida
    main(input_csv, output_prefix)
