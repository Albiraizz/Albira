#Aldo Bintang Rhamadhan


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove_at_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        last = self.head
        while last.next.next:
            last = last.next
        last.next = None

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Contoh penggunaan
linked_list = LinkedList()
linked_list.add_at_beginning(1)
linked_list.add_at_end(2)
linked_list.add_at_end(3)

data_to_search = int(input("Masukkan data yang akan dicari: "))
if linked_list.search(data_to_search):
    print("Data ditemukan.")
else:
    print("Data tidak ditemukan.")

print("Jumlah data dalam linked list: ", linked_list.size())