import NetworkClasses

graph = NetworkClasses.Graph()

# Add Players
graph.add_player("Josh Allen")
graph.add_player("James Cook")
graph.add_player("Tom Brady")
graph.add_player("Deion Sanders")
graph.add_player("Terry Bradshaw")
graph.add_player("Jim Kelly")
graph.add_player("Patrick Mahomes")
graph.add_player("Travis Kelce")

# Add relationships between existing players

graph.add_edge("Josh Allen", "James Cook", ["Buffalo Bills"])
graph.add_edge("Patrick Mahomes", "Travis Kelce", ["Kansas City Chiefs"])

# Add relationships between non-existing players

graph.add_edge("Josh Allen", "Dalton Kincaid", ["Buffalo Bills"])
graph.add_edge("Dalton Kincaid", "James Cook", ["Buffalo Bills"])
graph.add_edge("Deion Sanders", "Jamal Lewis", ["Baltimore Ravens"])
graph.add_edge("Andre Reed", "Jim Kelly", ["Buffalo Bills"])
graph.add_edge("Joe Burrow", "Jamarr Chase", ["Cincinnati Bengals"])
graph.add_edge("Jamal Lewis", "Derek Anderson", ["Cleveland Browns"])
graph.add_edge("Derek Anderson", "Josh Allen", ["Buffalo Bills"])
graph.add_edge("Deion Sanders", "Jerry Rice", ["San Francisco 49ers"])

# Delete Edges
print("Deletion examples:")
print(graph.return_teammates("Joe Burrow"))
print(graph.return_teammates_count("Jamarr Chase"))
print(graph.is_teammate("Joe Burrow", "Jamarr Chase"))
print(graph.find_closest_relationship_bfs("Jamarr Chase", "Joe Burrow"))
graph.delete_edge("Jamarr Chase", "Joe Burrow")
print(graph.return_teammates("Joe Burrow"))
print(graph.return_teammates_count("Jamarr Chase"))
print(graph.is_teammate("Joe Burrow", "Jamarr Chase"))
print(graph.find_closest_relationship_bfs("Jamarr Chase", "Joe Burrow"))
# graph.delete_edge("Phineas Flynn", "Darren Watkins Jr")


# Delete Relationships


# BFS
print("BFS: \n")
print("Possible Path example: ")
for player in graph.find_closest_relationship_bfs("Jerry Rice", "James Cook"):
    print(player[0])
    print("^\n|")
    print(player[1])
    print("|\nv")
print("Impossible Path example: ")
print(graph.find_closest_relationship_bfs("Jerry Rice", "Andre Reed"))
print("Repeated visits are prevented correctly example: ")
print(graph.find_closest_relationship_bfs("Josh Allen", "James Cook"))
print()
# DFS
print("DFS: \n")
print("Possible Path example: ")
print(graph.find_closest_relationship_bfs("Jerry Rice", "James Cook"))
print("Impossible Path example: ")
print(graph.find_closest_relationship_bfs("Jerry Rice", "Andre Reed"))
print("Repeated visits are prevented correctly example: ")
print(graph.find_closest_relationship_bfs("Josh Allen", "James Cook"))


# Delete Player
graph.delete_player("Dalton Kincaid")
graph.delete_player("Darren Watkins Jr")

print("\nComplete Graph:\n")
print(graph)