#!/bin/sh

jq -r '
  ["id","created_at","name","has_test","alternate_url"],
  (.items[] | [
    .id,
    .created_at,
    (
      if (.name | test("Junior|Middle|Senior"))
      then (.name | capture("(?<lvl>(Junior|Middle|Senior)(/(Junior|Middle|Senior))*)") | .lvl)
      else "-"
      end
    ),
    .has_test,
    .alternate_url
  ]) | @csv
' ../ex00/hh.json > hh_positions.tmp.csv

(head -n 1 hh_positions.tmp.csv && tail -n +2 hh_positions.tmp.csv | sort -t, -k2,2 -k1,1) > hh_positions.csv

rm hh_positions.tmp.csv
