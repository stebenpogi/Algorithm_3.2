


def enqueue_all(word):
    queue = [None] * len(word)
    front, rear = 0, -1
    for letter in word:
        rear = rear + 1
        queue[rear] = letter
        print(f"Enqueued: {letter}  (rear = {rear})")
    return queue, front, rear


def dequeue_all(queue, front, rear):
    order = []
    while front <= rear:
        print(f"Dequeued: {queue[front]}  (front = {front + 1})")
        order.append(queue[front])
        front = front + 1
    return order


def main():
    word = input("Enter a word/last name: ").strip().upper()
    if not word:
        print("Nothing to enqueue.")
        return
    queue, front, rear = enqueue_all(word)
    print()
    order = dequeue_all(queue, front, rear)
    print("\nRemoval order:", ", ".join(order))
    print("The queue is empty.")


if __name__ == "__main__":
    main()