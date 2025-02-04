import math

##Linear neuarl network
x = float(input("Enter the value of input x: "))
w = float(input("Enter the value of weight w: "))
b = float(input("Enter the value of bias b: "))
net = x*w+b
if(net<0):
    out = 0
elif((net >= 0) and (net <= 1)):
    out = net
else:
    out =1

print("x : ",x)
print("b : ",b)
print("w : ",w)
print("output : ",out)

#binary & bipolar sigmodial
def binary_sigmoid(x):
    return 1 / (1 + math.exp(-x))

def bipolar_sigmoid(x):
    return (2 / (1 + math.exp(-x))) - 1

def calculate_output(x, w):
    y =0
    for i in range(0,len(x)):
        y = y + x[i] * w[i]
        
    binary_output = binary_sigmoid(y)
    bipolar_output = bipolar_sigmoid(y)
    
    return binary_output, bipolar_output
x = [0.3,0.5,0.6]   # Input
w = [0.2,0.1,-0.3]   # Weight
binary_output, bipolar_output = calculate_output(x, w)
print(f"Binary Sigmoid Output: {binary_output:.4f}")
print(f"Bipolar Sigmoid Output: {bipolar_output:.4f}")

##with bias
x = [0.2,0.6]
w = [0.3,0.7]
y = 0
b = 0.45

for(i in range(0,len(x)):
    y = y + x[i] * w[i]
y = y + b

print("x: ",x)
print("w: ",w)
print("y: ",round(y,3))

##AND/NOT MuCulloch-Pits
x1 = [0,0,1,1]
x2 = [0,1,0,1]
w1 = 1
w2 = -1
y = []
for(i in range(0,len(x1)):
    xm = x1[i]*w1+x2[1]*w2
if(xm <= 0):
    y.append(0)
else:
    y.append(1)
print("x1: ",x1)
print("x2: ",x2)
print("y: ",y)

##XOR using MuCulloch-Pits
x1 = [0,0,1,1]
x2 = [0,1,0,1]
w1 = 1
w2 = 1
y = []
for i in range(0,len(x1)):
    xm=x1[i]*w1+x2[i]*w2
    if(xm == 1):
        y.append(1)
    else:
        y.append(0)
print("x1: ",x1)
print("x2: ",x2)
print("y: ",y)

##Hebb Rule
x1=[1,1,1,-1,1,-1,1,1,1]
x2=[1,1,1,1,-1,1,1,,1,1]
b = 0

y0 = 1 #target output
y1 = -1 #target output

wtold = [0,0,0,0,0,0,0,0,0]
print("First input with target = 1")

for(i in range(0,9)):
    wtold[i] = wtold[i] + x1[i] * y0
b = b + y0
print("new weight = ",wtold)
print("Bia new value= ",b)

print("Second input with target -1")
for i in range(0,9):
    wtold[i] = wtold[i] + x1[i] * y1
b = b + y1
print("new weight = ",wtold)
print("Bias value = ",b)

##Back Propogation
a0 = -1 #Input for first layer
t  = -1 #Target Output

w10 = float(input("Enter weight of first network"))
b10 = float(input("Enter bias of first network"))
w20 = float(input("Enter weight of second network"))
b20 = float(input("Enter bias of second network"))
c = float(input("Enter the learning coffieient"))

n1 = float(w10 * a0 + b10)
a1 = math.tanh(n1)

n2 = float(w20 * a1 + b20)
a2 = math.tanh(float(n2))

e = t - a2

s2 = -2 * (1 - a2 * a2) * e  #gradient
s1 = (1 - a1 * a1) * w20 * s2 #gradient

w21 = w20 - (c *s2*a1) #updated weight
w11 = w10 - (c *s1*a0) #updated weight

b21 = b20 - (c * s2) #updated bias
b11 = b10 - (c * s1) #updated bias

##Self organinzing map
from minisom import Minisom
import matplotlib.pyplot as plt

data = [[0.80,0.55,0.22,0.03],
        [0.82,0.50,0.23,0.03],
        [0.80,0.54,0.26,0.03],
        [0.79,0.56,0.22,0.03],
        [0.75,0.60,0.25,0.03],
        [0.77,0.59,0.22,0.03]
        ]
Som = MiniSom(6,6,4,sigma = 0.3,learning_rate = 0.5)
Som.train_random(data,100)
plt.imshow(Som.distance().map())
plt.show()

##Hopefield Network
import numpy as np
import matplotlib.pyplot as plt
class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))  # Initialize weights as zeros

    def train(self, patterns):
        """Train the network using Hebbian learning."""
        for pattern in patterns:
            self.weights += np.outer(pattern, pattern)  # Update weights
        np.fill_diagonal(self.weights, 0)  # No self-connections

    def recall(self, pattern):
        """Recall a pattern from noisy input."""
        state = pattern.copy()
        for _ in range(5):  # Update for 5 steps
            for i in range(self.size):
                state[i] = 1 if np.dot(self.weights[i], state) > 0 else -1
        return state

    def plot_pattern(self, pattern):
        """Plot the pattern as a 3x3 grid."""
        plt.imshow(pattern.reshape(3, 3), cmap='gray')  # Display as a 3x3 grid
        plt.axis('off')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define simple patterns
    pattern1 = np.array([1, -1, 1, -1, 1, -1, 1, -1, 1])  # Checkerboard
    pattern2 = np.array([-1, 1, -1, 1, -1, 1, -1, 1, -1])  # Inverse of pattern1

    # Create Hopfield network
    net = HopfieldNetwork(9)

    # Train network with patterns
    net.train([pattern1, pattern2])

    # Plot original patterns
    net.plot_pattern(pattern1)
    net.plot_pattern(pattern2)

    # Create noisy version of patte
    noisy_pattern = pattern1.copy()
    noisy_pattern[2] = -noisy_pattern[2]  # Flip one bit
    recalled_pattern = net.recall(noisy_pattern)
    net.plot_pattern(recalled_pattern)

