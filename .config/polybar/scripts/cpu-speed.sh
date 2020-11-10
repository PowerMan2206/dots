#!/bin/bash

# shows the CPU speed in MHz
 echo $(lscpu | grep "CPU MHz"  | cut -d":" -f2 | tr -d ' ' | cut -d"." -f1) MHz
