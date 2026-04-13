import csv
import re
from collections import defaultdict, OrderedDict
import pytest

class Movies:
    def __init__(self, path_to_the_file):
        self.path = path_to_the_file
        self.movies = []  # [{id, title, year, genres}, ...]

        with open(self.path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row["title"]
                # достаем год из названия
                match = re.search(r"\((\d{4})\)", title)
                year = int(match.group(1)) if match else None

                genres = row["genres"].split("|") if row["genres"] != "(no genres listed)" else []

                self.movies.append({
                    "id": int(row["movieId"]),
                    "title": title,
                    "year": year,
                    "genres": genres
                })

    def dist_by_release(self):
        counts = defaultdict(int)
        for m in self.movies:
            if m["year"]:
                counts[m["year"]] += 1
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return OrderedDict(sorted_counts)

    def dist_by_genres(self):
        counts = defaultdict(int)
        for m in self.movies:
            for g in m["genres"]:
                counts[g] += 1
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return OrderedDict(sorted_counts)

    def most_genres(self, n):
        movie_genre_counts = {m["title"]: len(m["genres"]) for m in self.movies}
        sorted_counts = sorted(movie_genre_counts.items(), key=lambda x: x[1], reverse=True)
        return OrderedDict(sorted_counts[:n])

@pytest.fixture
def movies(tmp_path):
    # создаем временный CSV-файл для тестов
    csv_content = """movieId,title,genres
1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
2,Jumanji (1995),Adventure|Children|Fantasy
3,Grumpier Old Men (1995),Comedy|Romance
4,Waiting to Exhale (1995),Comedy|Drama|Romance
5,Father of the Bride Part II (1995),Comedy
6,Heat (1995),Action|Crime|Thriller
7,Sabrina (1995),Comedy|Romance
8,Tom and Huck (1995),Adventure|Children
9,Sudden Death (1995),Action
10,GoldenEye (1995),Action|Adventure|Thriller
11,"American President, The (1995)",Comedy|Drama|Romance
12,Dracula: Dead and Loving It (1995),Comedy|Horror
13,Balto (1995),Adventure|Animation|Children
14,Nixon (1995),Drama
15,Cutthroat Island (1995),Action|Adventure|Romance
16,Casino (1995),Crime|Drama
"""
    file_path = tmp_path / "movies.csv"
    file_path.write_text(csv_content, encoding="utf-8")
    return Movies(file_path)


def test_dist_by_release(movies):
    result = movies.dist_by_release()
    assert isinstance(result, OrderedDict)
    assert list(result.keys()) == [1995]
    assert result[1995] == 16


def test_dist_by_genres(movies):
    result = movies.dist_by_genres()
    assert isinstance(result, OrderedDict)
    assert list(result.keys())[0] == "Comedy"
    assert result["Comedy"] == 7
    assert result["Horror"] == 1


def test_most_genres(movies):
    result = movies.most_genres(3)
    assert isinstance(result, OrderedDict)
    first_movie, genres_count = next(iter(result.items()))
    assert first_movie == "Toy Story (1995)"
    assert genres_count == 5
    assert len(result) == 3
