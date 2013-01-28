#!/bin/bash

echo "1." >> stutest.out
gforth prob1 >> stutest.out
echo >> stutest.out

echo "2." >> stutest.out
gforth prob2 >> stutest.out
echo >> stutest.out

echo "3." >> stutest.out
gforth prob3 >> stutest.out
echo >> stutest.out

echo "4." >> stutest.out
gforth prob4 >> stutest.out
echo >> stutest.out

echo "5." >> stutest.out
gforth prob5 >> stutest.out
echo >> stutest.out

echo "6." >> stutest.out
gforth prob6 >> stutest.out
echo >> stutest.out

echo "7." >> stutest.out
gforth prob7 >> stutest.out
echo >> stutest.out

echo "8." >> stutest.out
gforth prob8 >> stutest.out
echo >> stutest.out

echo "9." >> stutest.out
gforth prob9 >> stutest.out
echo >> stutest.out

echo "10." >> stutest.out
gforth prob10 -e "-1 int_to_long d. CR BYE" >> stutest.out
gforth prob10 -e "0 int_to_long d. CR BYE" >> stutest.out
gforth prob10 -e "1 int_to_long d. CR BYE" >> stutest.out
echo >> stutest.out

echo "11." >> stutest.out
gforth prob11 -e "-1 fact . CR BYE" >> stutest.out
gforth prob11 -e "0 fact . CR BYE" >> stutest.out
gforth prob11 -e "1 fact . CR BYE" >> stutest.out
gforth prob11 -e "2 fact . CR BYE" >> stutest.out
echo >> stutest.out
