"""Example of writing a function to process a list."""


def main() -> None:
    """Entrypoint of program."""
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kevin", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in the haystack, False otherwise."""
    # Move through each item in list until needle is found
    i: int = 0
    while i < len(haystack):
        item: str = haystack[1]
        if item == needle:
            return True
        i += 1
    
    return False

if __name__ == "__main__":
    main()