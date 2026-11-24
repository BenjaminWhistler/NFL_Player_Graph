from collections import defaultdict, deque
from typing import List


class Graph:
    def __init__(self):
        self._graph = defaultdict(dict)

    def __str__(self):
        temp = ""
        for player, teammates in self._graph.items():
            temp = temp + f"{player}: {teammates}\n"
        return temp


    def add_player(self, player):
        if player in self._graph:
            raise ValueError(f"Vertex {player} already exists")
        self._graph[player] = {}

    def add_edge(self, player1:str, player2:str, teams: List):
        if player1 not in self._graph:
            self.add_player(player1)
        if player2 not in self._graph:
            self.add_player(player2)
        if player2 not in self._graph[player1]:
            self._graph[player1][player2] = set()
        if player1 not in self._graph[player2]:
            self._graph[player2][player1] = set()
        for team in teams:
            self._graph[player1][player2].add(team)
            self._graph[player2][player1].add(team)

    def delete_player(self, player):
        if player not in self._graph:
            return
        for teammate in self._graph[player]:
            self._graph[teammate].pop(player)
        self._graph.pop(player)

    def delete_edge(self, player1, player2):
        if player1 not in self._graph:
            raise ValueError(f"Vertex {player1} does not exist")
        if player2 not in self._graph:
            raise ValueError(f"Vertex {player2} does not exist")
        if player2 in self._graph[player1]:
            self._graph[player1].pop(player2)
        if player1 in self._graph[player2]:
            self._graph[player2].pop(player1)

    def return_teammates(self, player):
        return self._graph[player]

    def return_teammates_count(self, player):
        return len(self._graph[player])

    def is_teammate(self, player1, player2):
        if player1 in self._graph[player2]:
            return True
        return False

    def find_closest_relationship_bfs(self, player1, player2):
        if player1 not in self._graph:
            raise ValueError(f"Vertex {player1} does not exist")
        if player2 not in self._graph:
            raise ValueError(f"Vertex {player2} does not exist")
        seen = {player1}
        queue = deque()
        queue.append(player1)
        predecessors = {player1: None}
        while queue:
            current = queue.popleft()
            # List is return with quickest path, from Player 1 to Player 2:
            # [('Player1', {teams shared with 'NextPlayer1'}), ('NextPlayer1', {teams shared with 'NextPlayer2'}), etc]
            if current == player2:
                quickest_path = []
                teams = None
                while current != player1:
                    quickest_path.append((current, teams))
                    parent = current
                    current = predecessors[current]
                    teams = self._graph[parent][current]
                quickest_path.append((current, teams))
                quickest_path.reverse()
                return quickest_path
            for teammate in self._graph[current]:
                if teammate not in seen:
                    seen.add(teammate)
                    queue.append(teammate)
                    predecessors[teammate] = current
        return []

    def find_closest_relationship_dfs(self, player1, player2):
        seen = {player1}
        stack = [player1]
        path = []
        while stack:
            current = stack.pop()
            path.append(current)
            if current == player2:
                return path
            for teammate in self._graph[current]:
                if teammate not in seen:
                    seen.add(teammate)
                    stack.append(teammate)
        return []





"""
graph = Graph()
graph.add_edge("Dalton Kincaid", "Josh Allen", ["Buffalo Bills", "Steelers"])
graph.add_edge("Dalton Kincaid", "Jim Allen", ["Eagles"])
graph.add_edge("Jim Allen", "Tom Brady", ["Patriots"])
print(graph)
print(graph.return_teammates("Dalton Kincaid"))
print(graph.return_teammates_count("Dalton Kincaid"))
print(graph.is_teammate("Josh Allen", "Jim Allen"))
print(graph.find_closest_relationship_bfs("Dalton Kincaid", "Josh Allen"))
print(graph.find_closest_relationship_dfs("Dalton Kincaid", "Josh Allen"))
print(graph.return_teammates("Tom Brady"))
print(graph.find_closest_relationship_bfs("Dalton Kincaid", "Tom Brady"))
"""

"""
GRAPH = {
    "Josh Allen": {
        "Dalton Kincaid": set("Buffalo Bills, Steelers")
    }   
"""