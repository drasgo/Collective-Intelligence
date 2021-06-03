# EmbodiedAI 2021
This repository contains the practical materials for the Embodied Artificial Intelligence course.

## Installation
To run this software, install the dependencies by running

    python3 -m pip install -r requirements.txt --user

## How it works
To run the code simply execute the main.py file. For more detailed overview of the code structure and functionality, please see the supplementary document 'CodeTutorial'.

## Documentation
If you want to auto generate the documentation, just run in the terminal in the main folder
    
    pdoc3 --html .


## NOTE

There is a known bug that may (rarely) crash the program in random occasions when the number of agents is very high 
(especially if your computer is not very performant), regarding the memory usage of pygame.
When this bug appears, just waiting couple of seconds and re-running the program should
fix it

We are actively working for fixing this. 


## Examples Assignment 1: 

About Stage 1:

![Output sample](gifs/Assignment1/demo_pt0.gif)


About Experiment 1:


![alt text](gifs/Assignment1/demo_pt1.PNG)


About Experiment 2:


![alt text](gifs/Assignment1/demo_pt2.png)



## Examples Assignment 2:

SIR model:

![Output sample](gifs/Assignment2/covid.gif)

Simplified lockdown:

![Output sample](gifs/Assignment2/covid1.gif)

