import os
import sys
import argparse

def parse_fasta(file):
    sequences = []
    with open(file) as f:
        seq = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    sequences.append(seq)
                    seq = ""
            else:
                seq += line
        if seq:
            sequences.append(seq)
    return sequences

def compute_stats(sequences):
    total_len = sum(len(seq) for seq in sequences)
    num_seq = len(sequences)
    gc = sum(seq.count("G") + seq.count("C") for seq in sequences)
    gc_percent = (gc / total_len) * 100 if total_len > 0 else 0

    return num_seq, total_len, round(gc_percent, 2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FASTA stats calculator")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")

    args = parser.parse_args()

if not os.path.exists(args.input):
    print(f"Error: File {args.input} not found")
    sys.exit(1)

    sequences = parse_fasta(args.input)
    num_seq, total_len, gc_percent = compute_stats(sequences)

    print(f"Sequences: {num_seq}")
    print(f"Total length: {total_len}")
    print(f"GC %: {gc_percent}")e

def parse_fasta(file):
    sequences = []
    with open(file) as f:
        seq = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    sequences.append(seq)
                    seq = ""
            else:
                seq += line
        if seq:
            sequences.append(seq)
    return sequences

def compute_stats(sequences):
    total_len = sum(len(seq) for seq in sequences)
    num_seq = len(sequences)
    gc = sum(seq.count("G") + seq.count("C") for seq in sequences)
    gc_percent = (gc / total_len) * 100 if total_len > 0 else 0

    return num_seq, total_len, round(gc_percent, 2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FASTA stats calculator")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA file")

    args = parser.parse_args()

    sequences = parse_fasta(args.input)
    num_seq, total_len, gc_percent = compute_stats(sequences)

    print(f"Sequences: {num_seq}")
    print(f"Total length: {total_len}")
    print(f"GC %: {gc_percent}")
