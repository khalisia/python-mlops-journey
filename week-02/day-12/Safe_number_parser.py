def safe_number_parser():
    """
    A safe number parser that handles various input types and errors gracefully.
    """
    
    def parse_to_int(value):
        """Safely convert a value to integer."""
        try:
            return int(value)
        except ValueError:
            return None
        except TypeError:
            return None
    
    def parse_to_float(value):
        """Safely convert a value to float."""
        try:
            return float(value)
        except ValueError:
            return None
        except TypeError:
            return None
    
    def parse_with_fallback(value, default=0):
        """Parse with a default fallback value."""
        try:
            # Try integer first
            return int(value)
        except (ValueError, TypeError):
            try:
                # Try float if int fails
                return float(value)
            except (ValueError, TypeError):
                # Return default if all parsing fails
                return default
    
    def parse_and_validate(value, min_val=None, max_val=None):
        """Parse and validate against bounds."""
        try:
            result = float(value)
            
            # Check minimum bound
            if min_val is not None and result < min_val:
                return None, f"Value {result} is below minimum {min_val}"
            
            # Check maximum bound
            if max_val is not None and result > max_val:
                return None, f"Value {result} is above maximum {max_val}"
            
            # Return integer if it's a whole number
            if result.is_integer():
                return int(result), None
            return result, None
            
        except (ValueError, TypeError) as e:
            return None, f"Invalid number format: {str(e)}"
    
    def parse_list(numbers):
        """Parse a list of numbers safely."""
        results = []
        errors = []
        
        for i, num in enumerate(numbers):
            try:
                results.append(float(num))
            except (ValueError, TypeError) as e:
                errors.append(f"Index {i}: '{num}' - {str(e)}")
                results.append(None)
        
        return results, errors
    
    # Return all functions
    return {
        'to_int': parse_to_int,
        'to_float': parse_to_float,
        'with_fallback': parse_with_fallback,
        'validate': parse_and_validate,
        'parse_list': parse_list
    }


# Example usage and demonstration
def demo_safe_parser():
    """Demonstrate the safe number parser with examples."""
    
    parser = safe_number_parser()
    
    print("=" * 50)
    print("SAFE NUMBER PARSER DEMONSTRATION")
    print("=" * 50)
    
    # Test data
    test_values = [
        "123",
        "45.67",
        "hello",
        "12.0",
        "abc123",
        "",
        None,
        "  42  ",
        "-99.99",
        "1e10"
    ]
    
    print("\n1. Parsing to Integer (returns None on failure):")
    print("-" * 40)
    for value in test_values:
        result = parser['to_int'](value)
        print(f"  '{value}' -> {result}")
    
    print("\n2. Parsing to Float (returns None on failure):")
    print("-" * 40)
    for value in test_values:
        result = parser['to_float'](value)
        print(f"  '{value}' -> {result}")
    
    print("\n3. Parsing with Fallback (default=0):")
    print("-" * 40)
    for value in test_values:
        result = parser['with_fallback'](value)
        print(f"  '{value}' -> {result}")
    
    print("\n4. Parsing with Validation:")
    print("-" * 40)
    test_cases = [
        ("100", 0, 200),
        ("250", 0, 200),
        ("-50", 0, 200),
        ("abc", 0, 200),
        ("50.5", 0, 100)
    ]
    
    for value, min_val, max_val in test_cases:
        result, error = parser['validate'](value, min_val, max_val)
        if error:
            print(f"  '{value}' -> ERROR: {error}")
        else:
            print(f"  '{value}' -> {result} (valid)")
    
    print("\n5. Parsing Lists:")
    print("-" * 40)
    test_lists = [
        ["10", "20", "30", "forty"],
        ["1.5", "2.7", "invalid", "3.9", None],
        ["", "   ", "100"]
    ]
    
    for i, num_list in enumerate(test_lists, 1):
        results, errors = parser['parse_list'](num_list)
        print(f"\n  List {i}: {num_list}")
        print(f"  Results: {results}")
        if errors:
            print(f"  Errors: {errors}")
    
    print("\n6. Interactive Example:")
    print("-" * 40)
    
    # Interactive loop (commented for demo, uncomment to use)
    """
    while True:
        user_input = input("\nEnter a number (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        
        result = parser['with_fallback'](user_input)
        print(f"Parsed value: {result}")
        
        # Try integer conversion if it's a whole number
        if isinstance(result, float) and result.is_integer():
            print(f"  As integer: {int(result)}")
    """


def advanced_examples():
    """Additional real-world examples."""
    
    parser = safe_number_parser()
    
    print("\n" + "=" * 50)
    print("ADVANCED REAL-WORLD EXAMPLES")
    print("=" * 50)
    
    # Example 1: Reading from a CSV-like string
    print("\n1. Parsing CSV data:")
    data_string = "Alice,25,Bob,thirty,Charlie,30.5"
    parts = data_string.split(',')
    
    for i in range(0, len(parts), 2):
        name = parts[i]
        age_str = parts[i+1] if i+1 < len(parts) else "?"
        age = parser['to_float'](age_str)
        
        if age is not None:
            print(f"  {name} is {age} years old")
        else:
            print(f"  {name} has invalid age: '{age_str}'")
    
    # Example 2: Configuration file parsing
    print("\n2. Configuration parsing:")
    config = {
        'volume': '85',
        'brightness': 'auto',
        'contrast': '0.75',
        'refresh_rate': 'invalid'
    }
    
    for setting, value in config.items():
        parsed = parser['with_fallback'](value)
        print(f"  {setting}: '{value}' -> {parsed}")
    
    # Example 3: Validating user age input
    print("\n3. Age validation:")
    age_inputs = ['25', '150', 'negative', '25.5', '0']
    
    for age_input in age_inputs:
        age, error = parser['validate'](age_input, 0, 120)
        if error:
            print(f"  Age '{age_input}' is invalid: {error}")
        else:
            print(f"  Age '{age_input}' is valid: {age}")


if __name__ == "__main__":
    # Run the demonstration
    demo_safe_parser()
    
    # Run advanced examples
    advanced_examples()
    
    # Learning summary
    print("\n" + "=" * 50)
    print("LEARNING SUMMARY")
    print("=" * 50)
    print("""
    ✅ try/except blocks catch errors before they crash your program
    ✅ ValueError specifically handles type conversion failures
    ✅ Different exceptions can be caught separately or together
    ✅ Multiple except blocks allow different error handling strategies
    ✅ Returning None or default values keeps your program running
    ✅ Validation adds another layer of safety beyond conversion
    
    Key Takeaways:
    • Always handle potential errors in user input processing
    • Provide meaningful feedback when parsing fails
    • Use specific exception types (ValueError) instead of bare except
    • Consider returning structured data (value + error message) for debugging
    """)