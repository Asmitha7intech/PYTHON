class CallQueue:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return self.rear == self.max_size - 1

    def is_empty(self):
        return self.front == -1

    def enqueue(self, call):
        if self.is_full():
            print("📞 Queue is full. Cannot accept new calls.")
            return
        if self.is_empty():
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = call
        print(f"✅ Call from '{call}' added to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("❌ Queue is empty. No calls to answer.")
            return
        call = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        print(f"📲 Call from '{call}' is now being attended by an agent.")

    def queue_status(self):
        if self.is_empty():
            print("📭 No calls are waiting.")
        else:
            print(f"📋 {self.rear - self.front + 1} call(s) are currently waiting.")
            print("➡️ Waiting calls:", self.queue[self.front:self.rear+1])


# ---- Main program loop ----
def main():
    max_calls = int(input("Enter the maximum number of calls the queue can hold: "))
    call_center = CallQueue(max_calls)

    while True:
        print("\n--- Call Center Menu ---")
        print("1. Add Incoming Call")
        print("2. Answer Next Call")
        print("3. Show Call Queue Status")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            caller = input("Enter caller's name or number: ")
            call_center.enqueue(caller)
        elif choice == '2':
            call_center.dequeue()
        elif choice == '3':
            call_center.queue_status()
        elif choice == '4':
            print("📞 Exiting call center system. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
