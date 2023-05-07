#A list in a dictionary
favorite_places = {
    "Genesis": ["Tent", "SRC", "FECE"],
    "Blackprince": ["Hall 7", "FECE", "Tent"],
    "Bene": ["Amen", "FECE", "Tent"]
}
for user, place in favorite_places.items():
    print(f"\n{user}'s favorite places are:")
    for each in place:
        print(f"{each}")
        
        
cities = {
    "Ayeduasi": {
        "Country": "Ghana",
        "Population": 1000,
        "Fact": "Food is expensive"
    },
    "Enyiresi": {
        "Country": "Ghana",
        "Population": 1200,
        "Fact": "Food is cheap"
    },
    "Koforidua": {
        "Country": "Ghana",
        "Population": 3000,
        "Fact": "The place is fun"
    }
}
  
#A dictionary in a dictionary  
for city, info in cities.items():
    print(f"\n{city} has the following details: ")
    print(f"Country: {info['Country']} ")
    print(f"Population: {info['Population']} ")
    print(f"Fact: {info['Fact']} ")