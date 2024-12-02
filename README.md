# Lung-Cancer-Sim
Lung Cancer Simulation for AP CSP. Group members: Ritchy Samedy, Gaetano Foster

## Features

* Generate Random DNA Sequences:
  * Produces a sequence of 20 nucleotides (A, T, G, C) as the starting point.

* Transcription and Reverse Transcription:
  * Converts DNA to RNA and back, simulating real biological processes.

* Random Mutations:
  * Includes substitution, insertion, and deletion mutations, with mutation likelihood adjusted based on smoking status:
    * Control group: 20% chance
    * Smokers: 65% chance

* Interactive User Input:
  * Asks the user whether they smoke to determine mutation probability.

* Mutation Tracking:
  * Counts the total mutations, substitutions, insertions, and deletions across replication cycles.

* Cancer Simulation:
  * Evaluates the number of mutations and outputs a simulated diagnosis based on thresholds.

## Example Output

```
DNA Sequence: ['A', 'T', 'G', 'C', ...]
Generation 1: ['U', 'A', 'C', 'G', ...]
Substitution of G for A at 4
...
Total mutations: 5
Your lung tissue cells are mutating rapidly. You unfortunately have developed lung cancer.
Total substitutions: 2
Total insertions: 1
Total deletions: 2
```
