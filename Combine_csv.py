import csv
import os

# --- Configuration ---
# Generate input filenames assuming a consistent pattern
input_filenames = [f'squid_game_s2_ep{i}.csv' for i in range(1, 8)] # e1 to e9
output_filename = 'combined_squid_game_fear.csv'
# --- End Configuration ---

header_written = False
files_processed = 0

print(f"Attempting to combine {len(input_filenames)} files into '{output_filename}'...")

try:
    # Open the output file in write mode ('w'). This will overwrite the file if it exists.
    # Use newline='' to prevent extra blank rows between entries in the CSV.
    # Specify encoding='utf-8' for broader character support.
    with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)

        # Loop through each input CSV file
        for filename in input_filenames:
            # Check if the input file actually exists before trying to open it
            if not os.path.exists(filename):
                print(f"  Skipping: File '{filename}' not found.")
                continue # Move to the next file in the list

            print(f"  Processing: '{filename}'...")
            try:
                # Open the current input file in read mode ('r')
                with open(filename, 'r', newline='', encoding='utf-8') as infile:
                    csv_reader = csv.reader(infile)

                    # Read the header row from the current file
                    try:
                        header = next(csv_reader)
                    except StopIteration:
                        # Handle case where file exists but is empty
                        print(f"  Skipping: File '{filename}' is empty.")
                        continue

                    # Write the header ONLY if it hasn't been written yet (i.e., from the first file processed)
                    if not header_written:
                        csv_writer.writerow(header)
                        header_written = True # Set the flag so header isn't written again

                    # Write the rest of the data rows from the current file
                    for row in csv_reader:
                        # Optional: Add a check to skip completely blank rows if necessary
                        if row: # This checks if the list 'row' is not empty
                            csv_writer.writerow(row)
                    files_processed += 1

            except csv.Error as e:
                 print(f"  Error processing CSV data in '{filename}', line {csv_reader.line_num}: {e}. Skipping file.")
            except Exception as e:
                # Catch other potential errors during file reading/processing
                print(f"  An unexpected error occurred processing '{filename}': {e}. Skipping file.")

except IOError as e:
    print(f"Error: Could not write to output file '{output_filename}'. Check permissions or path. Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred during the combination process: {e}")


# Final status message
if files_processed > 0:
    print(f"\nSuccessfully combined data from {files_processed} files into '{output_filename}'.")
elif header_written:
     print(f"\nCombined file '{output_filename}' created with only the header (no data rows found in processed files).")
else:
    print(f"\nNo input files were found or processed. Output file '{output_filename}' might be empty or not created.")