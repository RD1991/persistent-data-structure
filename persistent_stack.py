"""
Example 2: Persistent vs Non-Persistent Stack
Demonstrates the difference between a traditional stack that modifies state in place
and a persistent stack that preserves history of all operations.
"""

# Non-Persistent (Traditional) Stack
class RegularStack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        # Modifies stack in place
        self.items.append(item)
        return self
    
    def get_items(self):
        return self.items.copy()

# Persistent Stack with History
class PersistentStack:
    def __init__(self, items=None, previous=None):
        self.items = items or []
        self.previous = previous
    
    def push(self, item):
        # Creates new version with the current state as previous
        return PersistentStack(self.items + [item], self)
    
    def get_history(self):
        # Shows all previous versions
        current = self
        versions = []
        while current:
            versions.append(current.items)
            current = current.previous
        return versions[::-1]

if __name__ == "__main__":
    print("\n=== Stack Implementation Comparison ===")
    
    # Demo with Regular Stack
    print("\nRegular Stack Demo:")
    regular_stack = RegularStack()
    stack_v1 = regular_stack.push("A")
    stack_v2 = stack_v1.push("B")
    stack_v3 = stack_v2.push("C")
    
    print("Original stack:", regular_stack.get_items())  # Will show ['A', 'B', 'C']
    print("Version 1:", stack_v1.get_items())           # Will show ['A', 'B', 'C']
    print("Version 2:", stack_v2.get_items())           # Will show ['A', 'B', 'C']
    print("Version 3:", stack_v3.get_items())           # Will show ['A', 'B', 'C']
    print("All versions reference the same stack!")
    
    # Demo with Persistent Stack
    print("\nPersistent Stack Demo:")
    persistent_stack = PersistentStack()
    p_stack_v1 = persistent_stack.push("A")
    p_stack_v2 = p_stack_v1.push("B")
    p_stack_v3 = p_stack_v2.push("C")
    
    print("History of all versions:", p_stack_v3.get_history())
    print("Each version maintains its own state and links to previous versions!") 