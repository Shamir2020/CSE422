import random

class RunPredictor:
    def __init__(self,count,batsmen,targetRuns,iterations):
        self.count = count
        self.batsmen = batsmen
        self.targetRuns = targetRuns
        self.mutation_rate = 0.1
        self.iterations = iterations

    def Selection(self):
        return [random.choice([0,1]) for i in range(self.count)]

    def CalcFitness(self,selected_batsmen):
        total_runs = sum(self.batsmen[i][1] for i in range(self.count) if selected_batsmen[i])
        return abs(total_runs - target_runs)

        return abs(totalRuns - self.targetRuns)

    def crossover(self,father,mother):
        cross_point = random.randint(1,self.count-1)
        baby1 = father[:cross_point] + mother[cross_point:]
        baby2 = mother[:cross_point] + father[cross_point:]

        return baby1, baby2

    def mutation(self,selectedBatsmen):
        mutated_batsmen = selectedBatsmen.copy()
        for i in range(self.count):
            if random.random() < self.mutation_rate:
                mutated_batsmen[i] = 1 - mutated_batsmen[i]

        return mutated_batsmen


    def createFirstGeneration(self,size):
        return [self.Selection() for i in range(size)]

    def main(self,size):
        population = self.createFirstGeneration(size)

        for generation in range(self.iterations):
            fitnessScore = [self.CalcFitness(selected_batsmen) for selected_batsmen in population]

            if min(fitnessScore) == 0:
                 index = fitnessScore.index(0)
                 return population[index]

            generation2 = []
            for i in range(size):
                father, mother = random.choices(population, weights=[1 / fit for fit in fitnessScore], k=2)
                child1, child2 = self.crossover(father, mother)
                generation2.extend([self.CalcFitness(child1, self.mutation_rate), self.mutation(child2, self.mutation_rate)])

        population = generation2

        return -1

print('Input:')

count, target_runs = input().split(' ')
count = int(count)
target_runs = int(target_runs)
batsmen = []
for i in range(count):
    name, runs = input().split(' ')
    runs = int(runs)
    batsmen.append([name,runs])

population_size = 30
mutation_rate = 0.1
iterations = 1100
# count = 8
# batsmen = [
#     ['Tamim',68],
#     ['Soumya',25],
#     ['Shakib',70],
#     ['Afif',53],
#     ['Mushfiq',71],
#     ['Liton',55],
#     ['Mahmudullah',66],
#     ['Shanto',29]
# ]
iterations = 1100
population_size = 1100

runpredictor = RunPredictor(count,batsmen,target_runs,iterations)

x = runpredictor.main(population_size)
print(batsmen)
print(x)
