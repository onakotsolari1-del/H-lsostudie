import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


class HealthAnalyzer:
    """
    A class for analyzing the health study dataset.
    """
    def __init__(self, df):
        self.df = df

    def _fit_regression(self, X, y):
        """Fit a linear regression model and return model, R2 score, and RMSE."""
        model = LinearRegression()
        model.fit(X, y)

        predictions = model.predict(X)
        r2 = r2_score(y, predictions)
        rmse = np.sqrt(mean_squared_error(y, predictions))

        return model, r2, rmse

    def summary_statistics(self):
        """Return summary statistics for numeric variables."""
        columns = ["age", "height", "weight", "systolic_bp", "cholesterol"]
        return self.df[columns].agg(["mean", "median", "min", "max"])

    def disease_rate(self):
        """Calculate the proportion of participants with the disease."""
        return self.df["disease"].mean()

    def smoker_rate(self):
        """Calculate the proportion of smokers."""
        return (self.df["smoker"] == "Yes").mean()

    def linear_regression_age_bp(self):
        """
        Perform a simple linear regression using age to predict systolic blood pressure.
        Returns model, R2 score, and RMSE.
        """
        X = self.df[["age"]]
        y = self.df["systolic_bp"]
        return self._fit_regression(X, y)

    def multiple_regression_bp(self):
        """
        Predict systolic blood pressure using age, weight, and cholesterol.
        Returns model, R2 score, and RMSE.
        """
        X = self.df[["age", "weight", "cholesterol"]]
        y = self.df["systolic_bp"]
        return self._fit_regression(X, y)

    def run_pca(self):
        """
        Perform PCA on numerical features to identify patterns in data.
        Returns pca object and DataFrame with component loadings.
        """
        features = ["age", "height", "weight", "systolic_bp", "cholesterol"]
        X = self.df[features].dropna()

        # Standardize data (z-score normalization)
        X_scaled = (X - X.mean()) / X.std()

        pca = PCA(n_components=2, random_state=42)
        components = pca.fit_transform(X_scaled)

        plt.figure(figsize=(8, 5))
        scatter = plt.scatter(
            components[:, 0],
            components[:, 1],
            c=self.df.loc[X.index, "disease"],
            cmap="viridis",
            alpha=0.7
        )
        plt.title("PCA - Patterns in Health Data")
        plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)")
        plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)")
        cbar = plt.colorbar(scatter)
        cbar.set_label("Disease (0/1)")
        plt.grid(True, alpha=0.3)
        plt.show()

        return pca, pd.DataFrame(pca.components_, columns=features, index=["PC1", "PC2"])

    def plot_age_bp(self):
        """Plot age versus systolic blood pressure with a regression line."""
        model, _, _ = self.linear_regression_age_bp()

        x_min = self.df["age"].min()
        x_max = self.df["age"].max()
        x_sort_values = np.linspace(x_min, x_max, 100).reshape(-1, 1)

        # Convert to DataFrame with column name "age" to avoid UserWarning
        x_sort_df = pd.DataFrame(x_sort_values, columns=["age"])
        y_sort_pred = model.predict(x_sort_df)

        plt.figure(figsize=(8, 5))
        plt.scatter(self.df["age"], self.df["systolic_bp"], alpha=0.5, label="Data points")
        plt.plot(x_sort_df["age"], y_sort_pred, color="red", linewidth=2, label="Regression Line")
        plt.xlabel("Age")
        plt.ylabel("Systolic Blood Pressure")
        plt.title("Age vs Blood Pressure")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

    def plot_disease_by_sex(self):
        """Plot disease rate by sex."""
        disease_by_sex = self.df.groupby("sex")["disease"].mean()
        plt.figure(figsize=(6, 4))
        disease_by_sex.plot(kind="bar", color=["skyblue", "salmon"], edgecolor="black")
        plt.title("Disease Rate by Sex")
        plt.xlabel("Sex")
        plt.ylabel("Disease Rate")
        plt.xticks(rotation=0)
        plt.grid(axis="y", alpha=0.3)
        plt.show()

    def plot_bp_histogram(self):
        """Plot the distribution of systolic blood pressure."""
        plt.figure(figsize=(8, 5))
        plt.hist(self.df["systolic_bp"], bins=20, edgecolor="black", color="skyblue")
        plt.title("Distribution of Systolic Blood Pressure")
        plt.xlabel("Systolic Blood Pressure")
        plt.ylabel("Frequency")
        plt.grid(True, alpha=0.3)
        plt.show()

    def plot_bp_by_smoker(self):
        """Compare blood pressure by smoking status."""
        plt.figure(figsize=(6, 4))
        self.df.boxplot(column="systolic_bp", by="smoker")
        plt.title("Blood Pressure by Smoking Status")
        plt.suptitle("")
        plt.xlabel("Smoker")
        plt.ylabel("Systolic Blood Pressure")
        plt.grid(True, alpha=0.3)
        plt.show()


    def plot_correlation_heatmap(self):
        """
        Plot a correlation heatmap for the numerical features.
        Helps identify relationships between variables.
        """
        features = ["age", "height", "weight", "systolic_bp", "cholesterol"]
        corr = self.df[features].corr()

        plt.figure(figsize=(8, 6))
        plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
        plt.colorbar(label="Correlation")
        plt.xticks(range(len(features)), features, rotation=45, ha="right")
        plt.yticks(range(len(features)), features)
        
        # Add correlation values on the heatmap
        for i in range(len(features)):
            for j in range(len(features)):
                plt.text(j, i, f"{corr.iloc[i, j]:.2f}", 
                        ha="center", va="center", color="black", fontsize=9)
        
        plt.title("Correlation Heatmap of Health Variables")
        plt.tight_layout()
        plt.show()
        
        return corr 