import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

class HealthAnalyzer:
    """
    A class for analyzing the health study dataset.
    """

    def __init__(self, df):
        """
        Initialize the analyzer with a dataframe.

        Parameters:
        ----------
        df : pandas.DataFrame
            The health study dataset.
        """
        self.df = df

    def summary_statistics(self):
        """
        Return summary statistics for numeric variables.
        """

        columns = [
            "age",
            "height",
            "weight",
            "systolic_bp",
            "cholesterol"
        ]

        return self.df[columns].agg(
            ["mean", "median", "min", "max"]
        )
    def disease_rate(self):
        """
        Calculate the proportion of participants
        with the disease.
        """

        return self.df["disease"].mean()
    
    def smoker_rate(self):
        """
        Calculate the proportion of smokers.
        """

        return (self.df["smoker"] == "Yes").mean()

    
    def linear_regression_age_bp(self):
        """
        Perform a linear regression using age
        to predict systolic blood pressure.
        """

        X = self.df[["age"]]
        y = self.df["systolic_bp"]

        model = LinearRegression()

        model.fit(X, y)

        return model

    
    def plot_age_bp(self):
        """
        Plot age versus systolic blood pressure
        with a regression line.
        """

        X = self.df[["age"]]

        y = self.df["systolic_bp"]

        model = LinearRegression()

        model.fit(X, y)

        plt.figure(figsize=(8, 5))

        plt.scatter(
            self.df["age"],
            self.df["systolic_bp"],
            alpha=0.5
        )

        plt.plot(
            self.df["age"],
            model.predict(X),
            color="red"
        )

        plt.xlabel("Age")
        plt.ylabel("Systolic Blood Pressure")
        plt.title("Age vs Blood Pressure")

        plt.show()

    def multiple_regression_bp(self):
        """
        Predict systolic blood pressure using
        age, weight and cholesterol.
        """

        X = self.df[
        ["age", "weight", "cholesterol"]
        ]

        y = self.df["systolic_bp"]

        model = LinearRegression()

        model.fit(X, y)

        return model

    
    def plot_disease_by_sex(self):
        """
        Plot disease rate by sex.
        """

        disease_by_sex = (
            self.df.groupby("sex")["disease"]
            .mean()
        )

        disease_by_sex.plot(
            kind="bar",
            color=["skyblue", "salmon"]
        )

        plt.title("Disease Rate by Sex")
        plt.xlabel("Sex")
        plt.ylabel("Disease Rate")

        plt.show()
    def plot_bp_histogram(self):
        """
        Plot the distribution of systolic blood pressure.
        """

        plt.figure(figsize=(8, 5))

        plt.hist(
            self.df["systolic_bp"],
            bins=20,
            edgecolor="black"
        )

        plt.title("Distribution of Systolic Blood Pressure")
        plt.xlabel("Systolic Blood Pressure")
        plt.ylabel("Frequency")

        plt.show()

    def plot_bp_by_smoker(self):
        """
        Compare blood pressure by smoking status.
        """

        self.df.boxplot(
            column="systolic_bp",
            by="smoker"
        )

        plt.title("Blood Pressure by Smoking Status")
        plt.suptitle("")
        plt.xlabel("Smoker")
        plt.ylabel("Systolic Blood Pressure")

        plt.show()