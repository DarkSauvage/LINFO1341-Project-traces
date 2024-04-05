import matplotlib.pyplot as plt

def create_pie_chart():
    # Define the data for the pie chart
    labels = ['IPv4', 'IPv6']
    sizes = [86, 16]  # The percentages for each label

    # Create the pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Add a title
    plt.title('Répartition des protocoles IP')

    # Display the chart
    plt.show()
    # Save the figure to a file
    plt.savefig('camembert.png')

if __name__ == "__main__":
    create_pie_chart()