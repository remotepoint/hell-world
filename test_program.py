def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def test_calculate_area():
    """Test function for calculate_area."""
    # Test case 1: Regular positive numbers
    assert calculate_area(4, 5) == 20, "Test case 1 failed"
    # Test case 2: Zero as input
    assert calculate_area(0, 5) == 0, "Test case 2 failed"
    print("All tests passed!")

def main():
    print("Welcome to the Rectangle Area Calculator!")
    
    # Get input from user
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Calculate and display the area
    area = calculate_area(length, width)
    print(f"\nThe area of the rectangle is: {area}")

if __name__ == "__main__":
    # Run tests first
    test_calculate_area()
    # Then run the main program
    main() 