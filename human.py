import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

# Load HR data into a pandas DataFrame
hr_data = pd.read_csv('C:/Users/balah/HRDataset_v14.csv')

# Analyze employee turnover
turnover_rate = (hr_data['Turnover'].sum() / len(hr_data)) * 100
print(f"Turnover Rate: {turnover_rate:.2f}%")

# Visualize employee turnover rates using a heatmap
turnover_by_department = pd.pivot_table(hr_data, values='Turnover', index='Department', aggfunc='mean')
plt.figure(figsize=(10, 6))
sns.heatmap(turnover_by_department, cmap='RdYlBu', annot=True, fmt=".2f")
plt.title('Employee Turnover by Department')
plt.xlabel('Department')
plt.ylabel('Turnover Rate')
plt.tight_layout()
plt.show()

# Visualize employee turnover rates using a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Department', y='PerformanceRating', data=hr_data)
plt.xlabel('Department')
plt.ylabel('PerformanceRating')
plt.title('Employee Turnover by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualize employee turnover rates using a pie chart
plt.figure(figsize=(8, 8))
turnover_counts = hr_data['Turnover'].value_counts()
plt.pie(turnover_counts, labels=turnover_counts.index, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
plt.title('Employee Turnover')
plt.axis('equal')
plt.tight_layout()
plt.show()


# Create an organizational chart to visualize reporting structures and departmental hierarchies
G = nx.DiGraph()
G.add_nodes_from(hr_data['EmpID'])
for _, row in hr_data.iterrows():
    if pd.notnull(row['ManagerID']):
        G.add_edge(row['ManagerID'], row['EmpID'])

# Visualize organizational chart using networkx
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, node_size=1500, node_color='lightblue', font_size=10, arrows=False)
plt.title('Organizational Chart')
plt.tight_layout()
plt.show()

turnover_rates = hr_data.groupby('Department')['Turnover'].mean().sort_values(ascending=False)

# Visualize employee turnover rates using a funnel chart
plt.figure(figsize=(8, 6))
stages = turnover_rates.index
conversion_rates = turnover_rates.values * 100
plt.plot(stages, conversion_rates, marker='o', linestyle='-')
plt.title('Funnel Chart of Employee Turnover Rates by Department')
plt.xlabel('Department')
plt.ylabel('Turnover Rate (%)')
plt.grid(True)
plt.gca().invert_yaxis()  # Invert y-axis to represent funnel shape
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualize employee turnover rates using a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Department', y='Turnover', data=hr_data, palette='Set2')
plt.title('Violin Plot of Employee Turnover Rates by Department')
plt.xlabel('Department')
plt.ylabel('Turnover Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Violin plot to visualize the distribution of performance ratings
plt.figure(figsize=(10, 6))
sns.violinplot(x='PerformanceRating', data=hr_data, palette='muted')
plt.title('Distribution of Performance Ratings')
plt.xlabel('Performance Rating')
plt.ylabel('Density')
plt.show()

# Count plot to visualize the distribution of training hours
plt.figure(figsize=(10, 8))
sns.countplot(x='TrainingHours', data=hr_data, palette='pastel')
plt.title('Distribution of Training Hours')
plt.xlabel('Training Hours')
plt.ylabel('Count')
plt.show()
