


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, letter):
        new_node = Node(letter)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node

    def remove_all(self):
        order = []
        while self.head is not None:
            print(f"Removed : {self.head.data}")
            order.append(self.head.data)
            self.head = self.head.next
        return order


def main():
    word = input("Enter a word/last name: ").strip().upper()
    if not word:
        print("Nothing to add.")
        return
    ll = LinkedList()
    for letter in word:
        ll.add(letter)
        print(f"Added   : {letter}")
    print()
    order = ll.remove_all()
    print("\nRemoval order:", ", ".join(order))
    print("The linked list is empty.")


if __name__ == "__main__":
    main()