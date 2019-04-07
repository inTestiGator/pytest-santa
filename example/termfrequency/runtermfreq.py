"""Run script for termfrequency"""
# !/usr/bin/env python
import sys
from termfrequency.tf_objectoriented import WordFrequencyController
from termfrequency.tf_pipeline import run

# Run tf_objectoriented
WordFrequencyController(sys.argv[1]).run()

# Run tf_pipeline
run(sys.argv[1])
