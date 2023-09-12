class CircularQueue:
    def __init__(self, length: int):
        self.length = length;
        self.queue = [None] * length;
        self.head = self.tail = -1;

    def enqueue(self, data):
        if (self.isEmpty()):
            self.head = 0;
        self.tail = (self.tail + 1) % self.length;
        self.queue[self.tail] = data;

    def dequeue(self):
        if (self.head == self.tail):
            self.head = -1;
            self.tail = -1;
        self.head = (self.head + 1) % self.length;
    
    def printCQueue(self):
        if (self.head == -1):
            print("No element in the circular queue");
        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ");
            print();
        else:
            for i in range(self.head, self.length):
                print(self.queue[i], end=" ");
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ");
            print();

    def front(self):
        if (self.isEmpty()):
            return -1;
        return self.queue[self.head];

    def rear(self):
        if (self.isEmpty()):
            return -1;
        return self.queue[self.tail];

    def isEmpty(self) -> bool:
        return self.head == -1;

    def isFull(self) -> bool:
        return ((self.tail + 1) % self.length) == self.head;

queue = CircularQueue(6);
queue.enqueue('A');
queue.enqueue('B');
queue.enqueue('C');
print("Initial queue:");
queue.printCQueue();

front = queue.front();
rear = queue.rear();
print("Front: %s, Rear: %s" % (front, rear));

queue.enqueue('E');

print("\nQueue with E added:");
queue.printCQueue();

front = queue.front();
rear = queue.rear();
print("Front: %s, Rear: %s" % (front, rear));

# queue.dequeue();
# queue.dequeue();

# print("\nDequeued");
# queue.printCQueue();

# front = queue.front();
# rear = queue.rear();
# print("Front: %s, Rear: %s" % (front, rear));

# print("\nAdded some extra elements");
# queue.enqueue('A');
# queue.enqueue('B');
# queue.enqueue('D');
# queue.enqueue('F');

# queue.printCQueue();

# front = queue.front();
# rear = queue.rear();
# print("Front: %s, Rear: %s" % (front, rear));
