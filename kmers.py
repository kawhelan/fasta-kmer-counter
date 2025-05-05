# kmers.py
import sys
from collections import defaultdict

def read_fasta(filename):
    """
    Read a FASTA file and return the full sequence as a single string.

    Args:
        filename (str): Path to FASTA file

    Returns:
        str: Concatenated sequence string
    """
    sequence = []
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('>'): # Skip header lines
                sequence.append(line.strip().upper()) # Clean and uppercase sequence lines
    return ''.join(sequence) # Return full concatenated sequence

def extract_kmers(sequence, k):
    """
    Extract k-mers and count their occurrences and what follows them.

    Args:
        sequence (str): DNA sequence
        k (int): k-mer length

    Returns:
        dict: {kmer: {'count': int, 'next': {'A': int, 'C': int, 'G': int, 'T': int}}}
    """
    # Defaultdict structure to hold k-mer counts and what follows them
    kmer_data = defaultdict(lambda: {'count': 0, 'next': defaultdict(int)})
    # Loop through sequence to extract each k-mer and its next character
    for i in range(len(sequence) - k):
        kmer = sequence[i:i+k] # Get the current k-mer
        next_char = sequence[i+k] # Get the character that follows the k-mer
        kmer_data[kmer]['count'] += 1 # Count how often this k-mer appears
        kmer_data[kmer]['next'][next_char] += 1 # Count what comes next

    # Add the last k-mer (if there's no following character)
    last_kmer = sequence[-k:]
    if len(last_kmer) == k:
        kmer_data[last_kmer]['count'] += 1 # Count it even without a follower

    return kmer_data

def write_kmer_data(kmer_data, output_filename):
    """
    Write k-mer data to a tab-delimited output file.

    Args:
        kmer_data (dict): Output from extract_kmers()
        output_filename (str): Output file path
    """
    with open(output_filename, 'w') as f:
        # Write header row
        f.write("Kmer\tTotal\tNext_A\tNext_C\tNext_G\tNext_T\n")
        # Sort k-mers alphabetically and write data
        for kmer, data in sorted(kmer_data.items()):
            next_counts = data['next']
            f.write(f"{kmer}\t{data['count']}\t"
                    f"{next_counts.get('A', 0)}\t"
                    f"{next_counts.get('C', 0)}\t"
                    f"{next_counts.get('G', 0)}\t"
                    f"{next_counts.get('T', 0)}\n")

def main():
    # Expect exactly two command-line arguments: file path and k value
    if len(sys.argv) != 3:
        print("Usage: python kmers.py <reads.fa> <k>")
        sys.exit(1)

    fasta_path = sys.argv[1]
    k = int(sys.argv[2])
    # Process the sequence and write the output
    sequence = read_fasta(fasta_path)
    kmer_data = extract_kmers(sequence, k)
    output_filename = f"kmer_output_k{k}.txt"
    write_kmer_data(kmer_data, output_filename)
    print(f"Output written to {output_filename}")

if __name__ == "__main__":
    main()
