#!/bin/bash
for i in {1..50}
do
    ./sud2sat3 <puzzle${i}.txt >puzzle${i}.cnf
    minisat puzzle${i}.cnf out${i}.txt >>per_test3.txt
    rm puzzle${i}.txt
    rm puzzle${i}.cnf
done