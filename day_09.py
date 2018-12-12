class Node:
    def __init__(self, val):
        self.val = val
        self.left = self
        self.right = self


class MarbleGameLinkedList:
    def __init__(self):
        self.cur = Node(0)

    def _insert(self, node):
        l = self.cur.right
        r = self.cur.right.right
        l.right, r.left = node, node
        node.left, node.right = l, r

        self.cur = node

    def _insert_23(self):
        for _ in range(6):
            self.cur = self.cur.left
        # remove the one on the left (7th)
        score_from_popped = self.cur.left.val
        l = self.cur.left.left
        self.cur.left = l
        l.right = self.cur
        return score_from_popped

    def play(self, p, n):
        scores = [0] * p
        for i in range(1, n + 1):
            if i % 23 == 0:
                scores[i % p] += i + self._insert_23()
            else:
                self._insert(Node(i))
        return max(scores)


if __name__ == "__main__":
    p = 470
    n = 72170
    print(f"Part 1 answer: {MarbleGameLinkedList().play(p, n)}")
    print(f"Part 2 answer: {MarbleGameLinkedList().play(p, 100 * n)}")
