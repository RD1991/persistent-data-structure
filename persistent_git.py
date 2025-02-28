"""
Example 5: Git-like Version Control System
Demonstrates how Git uses persistent data structures for version control,
showing commit history, branching, and content tracking.
"""

from datetime import datetime
import hashlib
from typing import Dict, List, Optional

class Blob:
    """Represents a file's content, similar to Git blob object"""
    def __init__(self, content: str):
        self.content = content
        self.hash = self._calculate_hash()
    
    def _calculate_hash(self) -> str:
        return hashlib.sha1(self.content.encode()).hexdigest()[:10]

class Commit:
    """Represents a commit in version history"""
    def __init__(self, 
                 message: str, 
                 files: Dict[str, Blob], 
                 parent: Optional['Commit'] = None):
        self.message = message
        self.files = files
        self.parent = parent
        self.timestamp = datetime.now()
        self.hash = self._calculate_hash()
    
    def _calculate_hash(self) -> str:
        content = f"{self.message}{self.timestamp}{self.parent.hash if self.parent else ''}"
        return hashlib.sha1(content.encode()).hexdigest()[:10]

class Branch:
    """Represents a branch pointing to a specific commit"""
    def __init__(self, name: str, commit: Optional[Commit] = None):
        self.name = name
        self.head = commit

class PersistentGit:
    """A simplified Git-like version control system using persistent data structures"""
    
    def __init__(self):
        self.branches: Dict[str, Branch] = {"main": Branch("main")}
        self.current_branch = "main"
    
    def add_file(self, filename: str, content: str) -> Commit:
        """Creates a new commit with the added/modified file"""
        current_files = {}
        
        # Get current files from the latest commit
        if self.branches[self.current_branch].head:
            current_files = self.branches[self.current_branch].head.files.copy()
        
        # Add or update file
        current_files[filename] = Blob(content)
        
        # Create new commit
        commit = Commit(
            message=f"Update {filename}",
            files=current_files,
            parent=self.branches[self.current_branch].head
        )
        
        # Update branch head
        self.branches[self.current_branch].head = commit
        return commit
    
    def create_branch(self, branch_name: str) -> Branch:
        """Creates a new branch from current HEAD"""
        if branch_name in self.branches:
            raise ValueError(f"Branch {branch_name} already exists")
        
        current_head = self.branches[self.current_branch].head
        new_branch = Branch(branch_name, current_head)
        self.branches[branch_name] = new_branch
        return new_branch
    
    def switch_branch(self, branch_name: str):
        """Switches to specified branch"""
        if branch_name not in self.branches:
            raise ValueError(f"Branch {branch_name} does not exist")
        self.current_branch = branch_name
    
    def get_file_content(self, filename: str, commit_hash: Optional[str] = None) -> str:
        """Gets file content from specific commit or current HEAD"""
        if commit_hash:
            commit = self._find_commit(commit_hash)
        else:
            commit = self.branches[self.current_branch].head
        
        if not commit:
            raise ValueError("No commits found")
        
        if filename not in commit.files:
            raise ValueError(f"File {filename} not found in commit")
        
        return commit.files[filename].content
    
    def get_history(self) -> List[Commit]:
        """Returns commit history of current branch"""
        history = []
        current = self.branches[self.current_branch].head
        while current:
            history.append(current)
            current = current.parent
        return history
    
    def _find_commit(self, commit_hash: str) -> Optional[Commit]:
        """Finds commit by hash in current branch"""
        current = self.branches[self.current_branch].head
        while current:
            if current.hash == commit_hash:
                return current
            current = current.parent
        return None

if __name__ == "__main__":
    # Demo
    print("\n=== Git-like Version Control Demo ===")
    
    # Initialize repository
    repo = PersistentGit()
    
    # Make changes in main branch
    commit1 = repo.add_file("hello.txt", "Hello, World!")
    commit2 = repo.add_file("hello.txt", "Hello, World Updated!")
    print("\nMain branch commits:")
    for commit in repo.get_history():
        print(f"Commit {commit.hash}: {commit.message}")
    
    # Create and switch to feature branch
    repo.create_branch("feature")
    repo.switch_branch("feature")
    
    # Make changes in feature branch
    commit3 = repo.add_file("hello.txt", "Hello from feature branch!")
    commit4 = repo.add_file("new_file.txt", "New file in feature branch")
    
    print("\nFeature branch commits:")
    for commit in repo.get_history():
        print(f"Commit {commit.hash}: {commit.message}")
    
    # Demonstrate time travel
    print("\nTime travel demo:")
    print(f"Current version: {repo.get_file_content('hello.txt')}")
    print(f"Original version: {repo.get_file_content('hello.txt', commit1.hash)}")
    
    # Switch back to main branch
    repo.switch_branch("main")
    print("\nBack to main branch:")
    print(f"Current version in main: {repo.get_file_content('hello.txt')}") 