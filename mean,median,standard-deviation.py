import numpy as np


def array_statistics():
    """Generate a random array and compute statistics."""

    # Generate a random array of 10 elements with values between 1 and 100
    random_array = np.random.randint(1, 101, size=10)

    # Calculate mean, median, and standard deviation
    mean_value = np.mean(random_array)
    median_value = np.median(random_array)
    std_deviation = np.std(random_array)

    # Sort the array
    sorted_array = np.sort(random_array)

    # Print the results
    print("Random Array:")
    print(random_array)

    print(f"\nMean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {std_deviation}")

    print("\nSorted Array:")
    print(sorted_array)


# Run the array statistics calculation
array_statistics()

