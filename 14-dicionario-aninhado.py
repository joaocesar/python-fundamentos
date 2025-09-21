# Dicionário aninhado
# Dicionário dentro de outro dicionário
# Útil para representar dados mais complexos
filmeDict = {
    "Inception": {
        "yearLaunch": 2010,
        "noteMovie": 8.8,
        "genre": ["Action", "Sci-Fi", "Thriller"],
        "director": "Christopher Nolan",
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
        "awards": {
            "Oscar": 4,
            "BAFTA": 3,
            "Golden Globe": 4
        },
        "isAvailable": True
    },
    "The Dark Knight": {
        "yearLaunch": 2008,
        "noteMovie": 9.0,
        "genre": ["Action", "Crime", "Drama"],
        "director": "Christopher Nolan",
        "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "awards": {
            "Oscar": 2,
            "BAFTA": 1,
            "Golden Globe": 1
        },
        "isAvailable": True
    },
    "Pulp Fiction": {
        "yearLaunch": 1994,
        "noteMovie": 8.9,
        "genre": ["Crime", "Drama"],
        "director": "Quentin Tarantino",
        "cast": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"],
        "awards": {
            "Oscar": 1,
            "BAFTA": 0,
            "Golden Globe": 1
        },
        "isAvailable": True
    }
}
print(filmeDict)
print(type(filmeDict))
