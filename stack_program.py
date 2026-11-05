


def push_all(word):
    stack = [None] * len(word)
    top = -1
    for letter in word:
        top = top + 1
        stack[top] = letter
        print(f"Pushed  : {letter}  (top = {top})")
    return stack, top


def pop_all(stack, top):
    order = []
    while top >= 0:
        print(f"Popped  : {stack[top]}  (top = {top - 1})")
        order.append(stack[top])
        top = top - 1
    return order


def main():
    word = input("Enter a word/last name: ").strip().upper()
    if not word:
        print("Nothing to push.")
        return
    stack, top = push_all(word)
    print()
    order = pop_all(stack, top)
    print("\nRemoval order:", ", ".join(order))
    print("The stack is empty.")


if __name__ == "__main__":
    main()