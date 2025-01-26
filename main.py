class EuclideanAlgorithm:
    """Class to encapsulate the Euclidean Algorithm for finding the GCD of two numbers."""
    def gcd(a, b):
        """
        Calculate the greatest common divisor (GCD) of two integers using the Euclidean Algorithm.
        """
        # Ensure inputs are positive integers
        if a <= 0 or b <= 0:
            raise ValueError("Inputs must be positive integers.")
        # Euclidean Algorithm
        while b != 0:
            a, b = b, a % b  # Update a and b using the remainder
        return a
# Example Usage
if __name__ == "__main__":
    gcd = EuclideanAlgorithm.gcd(48, 18)
    print(f"The GCD of 48 and 18 is {gcd}")