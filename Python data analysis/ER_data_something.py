from datetime import datetime

start = datetime.now()


output_file = "C:\\Data\\matched_files.txt"
matched_files = []  # List to store matching file paths


# Open file_paths.txt and process each CSV file efficiently
with open(output_file, "r") as f:
    file_paths = [line.strip() for line in f.readlines()]

# Read only the 5th line of each CSV file efficiently
j=0
for file_path in file_paths:
    try:
        with open(file_path, "r", encoding="utf-8") as csvfile:
            for i, line in enumerate(csvfile):
                if line.strip() == "Digikrom Spectr.:0 (?)	X810 (V)	Y810 (V)	R810 (V)	X830 (V)	Y830 (V)	R830 (V)":
                    matched_files.append(file_path)
                    print(i, file_path)  # Print the 5th line without extra whitespace
                    # print()
                    break
                
                if i == 30:  # 5th line (zero-indexed)
                     break
                    
    except:
        pass


# # Export the list to a text file
# with open(output_file, "w", encoding="utf-8") as output:
#     for file in matched_files:
#         output.write(file + "\n")


print(datetime.now()-start)