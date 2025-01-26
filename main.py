class EuclideanAlgorithm:
    """Class to encapsulate the Euclidean Algorithm for finding the GCD of two numbers."""
    def gcd(a, b):
        """
        Calculate the greatest common divisor (GCD) of two integers using the Euclidean Algorithm.
        """
        # Euclidean Algorithm
        while b != 0:
            a, b = b, a % b  # Update a and b using the remainder
        return a
def main():
    """
    Main function to accept user input and compute the GCD.
    """
    #Prompt the user to enter two positive integers
    #Validate the input to ensure it's positive and numeric
    try:
        a = int(input("Enter the first positive integer: "))
        b = int(input("Enter the second positive integer: "))
        if a <= 0 or b <= 0:
            raise ValueError("Inputs must be positive integers.")
        gcd = EuclideanAlgorithm.gcd(a, b)
        print(f"The GCD of {a} and {b} is: {gcd}")
    except ValueError as e:
        print("Error:Inputs must be positive integers.")
if __name__ == "__main__":
    main()