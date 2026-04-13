#!/bin/sh

QUERY=$(echo "$1" | sed 's/ /+/g') # Кодируем пробелы в запросе
curl -s "https://api.hh.ru/vacancies?text=${QUERY}&per_page=20" | jq '.' > hh.json
