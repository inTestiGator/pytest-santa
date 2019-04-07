"""Run script for termfrequency"""
# !/usr/bin/env python
import sys
from tf_objectoriented import WordFrequencyController
from tf_pipeline import run

# Run tf_objectoriented
WordFrequencyController(sys.argv[1]).run()

# Run tf_pipeline
run(sys.argv[1])
