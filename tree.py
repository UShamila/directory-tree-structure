class DirectoryNode:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.parent = None
    
    def __str__(self):
        return self.name

class DirectoryTree:
    def __init__(self, root_name="Root"):
        self.root = DirectoryNode(root_name)
    
    def add_directory(self, path, parent_path=None):
        """
        Add a new directory at the specified path.
        If parent_path is None, add under the current path.
        """
        if parent_path is None:
            if path not in self.root.children:
                new_dir = DirectoryNode(path)
                self.root.children[path] = new_dir
                new_dir.parent = self.root
                return True
            return False
        
        # Find the parent directory
        parent_node = self._find_directory(parent_path)
        if not parent_node:
            return False
        
        # Create the new directory if it doesn't exist
        if path not in parent_node.children:
            new_dir = DirectoryNode(path)
            parent_node.children[path] = new_dir
            new_dir.parent = parent_node
            return True
        return False
    
    def delete_directory(self, path):
        """
        Delete a directory and all its subdirectories.
        Returns True if successful, False otherwise.
        """
        directory = self._find_directory(path)
        if not directory:
            return False
        
        # Cannot delete root
        if directory == self.root:
            return False

        parent = directory.parent
        if directory.name in parent.children:
            del parent.children[directory.name]
            return True
        return False
    
    def _find_directory(self, path):
        """
        Find and return the directory node at the given path.
        Path format: "dir1/dir2/dir3"
        """
        if not path:
            return self.root
            
        parts = path.split("/")
        current = self.root
        
        for part in parts:
            if part == "":
                continue
            if part not in current.children:
                return None
            current = current.children[part]
        
        return current
    
    def print_tree(self, node=None, level=0):
        """
        Print the directory tree in a hierarchical format.
        """
        if node is None:
            node = self.root

        prefix = "|   " * (level - 1) + "|-- " if level > 0 else ""
        print(f"{prefix}{node.name}")

        for i, child in enumerate(node.children.values()):
            self.print_tree(child, level + 1)
            
    def create_sample_directory(self):
        """
        Create a sample directory structure like the one in the image.
        """
        self.add_directory("Pictures")

        self.add_directory("Saved Pictures", "Pictures")
        self.add_directory("Screenshots", "Pictures")
        self.add_directory("Camera Roll", "Pictures")

        self.add_directory("Web Images", "Pictures/Saved Pictures")
        self.add_directory("2025", "Pictures/Camera Roll")
        self.add_directory("2024", "Pictures/Camera Roll")
        self.add_directory("2023", "Pictures/Camera Roll")

        self.add_directory("Chrome", "Pictures/Saved Pictures/Web Images")
        self.add_directory("Opera", "Pictures/Saved Pictures/Web Images")
        self.add_directory("Firefox", "Pictures/Saved Pictures/Web Images")

if __name__ == "__main__":
    dir_tree = DirectoryTree()
    dir_tree.create_sample_directory()

    print("Initial Directory Structure:")
    dir_tree.print_tree()

    print("\nAdding a new directory 'Vacation' under 'Pictures':")
    dir_tree.add_directory("Vacation", "Pictures")
    dir_tree.print_tree()

    print("\nDeleting 'Saved Pictures' directory and all subdirectories:")
    dir_tree.delete_directory("Pictures/Saved Pictures")
    dir_tree.print_tree()
