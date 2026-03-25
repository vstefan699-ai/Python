def icecream(amount, *flavors):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {amount} scoop icecream with the following flavors:")
    for flavor in flavors:
        print(f"- {flavor}")