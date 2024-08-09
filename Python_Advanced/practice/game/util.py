import random
import matplotlib.pyplot as plt

# Parameters for the normal distribution
mu = 0    # Mean
sigma = 1  # Standard deviation

# Generate a sample of 1000 random numbers from the normal distribution
samples = [random.gauss(mu, sigma) for _ in range(10000)]

players = [Players(generate_random_player_id(), actual_rating = random.gauss(1000, 100)) for _ in range(1000)]

# Plot the histogram
plt.hist(samples, bins=100, edgecolor='black')

# Add titles and labels
plt.title('Histogram of Samples from a Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()