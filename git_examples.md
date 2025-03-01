# Git Commands Demonstrating Persistence Concepts

This guide demonstrates how Git's version control system implements persistent data structure concepts through common Git operations.

## 1. Basic Linear History (Partial Persistence)
```bash
# Create and modify main branch (linear history)
git init
echo "Initial content" > file.txt
git add file.txt
git commit -m "Initial commit"

# Modify latest version (like partial persistence)
echo "Updated content" >> file.txt
git commit -am "Update content"
```

## 2. Branching (Full Persistence)
```bash
# Create new branch from any commit (modifying old version)
git checkout -b feature-branch
echo "Feature content" >> file.txt
git commit -am "Add feature"

# Switch between versions
git checkout main     # View main branch
git checkout feature-branch  # View feature branch
```

## 3. Merging (Confluent Persistence)
```bash
# Merge feature branch into main
git checkout main
git merge feature-branch

# Resolve any conflicts if they exist
git add .
git commit -m "Merge feature branch"
```

## 4. Fork Example (Tree-like History)
```bash
# On GitHub: Fork the repository
# Clone your fork
git clone https://github.com/your-username/repo.git
cd repo

# Create feature in fork
git checkout -b new-feature
echo "Fork-specific changes" >> file.txt
git commit -am "Add fork-specific feature"

# Push to your fork
git push origin new-feature
```

## 5. Viewing Version History
```bash
# View commit history (version tree)
git log --graph --oneline --all

# View specific version
git show <commit-hash>

# Compare versions
git diff <commit-hash1> <commit-hash2>
```

## Version Tree Visualization
```
o---o---o  main
     \
      o---o  feature-branch
           \
            o  fork-feature
```

## Persistence Concepts in Git

1. **Partial Persistence**
   - Each commit builds on previous version
   - History is immutable
   - `git commit` creates new version

2. **Full Persistence**
   - Branches can start from any commit
   - `git checkout -b` creates new branch
   - Multiple active branches

3. **Confluent Persistence**
   - `git merge` combines versions
   - Conflict resolution
   - Multiple parents possible

4. **Implementation Details**
   - Content-addressable storage
   - DAG (Directed Acyclic Graph)
   - Copy-on-write for efficiency 