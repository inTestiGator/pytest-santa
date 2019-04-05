"""Run script for termfrequency"""
# !/usr/bin/env python
import sys
from cp_termfrequency import WordFrequencyController


WordFrequencyController(sys.argv[1]).run()
