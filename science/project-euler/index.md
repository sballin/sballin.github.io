<!-- {"full_title": "Project Euler",
"date_written": "Apr 14"} -->

# Problems from Project Euler

## Langton's Ant <a href="https://github.com/sballin/iterant"><i class="fa fa-github"></i></a>

This is a start toward solving problem [349](http://projecteuler.net/problem=349) from Project Euler:

> An ant moves on a regular grid of squares that are coloured either black or white. The ant is always oriented in one of the cardinal directions (left, right, up or down) and moves from square to adjacent square according to the following rules:

> - if it is on a black square, it flips the color of the square to white, rotates 90 degrees counterclockwise and moves forward one square.

> - if it is on a white square, it flips the color of the square to black, rotates 90 degrees clockwise and moves forward one square.

> Starting with a grid that is entirely white, how many squares are black after $10^{18}$ moves of the ant?

I made a Mathematica simulation to find the point around which the motion of the ant stops being random and enters a "highway."

<center><img src="{{top-path}}/{{article-path}}/ant.gif" width="250px"/></center>

After spending a lot of time at the beginning going through seemingly random configurations, the ant reaches a configuration that makes it "repeat" the same sequence and launch into a highway.

<!--  -->

Here's the code, which you can also find on [GitHub](https://github.com/sballin/iterant):

    (* Short-term to long-term behavior of Langton's ant. *)

    moveAnt[gridLen_, maxIts_]:=Module[{grid, antX, antY, dir, dirlist, i},
        grid = ConstantArray[0, {gridLen, gridLen}];
        antX = Floor[gridLen/2];
        antY = Floor[gridLen/2];
        dir  = -Pi/2;
        i    = 0;

        Do[
            (* if on white, make black, turn 90 deg counterclockwise *)
            If[grid[[antX, antY]] == 0,
                grid[[antX, antY]] = 1;
                dir  = dir+Pi/2;
                antX = antX+Cos[dir];
                antY = antY+Sin[dir];
            ]

            (* if on black, make white, turn 90 deg clockwise *)
            If[grid[[antX, antY]] == 1,
                grid[[antX, antY]] = 0;
                dir  = dir-Pi/2;
                antX = antX+Cos[dir];
                antY = antY+Sin[dir];
            ]
        ,{i, maxIts}];

        MatrixPlot[grid, ColorFunction -> "Monochrome"]
    ];

    (* allow scrubbing through number of iterations *)
    Manipulate[moveAnt[100, its], {{its, 0, "Iterations"}, 0, 8500,1}]

_February 2014._

## Billionaire

Project Euler problem 267:

>You are given a unique investment opportunity.

>Starting with £1 of capital, you can choose a fixed proportion, f, of your capital to bet on a fair coin toss repeatedly for 1000 tosses.

>Your return is double your bet for heads and you lose your bet for tails.

>For example, if f = 1/4, for the first toss you bet £0.25, and if heads comes up you win £0.5 and so then have £1.5. You then bet £0.375 and if the second toss is tails, you have £1.125.

>Choosing f to maximize your chances of having at least £1,000,000,000 after 1,000 flips, what is the chance that you become a billionaire?

>All computations are assumed to be exact (no rounding), but give your answer rounded to 12 digits behind the decimal point in the form 0.abcdefghijkl.

<center><object type="image/svg+xml" width="500px" data="{{top-path}}/{{article-path}}/predictions.svg">Your browser does not support SVG</object></center>

_April 2014._
