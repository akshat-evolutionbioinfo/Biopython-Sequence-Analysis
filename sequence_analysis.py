from Bio.Seq import Seq

# DNA sequence
dna = Seq("ATGCGTACGTTAGC")

print("DNA Sequence:", dna)
print("Sequence Length:", len(dna))

# GC Content
gc_content = (dna.count("G") + dna.count("C")) / len(dna) * 100
print("GC Content:", round(gc_content, 2), "%")

# Reverse Complement
print("Reverse Complement:", dna.reverse_complement())

# Transcription
rna = dna.transcribe()
print("RNA Sequence:", rna)

# Translation
protein = dna.translate()
print("Protein Sequence:", protein)
