import random as r

DNA_NUCLEOTIDES = ['A', 'T', 'G', 'C'] # List of the 4 possible nucleotides in a dna sequence
RNA_NUCLEOTIDES = ['U', 'A', 'C', 'G'] # List of the 4 possible nucleotides in an rna sequence
                             # They are in opposite orders for easy converting

CONTROL_MUTATION_CHANCE = 0.2 # 20% chance of mutating each replication cycle
SMOKER_MUTATION_CHANCE = 0.65 # 65% chance of mutating each replication cycle
# ^ not necessarily realistic numbers, just estimates based on the given program

n_substitutions = 0
n_insertions = 0
n_deletions = 0
n_mutations = 0
n_generations = 1

def generate_dna_sequence():
    sequence = []
    for i in range(20):
        sequence.append(DNA_NUCLEOTIDES[r.randint(0, 3)])
    return sequence

def rna_from_dna(dna): # transcribes dna sequence into corresponding rna sequence
    rna = []
    for n in dna:
        rna.append(RNA_NUCLEOTIDES[DNA_NUCLEOTIDES.index(n)])
    return rna

def dna_from_rna(rna): # transcribes back
    dna = []
    for n in rna:
        dna.append(DNA_NUCLEOTIDES[RNA_NUCLEOTIDES.index(n)])
    return dna

def substitute_at_pos(rna, pos, val):
    print('Substitution of ' + str(rna[pos]) + ' for ' + str(val) + ' at ' + str(pos))
    rna[pos] = val

def insert_at_pos(rna, pos, val):
    print('Insertion of ' + str(val) + ' at ' + str(pos))
    rna.insert(pos, val)

def delete_at_pos(rna, pos):
    print('Deletion of ' + str(rna[pos]) + ' at position ' + str(pos))
    del rna[pos]

def mutate(rna): # randomly does one of the 3 mutation types (substitute, delete, insert)
    global n_substitutions
    global n_insertions
    global n_deletions
    global n_mutations
    mutation = r.randint(1, 3)

    if mutation == 1:
        substitute_at_pos(rna, r.randint(0, len(rna) - 1), RNA_NUCLEOTIDES[r.randint(0, 3)])
        n_substitutions += 1
    elif mutation == 2:
        insert_at_pos(rna, r.randint(0, len(rna) - 1), RNA_NUCLEOTIDES[r.randint(0, 3)])
        n_insertions += 1
    elif mutation == 3:
        delete_at_pos(rna, r.randint(0, len(rna) - 1))
        n_deletions += 1

    n_mutations += 1


def replicate(dna, pct):
    global n_generations
    rna = rna_from_dna(dna)
    if r.random() <= pct: # Only mutate (pct)% of the time
        mutate(rna)
    print('Generation ' + str(n_generations) + ': ' + str(rna))
    n_generations += 1

    return dna_from_rna(rna)

dna = generate_dna_sequence()
smoker = input('Are you a smoker?')
chance = 0

if smoker == 'yes':
    chance = SMOKER_MUTATION_CHANCE
else: # Assumed no
    chance = CONTROL_MUTATION_CHANCE

for i in range(10):
    print('DNA Sequence: ' + str(dna))
    dna = replicate(dna, chance)

print('Total mutations: ' + str(n_mutations))

if n_mutations > 4:
    print('Your lung tissue cells are mutating rapidly. You unfortunately have developed lung cancer.')
else:
    print('You do not have lung cancer.')

print('Total substitutions: ' + str(n_substitutions))
print('Total insertions: ' + str(n_insertions))
print('Total deletions: ' + str(n_deletions))
