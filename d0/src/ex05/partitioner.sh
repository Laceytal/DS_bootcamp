#!/bin/sh

INPUT="../ex03/hh_positions.csv"
HEADER=$(head -n 1 "$INPUT")
tail -n +2 "$INPUT" | while IFS=, read -r id created_at name has_test url; do
    date_part=$(echo "$created_at" | cut -c 2-11)# Дата — это первые 10 символов в поле created_at
    file="${date_part}.csv"
    if [ ! -f "$file" ]; then
        echo "$HEADER" > "$file"
    fi
    echo "$id,$created_at,$name,$has_test,$url" >> "$file"
done
