import streamlit as st
import csv
import random

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

# Fitness function
def fitness_function(schedule, ratings):
    total_rating = 0
    for time_slot, program in enumerate(schedule):
        total_rating += ratings[program][time_slot]
    return total_rating

# Crossover
def crossover(schedule1, schedule2):
    crossover_point = random.randint(1, len(schedule1) - 2)
    child1 = schedule1[:crossover_point] + schedule2[crossover_point:]
    child2 = schedule2[:crossover_point] + schedule1[crossover_point:]
    return child1, child2

# Mutation
def mutate(schedule, all_programs):
    mutation_point = random.randint(0, len(schedule) - 1)
    new_program = random.choice(all_programs)
    schedule[mutation_point] = new_program
    return schedule

# Genetic Algorithm
def genetic_algorithm(ratings, initial_schedule, generations, population_size, crossover_rate, mutation_rate, elitism_size, all_programs):
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

# Main Streamlit App
st.title("TV Scheduling Optimization using Genetic Algorithm")

# File input
uploaded_file = st.file_uploader("Upload the Modified_TV_Scheduling.csv file", type="csv")

if uploaded_file:
    ratings = read_csv_to_dict(uploaded_file)
    all_programs = list(ratings.keys())
    all_time_slots = list(range(6, 24))
    initial_schedule = random.sample(all_programs, len(all_programs))

    # Input parameters for Genetic Algorithm
    st.sidebar.header("Genetic Algorithm Parameters")
    CO_R = st.sidebar.slider("Crossover Rate (CO_R)", 0.0, 0.95, 0.8)
    MUT_R = st.sidebar.slider("Mutation Rate (MUT_R)", 0.01, 0.05, 0.02)
    GEN = st.sidebar.number_input("Generations (GEN)", 10, 500, 100, step=10)
    POP = st.sidebar.number_input("Population Size (POP)", 10, 100, 50, step=10)
    EL_S = st.sidebar.number_input("Elitism Size (EL_S)", 1, 10, 2)

    # Run Genetic Algorithm
    st.header("Resulting Schedule")
    schedule = genetic_algorithm(
        ratings=ratings,
        initial_schedule=initial_schedule,
        generations=GEN,
        population_size=POP,
        crossover_rate=CO_R,
        mutation_rate=MUT_R,
        elitism_size=EL_S,
        all_programs=all_programs,
    )
    schedule_table = {
        "Time Slot": [f"{slot:02d}:00" for slot in all_time_slots],
        "Program": schedule,
    }
    st.table(schedule_table)
    st.write(f"Total Ratings: {fitness_function(schedule, ratings)}")
