import sweetviz as sv
import pandas as pd


# Load the dataset
dataset_path = "heart_2020_cleaned.csv" 
data = pd.read_csv(dataset_path)

# Generate the analysis report using Sweetviz
report = sv.analyze(data)

# Save the report as a HTML file
report_path = "report.html"
report.show_html(report_path)
