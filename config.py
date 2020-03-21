from __future__ import print_function
from os import getenv

NAME="ExampleExperiment"
EXPT_UID="UniqueID"
RESULTS_DIR="2020/ExampleExperiment/results"

# AWS Settings
AWS_DEFAULT_REGION = 'us-west-2'

# SimpleDB databases for experiments and participants
SDB_EXPERIMENTS = "mall_experiments"
SDB_EXPERIMENTS_PARTICIPANTS = "mall_experiments_participants"




DEBUG = True
if getenv('ExptEnv') == 'Production':
    DEBUG = False

if __name__ == "__main__":
    print(EXPT_UID)
