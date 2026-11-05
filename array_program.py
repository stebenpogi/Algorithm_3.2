


def add_all(word):
    arr = [None] * len(word)      # array sized dynamically from the input
    size = 0
    for letter in word:
        arr[size] = letter
        size = size + 1
        print(f"Added   : {letter}  (size = {size})")
    return arr, size


def remove_all(arr, size):
    order = []
    while size > 0:
        size = size - 1
        print(f"Removed : {arr[size]}  (size = {size})")
        order.append(arr[size])
        arr[size] = None          # clear the slot
    return order


def main():
    word = input("Enter a word or last name: ").strip().upper()
    if not word:
        print("Nothing to add.")
        return
    arr, size = add_all(word)
    print("\nArray contents:", arr[:size], "\n")
    order = remove_all(arr, size)
    print("\nRemoval order:", ", ".join(order))
    print("The array is empty.")


if __name__ == "__main__":
    main()