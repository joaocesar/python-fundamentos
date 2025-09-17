movieName = "Top Gun Maverick"
movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura
muito consagrado na indústria
"""

print(movieName.upper())
print(movieName.lower())
print(movieName.capitalize())
print(movieName.title())
print(movieName.center(20, '-'))
print(movieName.find("u"))
print(movieDescription.find("u"))
print(movieName.count('u'))
print(movieDescription.count('u'))
print(movieName.replace("Gun", "Matrix"))
print(movieDescription.split("\n"))


