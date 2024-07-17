import statistics
import math
data=[2.4,3.6,3.2]
x=statistics.geometric_mean(data)
print(x)


def probability_of_outperformance(num_quarters):
    p = 0.75  # Probability of outperformance in any quarter
    q = 1 - p  # Probability of underperformance in any quarter
    n = 4  # Number of quarters in a year

    # Calculate the probability of outperformance in three or fewer quarters
    probability = sum(math.comb(n, k) * (p ** k) * (q ** (n - k)) for k in range(num_quarters + 1))

    return probability

# Calculate the probability of outperformance in three or fewer quarters
probability_three_or_fewer = probability_of_outperformance(3)
print(probability_three_or_fewer)


# If the probability that a portfolio outperforms its benchmark in any quarter is 0.75, 
# the probability that the portfolio outperforms its benchmark in three or fewer quarters 
# over the course of a year is closest to:  

from scipy import stats
sum(stats.binom.pmf([0,1,2,3],4,0.75))

# Over the past 10 years, a company’s annual earnings increased year over year seven times and 
# decreased year over year three times. You decide to model the number of earnings increases 
# for the next decade as a binomial random variable.  
# Assuming the estimated probability is the actual probability for the next decade, what is 
# the probability that earnings will increase in 5 out of the next 10 years? 
'
from scipy import stats
k=5
n=10
p=0.7
x=round(100*sum(stats.binom.pmf([k],n,p)),2)
print("The {} probability that earnings will increase in {} out of the next {} years is {}%".format(p,k,n,x))

# A stock is priced at $100.00 and follows a one-period binomial process with an up move 
# that equals 1.05 and a down move that equals 0.97. If 1 million Bernoulli trials are 
# conducted, and the average terminal stock price is $102.00, the probability of an 
# up move (p) is closest to: 

up=1.05
down=0.97
stock_price=100
terminal_stock_price=102
p=(terminal_stock_price/stock_price-down)/(up-down)
print("The probability of an up move is {}".format(p))
# The probability of an up move (p) can be found by solving for p in the equation: (p)105 + (1 – p)97 = 102.

# In two rolls of a dice what is the probability of rolling a 1 or a 6 in the first roll and a 1 or a 6 in the second roll? 
# The probability of rolling a 1 or a 6 in the first roll is 2/6 = 1/3.
# The probability of rolling a 1 or a 6 in the second roll is also 1/3.
# The probability of both events occurring is 1/3 * 1/3 = 1/9.
