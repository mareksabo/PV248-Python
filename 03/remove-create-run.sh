#! /bin/bash

rm scorelib.dat
sqlite3 scorelib.dat < scorelib.sql
python3 03.py
