"""
Zombie Outbreak Simulation
==========================

Challenge Overview
------------------

The objective is to simulate the spread of a zombie outbreak in a grid-based city.
Each cell in the grid can either be empty, contain a human, or contain a zombie.
Each day, zombies spread to *all* adjacent cells which contain humans (up, down, left, right),
turning any humans in those cells into zombies. Empty cells remain empty.

The challenge will be to write a function that performs the simulation for a given
number of days and generates expected results.

Instructions for Participants
-----------------------------

    Understand the Grid Representation: The grid is a list of lists, where each element can be:
        'H' for a human
        'Z' for a zombie
        'E' for an empty cell (if needed)

    Simulation Logic:
        Each day, every zombie spreads to its adjacent cells (up, down, left, right).
        If an adjacent cell contains a human, it turns into a zombie.
        The simulation runs for a given number of days.

    Task:
        Implement the simulate_zombie_outbreak function.
        Ensure that the function correctly simulates the outbreak for the specified number of days.


Bonus challenges
----------------

- Can you add more complexity and/or scale to the simulation? e.g. randomness, humans fighting back
  or a larger grid?.
- If you add more complexity and find the behaviour becomes more "emergent", how would you adjust
  your testing approach?
- How could you animate your results? (hint: using Pygame or Matplotlib)
"""


class City:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def print_grid(self):
        for row in self.grid:
            print(" ".join(row))
        print()


def simulate_zombie_outbreak(city, days):
    """
    Simulate the spread of the zombie outbreak for a given number of days.

    Args:
        city: City object with the initial grid setup
        days: Number of days to simulate the outbreak
    """
    # Your code here

    return city.grid


# Example usage
initial_grid = [
    ["H", "H", "H", "Z"],
    ["H", "H", "H", "E"],
    ["H", "E", "H", "H"],
    ["H", "H", "H", "H"],
]

city = City(initial_grid)
city.print_grid()

result = simulate_zombie_outbreak(city, 3)
city.grid = result
city.print_grid()
