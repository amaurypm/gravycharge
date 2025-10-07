# gravycharge
Calculate GRAVY and net charge for peptides.

This script will process line per line of peptide sequences in no given format and will generate
a CSV output with the peptide sequence, the GRAVY score (using Kyte-Doolittle Hydropathy Scale), and
the total charge at pH 7.0.
Each line is considered a different sequence.

These values are useful to estimate the relative hydrophobicity of peptides to be inserted in proteins.

## Usage
`gravycharge [-h] [-v] [input_file] [output_file]`

positional arguments:
  * `input_file`      Input sequence file [default: stdin].
  * `output_file`     Output file [default: stdout].

options:
  * `-h`, `--help`     Show this help message and exit
  * `-v`, `--version`  Show program's version number and exit.

## Installation
This is a Python script, so, you can just run the gravycharge.py file or put a symbolic link in any directory of your PATH.

## Dependencies
* Python3
* argparse
