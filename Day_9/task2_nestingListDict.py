capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested list in dictionary

travel_log = {
    "France": ["Paris","Lille", "Dijon"],
    "Germany": ["stuttgart", "Berlin"],

}

#print Lille

print(travel_log["France"][1])
print(travel_log["Germany"][0])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])

travel_log2 = {
    "France": {
        "num_times_visited": 8,
        "cities_visit": ["Paris","Little","Dijon"]
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log2["Germany"]["cities_visited"][2])
print(travel_log2["France"])