#!/usr/bin/env python3
## Calculate GRAVY and net charge for peptides.
##
## This script will process line per line of peptide sequences in no given format and will generate
## a CSV output with the peptide sequence, the GRAVY score (using Kyte-Doolittle Hydropathy Scale), and
## the total charge at pH 7.0
## Each line is considered a different sequence.
##
## Amaury Pupo Merino
## amaury.pupo@gmail.com
##
## This script is released under GPL v3.
##

## Importing modules
import argparse
import sys

# Define the Kyte-Doolittle Hydropathy Scale (for GRAVY calculation)
# Values: F, I, L, V, M, C, A, G, P, T, S, Y, W, H, Q, N, E, K, D, R
GRAVY_SCALE = {
    'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
    'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
    'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
    'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

# Define charge at pH ~7
CHARGE_AT_PH7 = {
    # Basic (+1)
    'R': 1, 'K': 1,
    # Acidic (-1)
    'D': -1, 'E': -1,
    # Histidine (often approximated as 0.1 to 0.5, using 0 for simplicity or 0.5 for a 'worst-case' basic estimate)
    'H': 0.0, # Using 0.0 for a conservative estimate at pH 7.0
    # Neutral (0)
    'A': 0, 'C': 0, 'G': 0, 'I': 0, 'L': 0, 'M': 0, 'F': 0, 
    'P': 0, 'S': 0, 'T': 0, 'W': 0, 'Y': 0, 'V': 0, 'N': 0, 'Q': 0 
}

## Functions

def calculate_gravy(sequence):
    """Calculates the GRAVY coefficient for the peptide."""
    total_hydropathy = sum(GRAVY_SCALE.get(res, 0) for res in sequence)
    return total_hydropathy / len(sequence) if sequence else 0

def calculate_net_charge(sequence):
    """
    Calculates the total net charge at pH ~7, including termini.
    Assumes standard N-terminus (+1) and C-terminus (-1).
    """
    charge_sum = sum(CHARGE_AT_PH7.get(res, 0) for res in sequence)
    # Add terminal charges: +1 for N-terminus, -1 for C-terminus
    # terminal_charge = 1 + (-1) # Assumes standard, unmodified termini
    return charge_sum

## Main
def main():
    """Main function.
    """
    parser=argparse.ArgumentParser(description="Calculate GRAVY and net charge for peptides.")
    parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input sequence file [default: stdin].')
    parser.add_argument('output_file', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='Output file [default: stdout].')
    parser.add_argument('-v', '--version', action='version', version='1.0.0', help="Show program's version number and exit.")

    args=parser.parse_args()

    args.output_file.write("sequence,GRAVY,net_charge_at_pH_7\n")

    for pep_seq in args.input_file:
        pep_seq=pep_seq.strip().upper()        
        args.output_file.write(f"{pep_seq},{calculate_gravy(pep_seq): .2f},{calculate_net_charge(pep_seq): .1f}\n")                
                  

## Running the script
if __name__ == "__main__":
        main()
