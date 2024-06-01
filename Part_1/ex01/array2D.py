import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Truncate a 2D array based on the provided start and end indices.

    Args:
        family (list): 2D array.
        start (int): Starting index for truncation.
        end (int): Ending index for truncation.

    Returns:
        list: Truncated version of the array.

    Raises:
        ValueError: If family is not a list or if start and end are not integers.
        IndexError: If start or end is out of range.
    """
    # Validate inputs
    if not isinstance(family, list):
        raise ValueError("family must be a list.")

    if not all(isinstance(row, list) for row in family):
        raise ValueError("All elements of family must be lists.")

    if not all(all(isinstance(x, (int, float)) for x in row) for row in family):
        raise ValueError("All elements of the 2D array must be integers or floats.")

    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("start and end must be integers.")

    num_rows = len(family)
    num_cols = len(family[0]) if num_rows > 0 else 0

    if not all(len(row) == num_cols for row in family):
        raise ValueError("All rows in the 2D array must have the same number of columns.")

    # Print the original shape
    print("My shape is:", (num_rows, num_cols))

    # Adjust negative indices
    # if start < 0:
    #     start += num_cols
    if end < 0:
        end = num_rows + end

    # Ensure indices are within the valid range
    if not (0 <= start <= num_cols) or not (0 <= end <= num_cols):
        raise IndexError("start and end indices are out of range.")

    # Ensure start is less than end
    if start >= end:
        raise IndexError("start index cannot be greater than or equal to end index.")

    # Convert to numpy array for slicing
    family_np = np.array(family)

    # Perform slicing
    sliced_family = family_np[start:end]

    # Print the new shape
    print("My new shape is:", sliced_family.shape)

    return sliced_family.tolist()


def main():
    """
    Main function to demonstrate the usage of slice_me function.
    """
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -1))


if __name__ == "__main__":
    main()
