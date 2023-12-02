#!/bin/python3
import subprocess
import sys

for line in sys.stdin:
    path = line.strip()

    # Print the raw input line to help identify any issues
    print(f"Raw input line: {path}")

    # Use 'hadoop fs -ls' to list files in the HDFS directory
    command = "hadoop fs -ls {}".format(path)
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print the 'hadoop fs -ls' output
    print(f"ls_output: {process}")

""" # Process the 'hadoop fs -ls' output to extract file names
    file_names = [line.split()[-1] for line in ls_output.strip().split('n') if line.strip()]

    # Print the extracted file names
    for file_name in file_names:
        print(f"Processing line: {file_name}")"""
