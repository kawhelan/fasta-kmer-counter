# Documentation: FASTA K-mer Counter Script

## 1. What data structures did you use and why?

I used a `defaultdict` to keep track of each k-mer. Each one stores:
- How many times it appears
- How many times it’s followed by A, C, G, or T

I chose `defaultdict` because it makes it easy to add new k-mers and update counts without writing extra code to check if keys already exist.

---

## 2. How did you handle edge cases?

I handled two special situations:

- **The last k-mer in the in the sequence** might not have a nucleotide that comes after it. I still count it, but don't try to record what follows. 
- **Very short sequences** (shorter than the value of *k*) won't have any valid k-mers and the extraction loop won't run. In that case, the script returns an empty or minimal result without crashing. 

---

## 3. How does your code avoid overcounting or missing data?

I made sure to:
- Stop the loop before it tries to go past the end of the sequence
- Count the final k-mer even if there’s no next base
- Only count what follows a k-mer when there actually is a next base

This avoids overcounting the last k-mer’s next base (which doesn’t exist) and missing that the last k-mer occurred.



