# FASTA K-mer Counter

This Python script processes a DNA sequence from a FASTA file, extracts all possible k-mers of a given length, and records what nucleotide follows each one. 
The output is a tab-delimited file summarizing total k-mer counts and the frequency of each possible base (A, C, G, T).

---

## What it does

- Reads a FASTA file and strips out header lines
- Extracts all substrings of length *k* (k-mers)
- Counts:
  - How often each k-mer appears
  - How often it’s followed by A, C, G, or T
- Outputs a `.txt` file with all counts

---

## Example command

```bash
python3 kmers.py /mnt/homes4celsrs/shared/439539/reads.fa 4
 
