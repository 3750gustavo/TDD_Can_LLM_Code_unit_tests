def calculate_relative_position(min_value, max_value, value):
    """
    Calculate the relative position of a value within a given range.

    Parameters:
    min_value (float): The minimum value of the range.
    max_value (float): The maximum value of the range.
    value (float): The value to check.

    Returns:
    float: The relative position of the value within the range, from 1.00 (at min_value) to 0.00 (at max_value).
    """
    if min_value > max_value:
        raise ValueError("min_value should be less than or equal to max_value")
    if not min_value <= value <= max_value:
        raise ValueError("value should be within the range [min_value, max_value]")

    return 1 - ((value - min_value) / (max_value - min_value))

def main():
    precision_score = 0.5 * 0.4
    print("Precision score: {:.4f}".format(precision_score))
    readbility_score = 0.708 * 0.1
    print("Readability score: {:.4f}".format(readbility_score))
    min_value = 0.676
    max_value = 1.43
    value = 1.43
    weight = 0.35
    normalized_value = calculate_relative_position(min_value, max_value, value)
    adjusted_value_with_weights = normalized_value * weight
    print("Normalized value: {:.3f}".format(normalized_value))
    print("Adjusted value with weights: {:.3f}".format(adjusted_value_with_weights))
    complexity_score = 1.00 * 0.15
    print("Complexity score: {:.4f}".format(complexity_score))
    final_score = precision_score + readbility_score + complexity_score + adjusted_value_with_weights
    print("Final score: {:.3f}".format(final_score))

if __name__ == "__main__":
    main()

# mathematical term is Normalization
# Normalization is the process of scaling and centering values.
# This can be done by subtracting the minimum value from each value and dividing by the range.