#!/bin/bash

pip install -r requirements.txt
cd src/antlr4
python3 Main.py ../../input_files/Samples/Full_Simulation.txt
#python3 Main.py ../input_files/Samples/Repeated_Id.txt
#python3 Main.py ../input_files/Samples/Wrong_State.txt
