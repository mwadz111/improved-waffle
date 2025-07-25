"""
main.py - Entry point for the Improved Waffles project.
This script simulates processing waffle data using modular code.
"""

from utils.helper import make_waffle_batch

def main():
    # Sample waffle order
    order = {
        "flavor": "chocolate",
        "toppings": ["strawberries", "whipped cream"],
        "quantity": 3
    }

    print("Preparing your waffle order...")
    result = make_waffle_batch(order)

    print("\n--- Order Summary ---")
    print(f"Waffle Flavor: {result['flavor']}")
    print(f"Toppings: {', '.join(result['toppings'])}")
    print(f"Quantity: {result['quantity']}")
    print("Status:", result["status"])

if __name__ == "__main__":
    main()
