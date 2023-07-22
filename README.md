# Sudoku Solver

![Sudoku Solver](https://github.com/roguetitan1703/Sudoku_solver/blob/main/sudoku_static/sudoku_solver.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Challenges Faced](#challenges-faced)
- [Takeaways](#takeaways)
- [How to Use](#how-to-use)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Sudoku Solver is a Python project that provides a graphical user interface (GUI) for playing Sudoku and solving Sudoku puzzles. The goal of the project is to offer a user-friendly experience for Sudoku enthusiasts, allowing them to play the game and enjoy its challenges.

## Features

- **Interactive Sudoku Puzzle GUI**: The application offers an interactive and intuitive graphical interface to play Sudoku puzzles with ease.

- **Multiple Difficulty Levels**: Players can select from different difficulty levels, such as Easy, Medium, and Hard, to challenge themselves at different skill levels.

- **Solving the Sudoku Puzzle**: The solver employs a backtracking algorithm to find and display the correct solution for the given Sudoku puzzle.

- **Real-Time Timer**: The application includes a real-time timer that tracks the time spent on solving the puzzle.

- **Mistake Limit**: Users are allowed a certain number of mistakes. The application informs them of the mistakes made during the game.

- **Keyboard Input Support**: For a more efficient and engaging experience, players can use the keyboard to enter numbers into the Sudoku board.

## Technologies Used

- **Python**: The project is developed using Python, leveraging its object-oriented programming features for modularity and maintainability.

- **Tkinter**: The graphical user interface is built using Tkinter, a standard GUI library in Python, offering a platform-independent way to create GUI applications.

- **NumPy**: NumPy is used for efficient array handling and performing various operations on the Sudoku board.

- **Keyboard**: The Keyboard library is utilized for handling keyboard input, making it easy for users to interact with the Sudoku board.

- **Random**: The Random library is employed to generate random Sudoku boards with varying difficulty levels.

## Challenges Faced

During the development of Sudoku Solver, several challenges were encountered:

- **Graphical User Interface**: Designing and implementing the GUI using Tkinter required understanding widget management, event handling, and updating the interface based on user interactions.

- **Backtracking Algorithm**: Developing the backtracking algorithm to solve Sudoku puzzles efficiently involved understanding the recursive approach and optimizing it to find the correct solution.

- **Keyboard Input Handling**: Integrating keyboard input for number entry in the Sudoku board required mapping keyboard keys and handling user inputs effectively.

## Takeaways

The Sudoku Solver project provided valuable learning experiences and takeaways:

- **Algorithmic Problem-Solving**: Implementing the backtracking algorithm to solve Sudoku puzzles deepened the understanding of recursive approaches and problem-solving techniques.

- **Graphical User Interface Design**: Building the GUI with Tkinter improved skills in creating interactive and user-friendly interfaces.

- **Software Modularity**: Organizing the project into modules enhanced code reusability and maintainability.

- **Handling User Input**: Integrating keyboard input and event handling improved the understanding of managing user interactions in a GUI application.

## How to Use

1. Clone the repository to your local machine.
2. Ensure you have Python and the required libraries installed (Tkinter, NumPy, Keyboard).
3. Run the `run.py` file using Python to start the Sudoku Solver application.
4. Choose the desired difficulty level and start playing the Sudoku puzzle using the mouse or keyboard.

## Installation

To run the Sudoku Solver, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/roguetitan1703/Sudoku_solver.git
```

2. Install the required libraries (Tkinter, NumPy, Keyboard):

```
pip install tk numpy keyboard
```

3. Navigate to the project directory and run the `run.py` file:

```
cd Sudoku_solver
python run.py
```

## Contributing

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/roguetitan1703/Sudoku_solver/blob/main/LICENSE) file for details.
