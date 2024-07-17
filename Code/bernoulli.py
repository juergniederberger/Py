from scipy.stats import binom

def sum_binomial_probabilities(n, p, k):
    """
    Calculate the sum of binomial probabilities for k or less successes.
    
    Parameters:
        n (int): Number of trials.
        p (float): Probability of success in each trial.
        k (int): Maximum number of successes.
    
    Returns:
        float: Sum of binomial probabilities.
    """
    sum_prob = 0
    for i in range(k + 1):
        sum_prob += binom.pmf(i, n, p)
    return sum_prob

# Example usage
n = 7  # Number of trials
p = 0.7  # Probability of success
k = 4  # Maximum number of successes

sum_probabilities = sum_binomial_probabilities(n, p, k)
print(f"Sum of binomial probabilities for {k} or less successes: {sum_probabilities}")