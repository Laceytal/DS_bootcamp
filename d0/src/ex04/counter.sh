#!/bin/sh

echo '"name","count"' > "hh_uniq_positions.csv"
tail -n +2 "../ex03/hh_positions.csv" | cut -d',' -f3 | tr -d '"' | grep -v '^-$' | sort | uniq -c | sort -nr | \
awk '{
  count=$1;
  $1=""; sub(/^ +/, "");
  name=$0;
  print "\"" name "\"," count
}' >> "hh_uniq_positions.csv"
