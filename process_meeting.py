#!/usr/bin/env python3
"""
Meeting Insights Engine
A Python script that processes meeting transcripts and extracts actionable insights.

Created as part of the AI Automation Specialist portfolio project.
Author: Your Name
Date: October 2024
"""

import nltk
import re
from datetime import datetime
from collections import defaultdict

def read_transcript(filename):
    """
    Read the meeting transcript from a text file.
    
    Args:
        filename (str): Path to the transcript file
        
    Returns:
        str: Content of the transcript file
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"✅ Successfully loaded transcript: {len(content)} characters")
            return content
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None

def extract_sentences(text):
    """
    Break the transcript into individual sentences using NLTK.
    
    Args:
        text (str): Raw meeting transcript
        
    Returns:
        list: List of sentences
    """
    sentences = nltk.sent_tokenize(text)
    print(f"📝 Found {len(sentences)} sentences in transcript")
    return sentences

def find_action_items(sentences):
    """
    Identify sentences that contain action items or commitments.
    
    Args:
        sentences (list): List of sentences from transcript
        
    Returns:
        list: List of sentences that appear to contain action items
    """
    action_patterns = [
        r'\bI will\b',
        r'\bI\'ll\b', 
        r'\bwe need to\b',
        r'\bplease\b',
        r'\bfollow up\b',
        r'\baction item\b',
        r'\bto do\b',
        r'\btask\b',
        r'\bassign\b',
        r'\bdeadline\b',
        r'\bby \w+day\b',  # by Friday, by Monday, etc.
        r'\bEOD\b',        # End of Day
        r'\bnext week\b',
        r'\btomorrow\b'
    ]
    
    action_items = []
    
    for sentence in sentences:
        for pattern in action_patterns:
            if re.search(pattern, sentence, re.IGNORECASE):
                action_items.append(sentence.strip())
                break  # Don't add the same sentence multiple times
    
    print(f"🎯 Found {len(action_items)} potential action items")
    return action_items

def find_people_mentioned(sentences):
    """
    Extract people's names mentioned in the meeting.
    Uses simple capitalized word detection.
    
    Args:
        sentences (list): List of sentences from transcript
        
    Returns:
        set: Set of unique names found
    """
    # Simple approach: find capitalized words that might be names
    # This is basic - in a real application you'd use spaCy's Named Entity Recognition
    names = set()
    
    for sentence in sentences:
        # Look for patterns like "Alice," or "Bob, please" or standalone capitalized words
        words = sentence.split()
        for i, word in enumerate(words):
            # Remove punctuation and check if it starts with capital
            clean_word = re.sub(r'[,.:;!?]', '', word)
            if (clean_word.istitle() and 
                len(clean_word) > 1 and 
                clean_word not in ['The', 'This', 'That', 'Let', 'We', 'I', 'You', 'It', 'Also', 'Yes', 'No', 
                                  'Hello', 'Today', 'Tomorrow', 'Friday', 'Monday', 'Tuesday', 'Wednesday', 
                                  'Thursday', 'Saturday', 'Sunday', 'January', 'February', 'March', 'April',
                                  'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December',
                                  'Q1', 'Q2', 'Q3', 'Q4', 'EOD']):
                names.add(clean_word)
    
    print(f"👥 Found {len(names)} people mentioned: {', '.join(sorted(names))}")
    return names

def find_dates_and_deadlines(text):
    """
    Extract dates and deadline-related information from the transcript.
    
    Args:
        text (str): Raw meeting transcript
        
    Returns:
        list: List of date-related information found
    """
    date_patterns = [
        r'\b\w+day\b',                    # Monday, Tuesday, etc.
        r'\b\w+ \d{1,2}(?:st|nd|rd|th)?\b',  # October 28th
        r'\d{1,2}/\d{1,2}/\d{4}',        # 10/28/2025
        r'\b\d{4}\b',                     # Year like 2025
        r'\bEOD\b',                       # End of Day
        r'\bnext week\b',
        r'\btomorrow\b',
        r'\btoday\b'
    ]
    
    dates_found = []
    
    for pattern in date_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        dates_found.extend(matches)
    
    # Remove duplicates while preserving order
    unique_dates = list(dict.fromkeys(dates_found))
    
    print(f"📅 Found {len(unique_dates)} date references: {', '.join(unique_dates)}")
    return unique_dates

def analyze_meeting_tone(sentences):
    """
    Perform basic sentiment analysis on the meeting.
    This is a simple version - more advanced versions would use VADER or spaCy.
    
    Args:
        sentences (list): List of sentences from transcript
        
    Returns:
        dict: Dictionary with tone analysis
    """
    positive_words = ['good', 'great', 'excellent', 'positive', 'happy', 'pleased', 'success', 'agree']
    negative_words = ['bad', 'terrible', 'negative', 'unhappy', 'problem', 'issue', 'concern', 'disagree']
    
    positive_count = 0
    negative_count = 0
    
    full_text = ' '.join(sentences).lower()
    
    for word in positive_words:
        positive_count += full_text.count(word)
    
    for word in negative_words:
        negative_count += full_text.count(word)
    
    if positive_count > negative_count:
        tone = "Positive"
    elif negative_count > positive_count:
        tone = "Negative" 
    else:
        tone = "Neutral"
    
    analysis = {
        'overall_tone': tone,
        'positive_indicators': positive_count,
        'negative_indicators': negative_count
    }
    
    print(f"😊 Meeting tone appears to be: {tone} (Positive: {positive_count}, Negative: {negative_count})")
    return analysis

def generate_summary_report(transcript_file, sentences, action_items, people, dates, tone_analysis):
    """
    Generate a comprehensive summary report of the meeting analysis.
    
    Args:
        transcript_file (str): Original transcript filename
        sentences (list): All sentences
        action_items (list): Identified action items
        people (set): People mentioned
        dates (list): Dates and deadlines found
        tone_analysis (dict): Results of tone analysis
    """
    
    print("\n" + "="*60)
    print("🔍 MEETING INSIGHTS REPORT")
    print("="*60)
    print(f"📁 Source File: {transcript_file}")
    print(f"📊 Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📝 Total Sentences: {len(sentences)}")
    print(f"😊 Overall Tone: {tone_analysis['overall_tone']}")
    
    print("\n🎯 ACTION ITEMS IDENTIFIED:")
    print("-" * 40)
    if action_items:
        for i, item in enumerate(action_items, 1):
            print(f"{i}. {item}")
    else:
        print("No clear action items identified.")
    
    print("\n👥 PEOPLE MENTIONED:")
    print("-" * 40)
    if people:
        for person in sorted(people):
            print(f"• {person}")
    else:
        print("No specific people identified.")
    
    print("\n📅 DATES & DEADLINES:")
    print("-" * 40)
    if dates:
        for date in dates:
            print(f"• {date}")
    else:
        print("No specific dates or deadlines mentioned.")
    
    print("\n🔑 KEY STATISTICS:")
    print("-" * 40)
    print(f"• Action Items: {len(action_items)}")
    print(f"• People Mentioned: {len(people)}")
    print(f"• Date References: {len(dates)}")
    print(f"• Sentiment Score: {tone_analysis['positive_indicators']} positive, {tone_analysis['negative_indicators']} negative")
    
    print("\n" + "="*60)

def main():
    """
    Main function that orchestrates the meeting analysis process.
    """
    print("🚀 Starting Meeting Insights Engine...")
    print("=" * 50)
    
    # Configuration
    transcript_filename = "sample_transcript.txt"
    
    # Step 1: Read the transcript
    transcript_text = read_transcript(transcript_filename)
    if not transcript_text:
        return
    
    # Step 2: Break into sentences
    sentences = extract_sentences(transcript_text)
    
    # Step 3: Extract insights
    action_items = find_action_items(sentences)
    people_mentioned = find_people_mentioned(sentences)
    dates_and_deadlines = find_dates_and_deadlines(transcript_text)
    tone_analysis = analyze_meeting_tone(sentences)
    
    # Step 4: Generate the final report
    generate_summary_report(
        transcript_filename, 
        sentences, 
        action_items, 
        people_mentioned, 
        dates_and_deadlines, 
        tone_analysis
    )
    
    print("✅ Meeting analysis complete!")

if __name__ == "__main__":
    main()