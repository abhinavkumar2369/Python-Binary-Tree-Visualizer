import tkinter as tk


# -------------------------------------------------------


# Ensure High DPI awareness on Windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# -------------------------------------------------------


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# -------------------------------------------------------


class BinaryTreeVisualizer:
    def __init__(self, root):
        self.root = root
        self.window = tk.Tk()
        self.window.title("Binary Tree Visualizer")
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg='white')
        self.canvas.pack()

    def draw_tree(self):
        self.canvas.delete("all")
        self._draw_node(self.root, 400, 50, 200)



    def _draw_node(self, node, x, y, x_offset):
        if node:
            # Node
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node.val))

            # Left child
            if node.left:
                next_x = x - x_offset
                next_y = y + 100
                self.canvas.create_line(x, y+20, next_x, next_y-20)
                self._draw_node(node.left, next_x, next_y, x_offset / 2)

            # Right child
            if node.right:
                next_x = x + x_offset
                next_y = y + 100
                self.canvas.create_line(x, y+20, next_x, next_y-20)
                self._draw_node(node.right, next_x, next_y, x_offset / 2)

    def run(self):
        self.draw_tree()
        self.window.mainloop()


# -------------------------------------------------------


if __name__ == "__main__":
    
    # Sample Binary Tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Visualizing
    visualizer = BinaryTreeVisualizer(root)
    visualizer.run()
