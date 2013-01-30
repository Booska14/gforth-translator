
." Problem 1" CR
." Hello World" CR


." Problem 2" CR
15 3 * 4 + 10 2 / - 7 - . CR

." Problem 3" CR
15.0e 3.0e f* 4.0e f+ 10.0e 2.0e f/ f- 7.0e f- f. CR

." Problem 4" CR
15.0e0 3.0e0 f* 4.0e0 f+ 10.0e0 2.0e0 f/ f- 7.0e0 f- f. CR

." Problem 5" CR
15 s>f 3.0e0 f* 4.0e0 f+ 10 s>f 2.0e0 f/ f- 7 s>f f- f. CR

." Problem 6" CR
: y 15 ;
: x 3.0e0 ;
y s>f x f* 4.0e0 f+ 10 s>f 2 s>f f/ f- 7 s>f f- f. CR

." Problem 7" CR
: problem7
2 3 < if 5 else 1 endif . ;
problem7 CR

." Problem 8" CR
\ renamed variables to avoid duplicate values
\ x = x1
\ y = y1
: x1 2 ;
: y1 3 ;
: problem8
x1 y1 > if 5 else 1 endif . ;
problem8 CR


." Problem 9" CR
: problem9
11 5 ?DO  i . LOOP ;
problem9 CR


." Problem 10 " CR
: convertint
s>d ;
10 convertint . CR

." Problem 11" CR
: fact recursive
dup 0 > if
    dup 1 - fact *
else
    drop 1
endif ;
5 dup . fact . CR


bye
