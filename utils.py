#!/usr/bin/env python3
"""
Utility Functions Module
Contains helper functions and utilities for ASCII art generation
"""

import re
import sys
import os
import platform
from typing import List, Tuple, Optional

class Utils:
    def __init__(self):
        self.system_info = self._get_system_info()

    def _get_system_info(self):
        """Get system information"""
        return {
            'platform': platform.system(),
            'python_version': sys.version,
            'encoding': sys.stdout.encoding or 'utf-8'
        }

    def clean_text(self, text: str) -> str:
        """Clean and prepare text for ASCII conversion"""
        if not text:
            return ""
        
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Remove special characters that might cause issues
        # Keep alphanumeric, spaces, and common punctuation
        text = re.sub(r'[^\w\s\.\,\!\?\-\+\=\(\)\[\]\{\}]', '', text)
        
        return text

    def validate_filename(self, filename: str) -> str:
        """Validate and clean filename for saving"""
        if not filename:
            return "ascii_art"
        
        # Remove invalid filename characters
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        
        # Remove excessive underscores and spaces
        filename = re.sub(r'[_\s]+', '_', filename)
        
        # Trim and ensure it's not empty
        filename = filename.strip('_')
        if not filename:
            filename = "ascii_art"
        
        # Limit length
        if len(filename) > 100:
            filename = filename[:100]
        
        return filename

    def get_terminal_size(self) -> Tuple[int, int]:
        """Get terminal width and height"""
        try:
            size = os.get_terminal_size()
            return size.columns, size.lines
        except:
            return 80, 24  # Default fallback

    def wrap_text(self, text: str, width: int) -> List[str]:
        """Wrap text to fit within specified width"""
        if not text:
            return []
        
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            word_length = len(word)
            
            if current_length + word_length + len(current_line) <= width:
                current_line.append(word)
                current_length += word_length
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = word_length
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines

    def format_file_size(self, size_bytes: int) -> str:
        """Format file size in human readable format"""
        if size_bytes == 0:
            return "0 B"
        
        size_names = ["B", "KB", "MB", "GB"]
        i = 0
        size = float(size_bytes)
        
        while size >= 1024.0 and i < len(size_names) - 1:
            size /= 1024.0
            i += 1
        
        return f"{size:.1f} {size_names[i]}"

    def count_characters(self, text: str) -> dict:
        """Count different types of characters in text"""
        if not text:
            return {'total': 0, 'letters': 0, 'digits': 0, 'spaces': 0, 'special': 0}
        
        counts = {
            'total': len(text),
            'letters': sum(1 for c in text if c.isalpha()),
            'digits': sum(1 for c in text if c.isdigit()),
            'spaces': sum(1 for c in text if c.isspace()),
            'special': sum(1 for c in text if not c.isalnum() and not c.isspace())
        }
        
        return counts

    def estimate_ascii_size(self, text: str, font_height: int = 5, char_width: int = 6) -> dict:
        """Estimate the size of ASCII art output"""
        char_count = len(text)
        estimated_width = char_count * char_width
        estimated_height = font_height
        
        return {
            'width': estimated_width,
            'height': estimated_height,
            'characters': char_count,
            'estimated_lines': estimated_height
        }

    def create_progress_bar(self, current: int, total: int, width: int = 50) -> str:
        """Create a simple progress bar"""
        if total <= 0:
            return "[ERROR] Invalid total"
        
        progress = min(current / total, 1.0)
        filled = int(width * progress)
        empty = width - filled
        
        bar = '█' * filled + '░' * empty
        percentage = int(progress * 100)
        
        return f"[{bar}] {percentage}% ({current}/{total})"

    def generate_separator(self, char: str = '-', width: int = 50) -> str:
        """Generate a separator line"""
        return char * width

    def center_text_in_width(self, text: str, width: int, fill_char: str = ' ') -> str:
        """Center text within a given width"""
        if len(text) >= width:
            return text
        
        padding = width - len(text)
        left_padding = padding // 2
        right_padding = padding - left_padding
        
        return fill_char * left_padding + text + fill_char * right_padding

    def validate_input(self, text: str, min_length: int = 1, max_length: int = 1000) -> Tuple[bool, str]:
        """Validate user input text"""
        if not text:
            return False, "Text cannot be empty"
        
        if len(text) < min_length:
            return False, f"Text must be at least {min_length} characters long"
        
        if len(text) > max_length:
            return False, f"Text cannot exceed {max_length} characters"
        
        # Check for only whitespace
        if not text.strip():
            return False, "Text cannot contain only whitespace"
        
        return True, "Valid input"

    def truncate_text(self, text: str, max_length: int, suffix: str = "...") -> str:
        """Truncate text to specified length with suffix"""
        if len(text) <= max_length:
            return text
        
        return text[:max_length - len(suffix)] + suffix

    def parse_color_code(self, color_input: str) -> Optional[str]:
        """Parse color input and return valid color code"""
        color_map = {
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'bright_black': '\033[90m',
            'bright_red': '\033[91m',
            'bright_green': '\033[92m',
            'bright_yellow': '\033[93m',
            'bright_blue': '\033[94m',
            'bright_magenta': '\033[95m',
            'bright_cyan': '\033[96m',
            'bright_white': '\033[97m',
            'reset': '\033[0m'
        }
        
        return color_map.get(color_input.lower())

    def colorize_text(self, text: str, color: str) -> str:
        """Add color codes to text"""
        color_code = self.parse_color_code(color)
        if color_code:
            reset_code = self.parse_color_code('reset')
            return f"{color_code}{text}{reset_code}"
        return text

    def get_random_quote(self) -> str:
        """Get a random motivational quote for ASCII art"""
        quotes = [
            "Dream Big",
            "Stay Strong",
            "Never Give Up",
            "Be Awesome",
            "Think Positive",
            "Create Magic",
            "Believe",
            "Inspire",
            "Achieve",
            "Success",
            "Victory",
            "Champion",
            "Excellence",
            "Brilliant",
            "Amazing"
        ]
        
        import random
        return random.choice(quotes)

    def benchmark_generation(self, generator_func, text: str, iterations: int = 5):
        """Benchmark ASCII generation performance"""
        import time
        
        times = []
        
        for _ in range(iterations):
            start_time = time.time()
            try:
                generator_func(text)
                end_time = time.time()
                times.append(end_time - start_time)
            except Exception:
                continue
        
        if not times:
            return None
        
        return {
            'min_time': min(times),
            'max_time': max(times),
            'avg_time': sum(times) / len(times),
            'total_time': sum(times),
            'iterations': len(times)
        }

    def detect_encoding(self, file_path: str) -> str:
        """Detect file encoding"""
        encodings = ['utf-8', 'utf-16', 'ascii', 'latin1', 'cp1252']
        
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    f.read()
                return encoding
            except (UnicodeDecodeError, UnicodeError):
                continue
        
        return 'utf-8'  # Default fallback

    def safe_print(self, text: str, encoding: Optional[str] = None):
        """Safely print text handling encoding issues"""
        if encoding is None:
            encoding = self.system_info['encoding']
        
        try:
            print(text)
        except UnicodeEncodeError:
            # Fallback to ASCII with error replacement
            safe_text = text.encode('ascii', errors='replace').decode('ascii')
            print(safe_text)

    def create_backup_name(self, base_name: str) -> str:
        """Create a backup filename with timestamp"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        name, ext = os.path.splitext(base_name)
        return f"{name}_backup_{timestamp}{ext}"

    def get_app_info(self) -> dict:
        """Get application information"""
        return {
            'name': 'Text-to-ASCII Art Generator',
            'version': '1.0.0',
            'author': 'me',
            'description': 'A comprehensive tool for converting text to ASCII art',
            'python_version': sys.version,
            'platform': platform.system(),
            'features': [
                'Multiple font support',
                'File save/load functionality',
                'Batch processing',
                'HTML export',
                'Font management',
                'Text preprocessing'
            ]
        }