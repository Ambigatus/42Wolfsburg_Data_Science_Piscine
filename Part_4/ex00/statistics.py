import numpy as np


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Calculate and display various statistical metrics based on the given arguments.

    Parameters:
    *args: any
        A variable number of arguments representing the dataset to calculate statistics on.
    **kwargs: any
        Keyword arguments specifying which statistical metrics to calculate.
        Supported metrics:
        - "mean": Calculate the mean of the dataset.
        - "median": Calculate the median of the dataset.
        - "quartile": Calculate the 25th and 75th quartiles of the dataset.
        - "std": Calculate the standard deviation of the dataset.
        - "var": Calculate the variance of the dataset.

    Returns:
    None
    """
    try:
        data = np.array(args, dtype=float)

        if len(args) == 0:
            print("ERROR")
            return

        for key, value in kwargs.items():
            if value == "mean":
                print(f"mean : {np.mean(data)}")
            elif value == "median":
                print(f"median : {int(np.median(data))}")
            elif value == "quartile":
                quartiles = np.percentile(data, [25, 75]).tolist()
                print(f"quartile : {quartiles}")
            elif value == "std":
                print(f"std : {np.std(data, ddof=0)}")
            elif value == "var":
                print(f"var : {np.var(data, ddof=0)}")
            else:
                print("ERROR")

    except Exception:
        print("ERROR")


def main():
    """
    Main function to execute test cases for the ft_statistics function.
    The function is not executed if the script is run directly.
    """
    pass


if __name__ == "__main__":
    main()
