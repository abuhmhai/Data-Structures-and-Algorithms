class Node:
    def __init__(self, key, info):
        self.key = key
        self.info = info
        self.link = None

def find_student(head, target_score):
    current = head
    
    while current is not None:
        if current.key == target_score:
            return current.info
        current = current.link
        
    return None

node1 = Node(8.5, "bit220073")
node2 = Node(9.0, "bit33212")
node3 = Node(7.5, "bit21123")
node4 = Node(9.5, "bit220049")

node1.link=node2;
node2.link=node3;
node3.link=node4;

L=node1;
target_score=9.0
result = find_student(L, target_score)

if result:
    print(f"Sinh viên có điểm {target_score} là: {result}")
else:
    print(f"Không tìm thấy sinh viên có điểm {target_score}")