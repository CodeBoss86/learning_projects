import matplotlib.pyplot as plt

from die import Die

# Creating two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some roll and store result in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range (2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
plt.title("Result of rolling two D6 dice 1000 times.")
plt.xticks(["2", '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
plt.xlabel("Result")
plt.ylabel("Frequency of Result")
plt.plot(results, frequencies)

plt.show()