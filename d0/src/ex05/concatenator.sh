#!/bin/sh

OUTPUT="$1"

first_file=$(ls *.csv | grep -v "^$OUTPUT$" | head -n 1)
if [ -z "$first_file" ]; then
    echo "No CSV files found"
    exit 1
fi

head -n 1 "$first_file" > "$OUTPUT"

for file in $(ls *.csv | grep -v "^$OUTPUT$" | sort); do
    tail -n +2 "$file" >> "$OUTPUT"
done
