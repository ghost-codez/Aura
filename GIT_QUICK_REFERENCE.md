# Git Quick Reference - Future Updates

## 🚀 Standard Update Workflow (3 Steps)

### **When you make changes to any files:**

```bash
# Step 1: Add all changes
git add .

# Step 2: Commit with descriptive message
git commit -m "Your update description here"

# Step 3: Push to GitHub
git push origin main
```

## 📝 **Real Examples:**

### **Example 1: Bug Fix**
```bash
git add .
git commit -m "Fix name detection for names with apostrophes"
git push origin main
```

### **Example 2: New Feature**
```bash
git add .
git commit -m "Add Excel export functionality for meeting reports"
git push origin main
```

### **Example 3: Documentation Update**
```bash
git add .
git commit -m "Update README with new installation instructions"
git push origin main
```

## 🔍 **Helpful Commands:**

### **Check Status (See what changed):**
```bash
git status
```

### **See What Files Changed:**
```bash
git diff
```

### **View Commit History:**
```bash
git log --oneline
```

### **Push to Your Repository:**
```bash
git push origin main
```
*Note: `origin` points to https://github.com/ghost-codez/Meeting-Insights-Engine*

## 🎯 **One-Liner for Quick Updates:**
```bash
git add . && git commit -m "Quick update" && git push origin main
```

## ❗ **Important Notes:**

1. **Always be in your project folder:** `C:\Users\Mgang\Meeting-Insights-Engine`
2. **Your repository is already linked** - no need to set it up again
3. **Use descriptive commit messages** - helps track your progress
4. **Run `git status` first** if you're unsure what changed

## 🚨 **If You Get Errors:**

### **If push is rejected:**
```bash
git pull origin main
git push origin main
```

### **If you need to force push (be careful!):**
```bash
git push origin main --force
```

---
**Your repository URL:** https://github.com/ghost-codez/Meeting-Insights-Engine
**Branch:** main (default)
**Remote:** origin (already configured)