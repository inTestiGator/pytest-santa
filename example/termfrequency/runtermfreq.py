"""Run script for termfrequency"""
# !/usr/bin/env python
import sys

from termfrequency import tf_objectoriented, tf_pipeline

if __name__ == "__main__":

    # Run tf_objectoriented
    tf_objectoriented.WordFrequencyController(sys.argv[1]).run()

    # Run tf_pipeline
    tf_pipeline.run(sys.argv[1])
