"""
Example 1: Persistent vs Non-Persistent List
This example demonstrates the difference between a regular list and a persistent list.
The key difference is that modifications to a regular list change it in place,
while modifications to a persistent list create new versions.
"""

# Non-Persistent (Traditional) List Example
class RegularList:
    def __init__(self, items=None):
        self._items = items or []
    
    def append(self, item):
        # Modifies the list in place
        self._items.append(item)
        return self
    
    def get_items(self):
        return self._items.copy()

# Persistent List Example
class PersistentList:
    def __init__(self, items=None):
        self._items = items or []
    
    def append(self, item):
        # Creates a new list instead of modifying the existing one
        return PersistentList(self._items + [item])
    
    def get_items(self):
        return self._items.copy()

if __name__ == "__main__":
    print("\n=== List Implementation Comparison ===")
    
    # Demo with Regular List
    print("\nRegular List Demo:")
    regular_list = RegularList()
    list_v1 = regular_list.append(1)
    list_v2 = list_v1.append(2)
    
    print("Original list:", regular_list.get_items())  # Will show [1, 2]
    print("Version 1:", list_v1.get_items())          # Will show [1, 2]
    print("Version 2:", list_v2.get_items())          # Will show [1, 2]
    print("All versions point to the same list!")
    
    # Demo with Persistent List
    print("\nPersistent List Demo:")
    persistent_list = PersistentList()
    persistent_v1 = persistent_list.append(1)
    persistent_v2 = persistent_v1.append(2)
    
    print("Original list:", persistent_list.get_items())  # Will show []
    print("Version 1:", persistent_v1.get_items())       # Will show [1]
    print("Version 2:", persistent_v2.get_items())       # Will show [1, 2]
    print("Each version maintains its own state!") 