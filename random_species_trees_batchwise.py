import os
import random

# Directory containing gene tree files
gene_tree_dir = r"D:\BUET\Oct'23\CSE6406(BA)\Code\all_gene_trees"

# List all gene tree files
gene_tree_files = [f for f in os.listdir(gene_tree_dir)]
#print(os.listdir(gene_tree_dir))
#print(gene_tree_files)

output_dir = r"D:\BUET\Oct'23\CSE6406(BA)\Code\all_species_trees"

# Function to randomly select and process 10 gene tree files
def process_random_files(gene_tree_files, batch_num):
    # Randomly select 15 files
    selected_files = random.sample(gene_tree_files, min(15,len(gene_tree_files)))
    #print(selected_files)
    
    # Write contents of selected files to a new file
    output_file_name = os.path.join(output_dir, f"gene_trees_batch_{batch_num}.txt")
    with open(output_file_name, "w") as output_file:
        for file_name in selected_files:
            with open(os.path.join(gene_tree_dir, file_name), "r") as input_file:
                output_file.write(input_file.read())
                output_file.write("\n")
    
    # Remove selected files from the list
    for file_name in selected_files:
        gene_tree_files.remove(file_name)

    #print(gene_tree_files)

# Process files until all gene tree files are processed
batch_counter = 1
while gene_tree_files:
    process_random_files(gene_tree_files, batch_counter)
    batch_counter += 1
