"""
Example 4: Persistent vs Non-Persistent Dictionary
Demonstrates the difference between a traditional dictionary that modifies state in place
and a persistent dictionary that maintains version history.
"""

# Non-Persistent (Traditional) Dictionary
class RegularDict:
    def __init__(self):
        self.data = {}
    
    def set(self, key, value):
        # Modifies dictionary in place
        self.data[key] = value
        return self
    
    def get_data(self):
        return self.data.copy()

# Persistent Dictionary with Time Travel
class PersistentDict:
    def __init__(self, data=None, timestamp=0, previous=None):
        self.data = data or {}
        self.timestamp = timestamp
        self.previous = previous
    
    def set(self, key, value):
        # Creates new version with current state as previous
        new_data = self.data.copy()
        new_data[key] = value
        return PersistentDict(new_data, self.timestamp + 1, self)
    
    def get_version(self, timestamp):
        current = self
        while current and current.timestamp > timestamp:
            current = current.previous
        return current.data if current else {}

if __name__ == "__main__":
    print("\n=== Dictionary Implementation Comparison ===")
    
    # Demo with Regular Dictionary
    print("\nRegular Dictionary Demo:")
    regular_dict = RegularDict()
    dict_v1 = regular_dict.set("name", "Alice")
    dict_v2 = dict_v1.set("age", 25)
    dict_v3 = dict_v2.set("name", "Bob")
    
    print("Original dict:", regular_dict.get_data())  # Will show final state
    print("Version 1:", dict_v1.get_data())          # Will show final state
    print("Version 2:", dict_v2.get_data())          # Will show final state
    print("Version 3:", dict_v3.get_data())          # Will show final state
    print("All versions reference the same dictionary!")
    
    # Demo with Persistent Dictionary
    print("\nPersistent Dictionary Demo:")
    persistent_dict = PersistentDict()
    p_dict_v1 = persistent_dict.set("name", "Alice")
    p_dict_v2 = p_dict_v1.set("age", 25)
    p_dict_v3 = p_dict_v2.set("name", "Bob")
    
    print("Original state:", persistent_dict.data)
    print("Version 1:", p_dict_v3.get_version(1))  # Shows state after first operation
    print("Version 2:", p_dict_v3.get_version(2))  # Shows state after second operation
    print("Current state:", p_dict_v3.data)        # Shows current state
    print("Each version maintains its own state and can be accessed at any time!") 