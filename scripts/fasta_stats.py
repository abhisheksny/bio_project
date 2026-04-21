from Bio import SeqIO

def fasta_stats(file):
    lengths = []
    for record in SeqIO.parse(file, "fasta"):
        lengths.append(len(record.seq))
    
    print("Sequences:", len(lengths))
    print("Avg length:", sum(lengths)/len(lengths))

if __name__ == "__main__":
    fasta_stats("test.fasta")
