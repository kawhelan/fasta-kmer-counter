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

## Usage

### Command line:

```
python3 kmers.py <path_to_fasta_file> <k>
```

### Example:

```
python3 kmers.py /mnt/homes4celsrs/shared/439539/reads.fa 4
```
This runs the script on a shared FASTA file and analyzes 4-mers.

---

## Output format

```
Kmer    Total   Next_A  Next_C  Next_G  Next_T
AAAA    61264   15265   15010   15924   15065
AAAC    61124   14859   15671   14910   15684
...
```

- Total = how many times the k-mer appeared
- Next_X = how many times each base followed it

---

## Running the tests

A separate test suite is included using `pytest`.
To run all tests:

```
pytest test_kmers.py
```

Tests cover:
- FASTA parsing (`read_fasta`)
- k-mer extraction and follower logic (`extract_kmers`)
- Output formatting (`write_kmer_data`)
- Edge cases (e.g., final k-mer, short sequences)

---

## Files included

```
kmers.py           # Main script for k-mer counting
test_kmers.py      # Unit tests (pytest)
kmer_output_k4.txt # Example output (for k=4)
README.md          # This file
documentation.md   # Reflection questions and design summary
```

---

## For

BIO 539: Big Data Analysis - Spring 2025
University of Rhode Island
