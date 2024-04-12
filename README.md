# Leistungskurve-I
## Description
The Leistungskurve-I is a project designed to import data, sort the data (descending), create a plot with the sorted data and save the `.png` file into a new folder titled figures.
## Features
- Imports data from activity.csv (load_data.py)
- Sorts data. (sort.py)
- Creates a plot (in main.py).
- Saves the plot as a `.png` file into a new folder. (in main.py)
- The code was written by using a venv. 
## How to Use
1. Clone this repository to your local machine.
2. Make sure you have Python installed.
3. Install the required packages, if not installed yet:
    ```bash
    pip install numpy matplotlib
    pip install numpy
    ```
4. To execute the project, run the `main.py` file:
     ```bash
    python main.py
    ```
5. Find the generated `.png` file named `PowerOriginal.png` in the folder `figures`.