##Membership & Identity operator
    fruits = ['apple','banana','cherry','date']
    if 'banana' in fruits:
        print("Banan is in fruits lists")

    if 'orange' not in fruits:
        print("Orange is not in fruits lists")


    a = [1,2,3]
    b = a
    c = [1,2,3]

    if a is b:
        print("a & b refer to the same object")

    if a is not c:
        print("a & c do not refer to the same object")

    if b is a:
        print("b and a refer to the same object")

    if c is not b:
        print("c & b do not refer to the same object")

##Ratio Fuzzy
from fuzzywuzzy import fuzz  
from fuzzywuzzy import process  
s1 = "I love fuzzysforfuzzys" 
s2 = "I am loving fuzzysforfuzzys" 
print ("FuzzyWuzzy Ratio:", fuzz.ratio(s1, s2))  
print ("FuzzyWuzzyPartialRatio: ", fuzz.partial_ratio(s1, s2))  
print ("FuzzyWuzzyTokenSortRatio: ", fuzz.token_sort_ratio(s1, s2))  
print ("FuzzyWuzzyTokenSetRatio: ", fuzz.token_set_ratio(s1, s2))  
print ("FuzzyWuzzyWRatio: ", fuzz.WRatio(s1, s2),'\n\n') 
# for process library,  
query = 'fuzzys for fuzzys' 
choices = ['fuzzy for fuzzy', 'fuzzy fuzzy', 'g. for fuzzys']  
print ("List of ratios: ") 
print (process.extract(query, choices), '\n') 
print ("Best among the above list: ",process.extractOne(query, choices))

##Tipping

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the fuzzy variables
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Auto-membership functions for quality and service
quality.automf(3)
service.automf(3)

# Define tip categories
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Define rules
rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

# Create control system and simulation
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Input values
tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

# Compute the output
tipping.compute()

# Print result
print(tipping.output['tip'])

# Visualize the result
tip.view(sim=tipping)


##Genetic
import random

# Function to maximize: f(x) = x^2
def fitness(x):
    return x * x

# Generate a random individual (binary string)
def generate_individual():
    return random.randint(0, 31)  # Represent as a number between 0 and 31

# Main Genetic Algorithm
def genetic_algorithm(population_size=10, generations=50):
    population = [generate_individual() for _ in range(population_size)]  # Initialize population

    for gen in range(generations):
        # Sort the population based on fitness (descending order)
        population.sort(key=fitness, reverse=True)

        # Print the best solution of the generation
        best_individual = population[0]
        print(f"Generation {gen + 1}: Best fitness = {fitness(best_individual)} | Best individual = {best_individual}")

        # Elitism: Keep the best individual, remove the rest
        new_population = population[:2]  # Keep the top 2 individuals

        # Fill the rest of the population with mutated crossover offspring
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(population[:5], 2)  # Pick 2 random parents from top 5
            child = (parent1 + parent2) // 2  # Simple crossover: average of the two parents

            # Mutation: randomly change the child by +-1
            mutation = random.choice([-1, 1]) if random.random() < 0.1 else 0  # 10% mutation rate
            child += mutation

            new_population.append(child)

        population = new_population  # Set the new population for the next generation

    return population[0]  # Return the best individual

# Run the Genetic Algorithm
best_solution = genetic_algorithm()
print(f"Best solution found: {best_solution} with fitness = {fitness(best_solution)}")





                
        
        




    



