from Bio import SeqIO
import argparse
import sys
import os

def fasta_stats(file):
    total = 0
    total_len = 0

    for record in SeqIO.parse(file, "fasta"):
        seq = record.seq
        length = len(seq)
        gc = (seq.count("G") + seq.count("C")) / length * 100 if length > 0 else 0

        print(f"{os.path.basename(file)},{record.id},{length},{gc:.2f}")

        total += 1
        total_len += length

    return total, total_len


def main():
    parser = argparse.ArgumentParser(description="FASTA stats tool")
    parser.add_argument("inputs", nargs="+", help="Input FASTA files")
    parser.add_argument("-o", "--output", help="Output CSV file")

    args = parser.parse_args()

    if args.output:
        sys.stdout = open(args.output, "w")

    print("file,id,length,gc_percent")

    total_seq = 0
    total_len = 0

    for f in args.inputs:
        if not os.path.exists(f):
            print(f"Warning: File not found: {f}", file=sys.stderr)
            continue

        seqs, length = fasta_stats(f)
        total_seq += seqs
        total_len += length

    print("\nSummary:")
    print(f"Total sequences: {total_seq}")
    print(f"Total length: {total_len}")


if __name__ == "__main__":
    main()
