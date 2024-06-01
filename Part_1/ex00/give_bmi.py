def give_bmi(height, weight):
    """
    Calculate the BMI (Body Mass Index) for a given height and weight.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[float]: List of calculated BMI values.

    Raises:
        ValueError: If height or weight contain non-numeric values, or if the number of heights
                    and weights does not match.
    """
    if not all(isinstance(h, (int, float)) for h in height) or \
            not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("Height and weight must contain only numeric values.")

    if len(height) != len(weight):
        raise ValueError("The number of heights and weights must be the same.")

    bmi_values = []
    for h, w in zip(height, weight):
        bmi = w / (h ** 2)
        bmi_values.append(bmi)

    return bmi_values


def apply_limit(bmi, limit):
    """
    Apply a limit to the BMI values.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The limit to apply.

    Returns:
        list[bool]: List of boolean values indicating if the BMI is above the limit.

    Raises:
        ValueError: If bmi contains non-numeric values.
    """
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("BMI must contain only numeric values.")

    return [bmi_val > limit for bmi_val in bmi]


def main():
    """
    Main function to demonstrate the usage of give_bmi and apply_limit functions.
    """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
