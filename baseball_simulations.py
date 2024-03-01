import random
import matplotlib.pyplot as plt

class Player:
    def __init__(self, name, single, double, triple, homerun):
        self.name = name
        self.single = single
        self.double = double
        self.triple = triple
        self.homerun = homerun
        self.strikeout = 1 - (single + double + triple + homerun)

    # Simulate a single at-bat result based on the player's percentages
    def get_hit_result(self):
        roll = random.random()
        if roll < self.strikeout:
            return "Strikeout"
        elif roll < self.strikeout + self.single:
            return "Single"
        elif roll < self.strikeout + self.single + self.double:
            return "Double"
        elif roll < self.strikeout + self.single + self.double + self.triple:
            return "Triple"
        else:
            return "Homerun"

# Simulate a game with a specified number of simulations for each player
def simulate_game(players, num_simulations=100):
    results = {player.name: {"runs": 0, "hits": {"Single": 0, "Double": 0, "Triple": 0, "Homerun": 0, "Strikeout": 0}, "run_history": []} for player in players}
    for _ in range(num_simulations):
        for player in players:
            hit_result = player.get_hit_result()
            results[player.name]["hits"][hit_result] += 1
            if hit_result == "Single":
                results[player.name]["runs"] += 1
            elif hit_result == "Double":
                results[player.name]["runs"] += 2
            elif hit_result == "Triple":
                results[player.name]["runs"] += 3
            elif hit_result == "Homerun":
                results[player.name]["runs"] += 4
            results[player.name]["run_history"].append(results[player.name]["runs"])
    return results

# Run a simulation scenario with options to reveal different levels of information and plot results
def run_simulation_scenario(players, num_simulations=100, reveal_names=False, reveal_single_percentage=False, reveal_percentages=False, reveal_hits=False, plot_runs=False):
    results = simulate_game(players, num_simulations)
    winner = max(results, key=lambda x: results[x]["runs"])
    print(f"\nWinner: {winner} with {results[winner]['runs']} runs")
    if reveal_names:
        print("\nPlayer Names:")
        for player in players:
            print(player.name)
    if reveal_single_percentage:
        print("\nPlayer Single Percentage:")
        for player in players:
            print(f"{player.name}: Single: {player.single*100}%")
    if reveal_percentages:
        print("\nPlayer Percentages:")
        for player in players:
            print(f"{player.name}: Single: {player.single*100}%, Double: {player.double*100}%, Triple: {player.triple*100}%, Homerun: {player.homerun*100}%, Strikeout: {player.strikeout*100}%")
    if reveal_hits:
        print("\nPlayer Totals:")
        for player in players:
            print(f"{player.name}: {results[player.name]['runs']} runs, {results[player.name]['hits']}")
    else:
        print("\nPlayer Runs:")
        for player in players:
            print(f"{player.name}: {results[player.name]['runs']} runs")
    if plot_runs:
        plt.figure(figsize=(10, 6))
        for player in players:
            plt.plot(range(1, num_simulations + 1), results[player.name]["run_history"], label=player.name)
        plt.xlabel('At Bats')
        plt.ylabel('Cumulative Runs')
        plt.title('Cumulative Runs Over At Bats')
        plt.legend()
        plt.show()
    return results

# Players with percentages
players = [
    Player("Sammy 'Speedster' Smith", 0.15, 0.05, 0.02, 0.01),
    Player("Bella 'Batter' Brown", 0.18, 0.08, 0.03, 0.02),
    Player("Charlie 'Champion' Carter", 0.20, 0.08, 0.04, 0.03),
    # Add more players as needed
]

# Run simulation for each scenario
print("\nPlayer Names:")
for player in players:
    print(player.name)
input("\nPress Enter to start Scenario 1: Limited Information")
results_scenario_1 = run_simulation_scenario(players)


print("\nPlayer Single Percentage:")
for player in players:
    print(f"{player.name}: Single: {player.single*100}%")
input("\nPress Enter to start Scenario 2: Partial Information")
results_scenario_2 = run_simulation_scenario(players,reveal_percentages=True, plot_runs=True)


input("\nPress Enter to start Scenario 3: Full Information")
results_scenario_3 = run_simulation_scenario(players,reveal_percentages=True, plot_runs=True)
 