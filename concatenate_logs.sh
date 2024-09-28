#!/bin/bash

# Check if a date argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 YYYY_MM_DD"
    exit 1
fi

# Set the date prefix for files to process
prefix="$1"

# Define the output file
output_file="${prefix}_combined_conversation.log"

# Remove the output file if it already exists
echo "Creating output file: $output_file"
rm -f "$output_file"

# Iterate over files matching the prefix and append to the output file
for file in ${prefix}_*.log; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        cat "$file" >> "$output_file"
        echo -e "\n" >> "$output_file" # Add a newline for separation
        echo "$file contents added to combined file."
    else
        echo "No files found with the prefix $prefix."
        exit 2
    fi
done

echo "Concatenation complete. All files combined into $output_file."