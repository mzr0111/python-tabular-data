import pandas as pd  #handling the data
import matplotlib.pyplot as plt  #creating the plots
from scipy import stats  #performing the linear regression

def read_data(file_path):    #Defines a function called read_data that takes a single argument, file_path.
    return pd.read_csv(file_path)   #Reads the CSV file at the provided file path into a pandas DataFrame and returns it

def linear_regression(x, y):    #Defines a function called linear_regression that takes two arguments, x and y.
    regression = stats.linregress(x, y)     #Performs linear regression on the given data and stores the result in a variable called regression.
    return regression.slope, regression.intercept    #Returns a tuple containing the slope and intercept of the regression line.

def plot_species_regression(dataframe, species):   #Defines a function called plot_species_regression that takes two arguments, dataframe and species.
    species_data = dataframe[dataframe.species == species] #Filters the DataFrame to include only the rows corresponding to the given species and stores it in a variable called species_data.

    x = species_data.petal_length_cm    #Extracts the petal length and sepal length columns from species_data and stores them in variables x and y, respectively.
    y = species_data.sepal_length_cm

    slope, intercept = linear_regression(x, y)   #Performs linear regression on the extracted data and stores the slope and intercept in corresponding variables.

    plt.scatter(x, y, label=f'{species} Data')   #Creates a scatter plot of the extracted data and labels it with the species name.
    plt.plot(x, slope * x + intercept, label=f'{species} Fitted Line')  #Plots the regression line on the same axes as the scatter plot and labels it with the species name.

    plt.xlabel("Petal length (cm)")   #Sets the x-axis and y-axis labels for the plot.
    plt.ylabel("Sepal length (cm)")
    plt.legend()   #Adds a legend to the plot.
    plt.savefig(f"{species}_petal_v_sepal_length_regress.png")  #Saves the plot as a PNG file with a name based on the species.
    plt.clf()   #Clears the current figure, so the next plot starts with a clean slate.


def main(): #Defines the main function, which is the entry point of the script.
    dataframe = read_data("iris.csv")   #Reads the iris.csv file into a DataFrame and stores it in a variable called dataframe.

    species_list = ["Iris_setosa", "Iris_versicolor", "Iris_virginica"]   #Creates a list of the three Iris species.

    for species in species_list:    #Iterates through the species list and calls plot_species_regression for each species.
        plot_species_regression(dataframe, species)


if __name__ == '__main__':
    main()
