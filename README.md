# Persistent vs Non-Persistent Data Structures Examples

This repository contains practical examples comparing persistent and non-persistent data structures implemented in Python. The examples demonstrate how persistent data structures maintain their previous versions after modifications, while traditional data structures modify state in place.

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd persistent-data-structures
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## What are Persistent Data Structures?

Persistent data structures are data structures that preserve their previous versions when modified. Instead of updating the data structure in place (like traditional data structures), each operation creates a new version while leaving the old version intact.

### Key Differences from Traditional Data Structures

**Traditional Data Structures:**
- ✏️ **Modifications:** Updates data in place
- 🗑️ **History:** Previous states are lost after modifications
- 💾 **Memory:** Generally lower memory usage
- 🔍 **Access:** Only current state is available
- 📦 **Best For:** Simple data storage and manipulation

**Persistent Data Structures:**
- 🔄 **Modifications:** Creates new versions for each change
- 📚 **History:** Preserves all previous versions
- 🧠 **Memory:** Higher but optimized through structural sharing
- ⏳ **Access:** Time-travel to any previous state
- 🛠️ **Best For:** Version control, undo/redo operations

## Examples Overview

### 1. List Implementation (`persistent_list.py`)
Compares `RegularList` vs `PersistentList`:
- **Regular List**: Modifies the list in place with `append`
- **Persistent List**: Creates a new list for each `append`
- Shows how persistent lists maintain separate states for each version
- Use case: When you need to track all changes made to a list

### 2. Stack Implementation (`persistent_stack.py`)
Compares `RegularStack` vs `PersistentStack`:
- **Regular Stack**: Traditional push operations modify the stack directly
- **Persistent Stack**: Each push creates a new stack with history
- Demonstrates complete history tracking capability
- Use case: Implementing undo/redo functionality

### 3. Binary Tree Implementation (`persistent_tree.py`)
Compares `RegularTree` vs `PersistentTree`:
- **Regular Tree**: Modifies nodes in place during insertion
- **Persistent Tree**: Creates new nodes only along the insertion path
- Shows structural sharing concept in hierarchical structures
- Use case: Version control systems, maintaining different versions of hierarchical data

### 4. Dictionary Implementation (`persistent_dict.py`)
Compares `RegularDict` vs `PersistentDict`:
- **Regular Dict**: Key-value pairs are updated in place
- **Persistent Dict**: Maintains version history with timestamps
- Demonstrates time-travel functionality
- Use case: Debug-friendly data stores, state management in applications

### 5. Git-like Version Control (`persistent_git.py`)
Implements a simplified version of Git's data model:
- **Blob**: Represents file content with hash
- **Commit**: Persistent snapshot of repository state
- **Branch**: Reference to specific commits
- Features:
  - Commit history tracking
  - Branching and switching
  - Time travel to previous versions
  - Content-addressable storage
- Use case: Understanding Git's internal data structure

## Key Concepts

1. **Immutability**
   - Traditional: Mutable state that changes in place
   - Persistent: Immutable state where changes create new versions
   - Benefit: Predictable behavior and easier debugging

2. **History Preservation**
   - Traditional: Only current state is available
   - Persistent: Complete history of changes
   - Benefit: Time travel debugging and undo/redo operations

3. **Memory Efficiency**
   - Traditional: Lower memory overhead
   - Persistent: Uses structural sharing to minimize memory impact
   - Trade-off: Memory vs version history

4. **Common Use Cases**
   - Version Control Systems (Git)
   - Undo/Redo Operations
   - Time-travel Debugging
   - Concurrent Programming
   - Functional Programming
   - State Management (Redux)

## Running the Examples

Each example can be run independently and shows a side-by-side comparison:
```bash
python persistent_list.py    # Compare regular vs persistent list
python persistent_stack.py   # Compare regular vs persistent stack
python persistent_tree.py    # Compare regular vs persistent tree
python persistent_dict.py    # Compare regular vs persistent dictionary
```

## Learning Path for Beginners

1. Start with `persistent_list.py` 
   - Simplest example showing basic persistence
   - Clear comparison with traditional list

2. Move to `persistent_stack.py`
   - Introduces history tracking
   - Shows linked version history

3. Explore `persistent_dict.py`
   - Demonstrates practical time-travel features
   - Shows timestamp-based versioning

4. Finally, study `