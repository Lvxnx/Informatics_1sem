import csv
import matplotlib.pyplot as plt

SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm = [], [], [], []

def plotting(x, y, xlabel, ylabel):
    title = ylabel + " VS " + xlabel
    plt.title(title, fontsize=15)
    plt.xlabel(xlabel +", cm")
    plt.ylabel(ylabel +", cm")
    plt.scatter(x, y, s=3, c='k')
    plt.savefig(title+".png")

with open("iris_data.csv","r") as data_file:
    data_reader = csv.reader(data_file, delimiter=",")

    for row in data_reader:
        if row[0] != "Id":
            SepalLengthCm.append(float(row[1]))
            SepalWidthCm.append(float(row[2]))
            PetalLengthCm.append(float(row[3]))
            PetalWidthCm.append(float(row[4]))

    plotting(SepalLengthCm, SepalWidthCm, "Sepal Length", "Sepal Width")
    plotting(SepalLengthCm, PetalLengthCm, "Sepal Length", "Petal Length")
    plotting(SepalLengthCm, PetalWidthCm, "Sepal Length", "Petal Width")
    plotting(SepalWidthCm, PetalLengthCm, "Sepal Width", "Petal Length")
    plotting(SepalWidthCm, PetalWidthCm, "Sepal Width", "Petal Width")
    plotting(PetalLengthCm, PetalWidthCm, "Petal Length", "Petal Width")

    # plt.show()
