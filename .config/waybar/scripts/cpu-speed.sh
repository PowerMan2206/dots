#!/bin/bash

# shows the CPU speed in MHz and temp in C
echo $(lscpu | grep "CPU MHz" | cut -d":" -f2 | tr -d ' ' | cut -d"." -f1) MHz $(sensors | grep "Tdie" | cut -d":" -f2 | tr -d ' ' | cut -d"+" -f2)
