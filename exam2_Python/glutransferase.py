#Ejercicio 2 
#Ejercicio 2.1
import pandas as pd
from Bio import Entrez, SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import matplotlib.pyplot as plt

def source(id):
    # Conexión al NCBI
    Entrez.email = "emily.cherrez@est.ikiam.edu.ec" 
    handle = Entrez.efetch(db="nucleotide", id=id, rettype="gb", retmode="text")
    record = SeqIO.read(handle, "gb")
    
    # Extracción del nombre del organismo fuente
    source_name = record.annotations["source"]
    
    # Cálculo de la frecuencia de cada especie
    species_frequency = {}
    for feature in record.features:
        if feature.type == "source":
            organism = feature.qualifiers.get("organism", ["Unknown Organism"])[0]
            species_frequency[organism] = species_frequency.get(organism, 0) + 1
            print(species_frequency)
    
    # Guardar el resultado en un archivo CSV
    df = pd.DataFrame.from_dict(species_frequency, orient="index", columns=["Frequency"])
    df.index.name = "Species"
    df.to_csv("results/source.csv")
    
    # Imprimir el nombre del organismo fuente
    print("Source organism:", source_name)


