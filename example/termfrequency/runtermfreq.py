"""Run script for termfrequency"""
# !/usr/bin/env python
import sys
from termfrequency.cp_termfrequency import WordFrequencyController


WordFrequencyController(sys.argv[1]).run()
