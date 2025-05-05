# test_kmers.py
import pytest
from kmers import read_fasta, extract_kmers, write_kmer_data
import os

def test_read_fasta(tmp_path):
    """
    Test reading a FASTA file with multiple sequences and header lines.
    Makes sure headers are skipped and sequences are concatenated and capitalized. 
    """
    test_file = tmp_path / "test.fa"
    test_file.write_text(">seq1\nACGTACGT\n>seq2\nTTGCAA")
    result = read_fasta(str(test_file))
    assert result == "ACGTACGTTTGCAA"
    
def test_extract_kmers_basic():
    """
    Test basic extraction of 3-mers and their next character counts.
    Confirms correct total and next-nucleotide frequencies.
    """
    seq = "ACGTAC"
    k = 3
    result = extract_kmers(seq, k)
    
    # Check that ACG appears once and is followed by T
    assert result["ACG"]["count"] == 1
    assert result["ACG"]["next"] == {'T': 1}
    
    # Check that CGT is followed by A
    assert result["CGT"]["next"] == {'A': 1}
    
    # Confirm final k-mer (TAC) is counted even though it has no next base
    assert "TAC" in result
    
def test_extract_kmers_edge():
    """
    Test a 1-character sequence with k = 1.
    Makes sure correct counts appear in the output file.
    """
    seq = "A"
    k = 1
    result = extract_kmers(seq, k)
    assert result == {'A': {'count': 1, 'next': {}}}
    
def test_write_kmer_data(tmp_path):
    """
    Test writing k-mer dictionary to file and validate content format.
    Makes sure correct counts appear in the output file. 
    """
    output = tmp_path / "output.txt"
    
    # Define sample k-mer dictionary to write
    kmer_data = {
           'AAA': {'count': 3, 'next': {'A': 1, 'C': 2}},
        'AAC': {'count': 2, 'next': {'G': 2}}
    }
    
    write_kmer_data(kmer_data, str(output))
    
    # Read written content
    contents = output.read_text()
    
    # Validate header and key values
    assert "Kmer\tTotal\tNext_A\tNext_C\tNext_G\tNext_T" in contents
    assert "AAA\t3\t1\t2\t0\t0" in contents
    assert "AAC\t2\t0\t0\t2\t0" in contents