# Meeting Insights Engine - Setup for Minimal Interference

## 🚀 Quick Setup Guide

### **Method 1: Double-Click Execution (Simplest)**
1. **Just double-click `run_analysis.bat`** in Windows Explorer
2. It will automatically find and process any transcript files
3. Press any key when done

### **Method 2: Desktop Shortcut (Fastest)**
1. Right-click on `run_analysis.bat`
2. Select "Send to" → "Desktop (create shortcut)"
3. Now you can run analysis from your desktop with one double-click!

### **Method 3: PowerShell (Most Advanced)**
```powershell
# Basic usage
.\run_analysis.ps1

# Silent mode (no prompts)
.\run_analysis.ps1 -Silent

# Process specific file
.\run_analysis.ps1 -TranscriptPath "C:\path\to\your\transcript.txt"

# Process file and auto-open results
.\run_analysis.ps1 -TranscriptPath "C:\path\to\your\transcript.txt" -OpenOutput
```

## 📁 **File Organization for Zero Friction**

### **Recommended Folder Structure:**
```
Meeting-Insights-Engine/
├── process_meeting.py          # Main script
├── run_analysis.bat           # One-click runner
├── run_analysis.ps1           # Advanced PowerShell runner
├── sample_transcript.txt      # Example file
└── [your-transcript-files]    # Drop your files here!
```

### **How to Use:**
1. **Drop any `.txt` file** into the `Meeting-Insights-Engine` folder
2. **Double-click `run_analysis.bat`**
3. **Done!** - It automatically finds and processes your file

## 🔄 **For Regular Use (Limitless AI Integration)**

### **Workflow Setup:**
1. **Export your Limitless AI transcript** as a `.txt` file
2. **Save it to your Meeting-Insights-Engine folder** 
   - Name it something like: `meeting_2025-10-05.txt`
   - Or just: `transcript.txt`
3. **Double-click your desktop shortcut**
4. **Review the insights** in the terminal output

### **Advanced Automation Options:**

#### **Option A: Folder Monitoring (Future Enhancement)**
- Set up a folder watcher that automatically processes new files
- Great for integration with Limitless AI auto-export

#### **Option B: Scheduled Processing**
- Use Windows Task Scheduler to run analysis at set times
- Perfect for batch processing daily transcripts

#### **Option C: Integration with Limitless AI**
- Create a script that automatically downloads from Limitless
- Process immediately after meetings end

## 🛠️ **Troubleshooting**

### **If the batch file doesn't work:**
1. Make sure Python is installed and in your PATH
2. Try running in PowerShell: `python process_meeting.py`
3. Check that NLTK packages are downloaded

### **If no files are found:**
1. Make sure your transcript files are `.txt` format
2. Place them in the same folder as `process_meeting.py`
3. The script automatically detects files with "transcript" in the name first

### **For PowerShell execution errors:**
1. Open PowerShell as Administrator
2. Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
3. Try running the script again

## 🎯 **Next Level Automation Ideas**

### **For Your Work Environment:**
1. **Power Automate Flow:**
   - Trigger: New file in OneDrive/SharePoint
   - Action: Run analysis logic using AI Builder
   - Output: Create tasks in Microsoft Planner

2. **Email Integration:**
   - Forward meeting transcripts to a specific email
   - Auto-process and send summary back

3. **Teams Integration:**
   - Post analysis results directly to Teams channels
   - @mention people found in the transcript

### **Personal Productivity:**
1. **Batch Processing:** Analyze multiple files at once
2. **Export to Excel:** Structured data for tracking trends
3. **Calendar Integration:** Auto-create follow-up meetings
4. **Task Manager Integration:** Send action items to your preferred app

---

**🎉 You're all set for minimal-interference meeting analysis!**

Just remember: **Drop transcript → Double-click shortcut → Get insights!**