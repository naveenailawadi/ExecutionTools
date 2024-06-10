import hashlib
import sys

def calculate_file_hash(filepath, hash_algorithm='sha256'):
    """Calculate the hash of a file."""
    hash_func = getattr(hashlib, hash_algorithm)()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def compare_files(filepaths, hash_algorithm='sha256'):
    """Compare the hashes of multiple files to check if they are the same."""
    file_hashes = {}
    for filepath in filepaths:
        file_hash = calculate_file_hash(filepath, hash_algorithm)
        file_hashes[filepath] = file_hash

    # Check if all hashes are the same
    unique_hashes = set(file_hashes.values())
    if len(unique_hashes) == 1:
        print("All files have the same hash.")
    else:
        print("Files have different hashes.")
        for filepath, file_hash in file_hashes.items():
            print(f"{filepath}: {file_hash}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python compare_hashes.py <file1> <file2> ... <fileN>")
        sys.exit(1)

    filepaths = sys.argv[1:]
    compare_files(filepaths)