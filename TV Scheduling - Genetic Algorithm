import streamlit as st
import pandas as pd
import random
import csv

# Function to read the CSV file and convert it to the desired format
def read_csv_to_dict(file_path):
    program_ratings = {}
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        # Skip the header
        header = next(reader)
        for row in reader:
            program = row[0]
            ratings = [float(x) for x in row[1:]]  # Convert the ratings to floats
            program_ratings[program] = ratings
    return program_ratings

# Function Definitions for the Genetic Algorithm
def fitness_function(schedule, ratings):
    total_rating = 0
    for time_slot, program in enumerate(schedule):
        total_rating += ratings[program][time_slot]
    return total_rating

def crossover(schedule1, schedule2):
    crossover_point = random.randint(1, len(schedule1) - 2)
    child1 = schedule1[:crossover_point] + schedule2[crossover_point:]
    child2 = schedule2[:crossover_point] + schedule1[crossover_point:]
    return child1, child2

def mutate(schedule, all_programs):
    mutation_point = random.randint(0, len(schedule) - 1)
    new_program = random.choice(all_programs)
    schedule[mutation_point] = new_program
    return schedule

def genetic_algorithm(initial_schedule, ratings, all_programs, generations, population_size, crossover_rate, mutation_rate, elitism_size):
    population = [initial_schedule]
    for _ in range(population_size - 1):
        random_schedule = initial_schedule.copy()
        random.shuffle(random_schedule)
        population.append(random_schedule)

    for generation in range(generations):
        new_population = []
        # Elitism
        population.sort(key=lambda schedule: fitness_function(schedule, ratings), reverse=True)
        new_population.extend(population[:elitism_size])
        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population, k=2)
            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1.copy(), parent2.copy()

            if random.random() < mutation_rate:
                child1 = mutate(child1, all_programs)
            if random.random() < mutation_rate:
                child2 = mutate(child2, all_programs)

            new_population.extend([child1, child2])

        population = new_population

    return population[0]

# Streamlit Interface
st.title("TV Scheduling using Genetic Algorithm")
st.sidebar.header("Genetic Algorithm Parameters")
file_path = st.sidebar.text_input("Path to CSV File", value="program_ratings.csv")
generations = st.sidebar.number_input("Generations", min_value=10, max_value=500, value=100)
population_size = st.sidebar.number_input("Population Size", min_value=10, max_value=100, value=50)
crossover_rate = st.sidebar.slider("Crossover Rate (CO_R)", 0.0, 0.95, 0.8, 0.01)
mutation_rate = st.sidebar.slider("Mutation Rate (MUT_R)", 0.01, 0.05, 0.2, 0.01)
elitism_size = st.sidebar.number_input("Elitism Size", min_value=1, max_value=10, value=2)

if st.button("Run Genetic Algorithm"):
    ratings = read_csv_to_dict(file_path)
    all_programs = list(ratings.keys())
    all_time_slots = list(range(6, 24))

    # Initialize with a brute-force optimal schedule
    initial_schedule = random.sample(all_programs, len(all_time_slots))
    final_schedule = genetic_algorithm(
        initial_schedule,
        ratings,
        all_programs,
        generations,
        population_size,
        crossover_rate,
        mutation_rate,
        elitism_size,
    )

    # Display results
    schedule_data = {
        "Hour": [f"{hour}:00" for hour in all_time_slots],
        "Program": final_schedule,
    }
    st.table(pd.DataFrame(schedule_data))
