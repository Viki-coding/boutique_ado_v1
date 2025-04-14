import os

def check_file_path(file_path):
    if os.path.exists(file_path):
        print(f"File exists: {file_path}")
    else:
        print(f"File does not exist: {file_path}")

# Example usage
file_path = '/Users/vikimulhall/Documents/boutique_ado_v1/3'
check_file_path(file_path)
