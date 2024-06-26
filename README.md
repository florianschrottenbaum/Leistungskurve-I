# Leistungskurve-I
## Description
The Leistungskurve-I is a project designed to import data, sort the data (descending), create a plot with the sorted data and save the `.png` file into a new folder titled figures.
## Features
- Imports data from activity.csv (load_data.py)
- Sorts data. (sort.py)
- Creates a plot (plot.py).
- Saves the plot as a `.png` file into a new folder. (plot.py)
- The code was written by using a venv. 
## How to Use
1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/florianschrottenbaum/Leistungskurve-I
    ```
2. Make sure you have Python installed.
3. Install the required packages, if not installed yet:
    ```bash
    pip install numpy matplotlib
    ```
4. To execute the project, run the `main.py` file:
     ```bash
    python main.py
    ```
5. Find the generated `.png` file named `PowerLight.png` in the folder `figures`.