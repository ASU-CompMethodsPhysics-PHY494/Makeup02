# PHY494: Makeup Homework 02
![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=main) ![Points badge](../../blob/badges/.github/badges/points.svg)

This is a **optional Makeup Assignment**. If you choose to hand it in
by the deadline, it will be graded like a normal homework
assignment. If its grade is better than your worst homework grade then
it will replace that grade.

* Follow the link in Canvas to set up your Makeup01 repository.

* `git clone` your repository to your laptop.

* Read the instructions ([makeup_02.pdf](makeup_02.pdf)).

* Work through the problem, check in your changes into your repository
  (`git add`, `git commit`), and `git push` your changes to the remote
  repository on GitHub.

**Tests and Autograding**: You can check that your code is correct and
that you include all necessary plots by running the following command
from the top of your working directory:

     pytest

To reduce output you may run

     pytest --tb=line

or

     pytest --tb=short

You can also redirect output to a file `TEST.txt` (or any name you choose)

     pytest > TEST.txt

and look at this file in an editor.

These tests are also ran automatically as soon as you push changes to
GitHub. Open the **Activity** tab and look for the *Autograding
Workflow* or check "pull request 1" (the Feedback pull request) in
your repository on GitHub to see results.

The result of the autograding tests are shown in the badge in the README on GitHub.




## Overview

1. Use a Laplace solver to compute the potential around a plate capacitor.
