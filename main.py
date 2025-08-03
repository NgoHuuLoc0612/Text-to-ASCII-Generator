#!/usr/bin/env python3
"""
Text-to-ASCII Art Generator
Main application file that handles user interface and program flow
"""

from ascii_generator import ASCIIGenerator
from font_manager import FontManager
from file_handler import FileHandler
from utils import Utils
import sys

class TextToASCIIApp:
    def __init__(self):
        self.generator = ASCIIGenerator()
        self.font_manager = FontManager()
        self.file_handler = FileHandler()
        self.utils = Utils()

    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "="*50)
        print("    TEXT-TO-ASCII ART GENERATOR")
        print("="*50)
        print("1. Generate ASCII Art")
        print("2. List Available Fonts")
        print("3. Save ASCII Art to File")
        print("4. Load Text from File")
        print("5. Change Font")
        print("6. Preview All Fonts")
        print("7. Exit")
        print("="*50)

    def get_user_input(self):
        """Get text input from user"""
        text = input("\nEnter text to convert: ").strip()
        if not text:
            print("Please enter some text!")
            return None
        return text

    def generate_art(self):
        """Generate ASCII art from user input"""
        text = self.get_user_input()
        if text:
            try:
                ascii_art = self.generator.text_to_ascii(text)
                print("\n" + "="*60)
                print("ASCII ART RESULT:")
                print("="*60)
                print(ascii_art)
                print("="*60)
                return ascii_art
            except Exception as e:
                print(f"Error generating ASCII art: {e}")
        return None

    def list_fonts(self):
        """Display available fonts"""
        fonts = self.font_manager.get_available_fonts()
        current_font = self.generator.get_current_font()
        
        print("\n" + "="*40)
        print("AVAILABLE FONTS:")
        print("="*40)
        for i, font in enumerate(fonts, 1):
            marker = " (CURRENT)" if font == current_font else ""
            print(f"{i}. {font}{marker}")
        print("="*40)

    def change_font(self):
        """Allow user to change the current font"""
        fonts = self.font_manager.get_available_fonts()
        self.list_fonts()
        
        try:
            choice = int(input(f"\nSelect font (1-{len(fonts)}): "))
            if 1 <= choice <= len(fonts):
                selected_font = fonts[choice - 1]
                self.generator.set_font(selected_font)
                print(f"Font changed to: {selected_font}")
            else:
                print("Invalid selection!")
        except ValueError:
            print("Please enter a valid number!")

    def preview_fonts(self):
        """Show preview of text in all available fonts"""
        text = input("Enter text for preview: ").strip()
        if not text:
            text = "Sample"
        
        fonts = self.font_manager.get_available_fonts()
        current_font = self.generator.get_current_font()
        
        for font in fonts:
            self.generator.set_font(font)
            try:
                preview = self.generator.text_to_ascii(text)
                print(f"\n--- {font} ---")
                print(preview)
            except:
                print(f"\n--- {font} --- (Error generating preview)")
        
        # Restore original font
        self.generator.set_font(current_font)

    def save_to_file(self):
        """Save ASCII art to a file"""
        text = self.get_user_input()
        if text:
            try:
                ascii_art = self.generator.text_to_ascii(text)
                filename = input("Enter filename (without extension): ").strip()
                if not filename:
                    filename = "ascii_art"
                
                full_path = self.file_handler.save_ascii_art(ascii_art, filename)
                print(f"ASCII art saved to: {full_path}")
            except Exception as e:
                print(f"Error saving file: {e}")

    def load_from_file(self):
        """Load text from a file and convert to ASCII"""
        filename = input("Enter filename: ").strip()
        if filename:
            try:
                text = self.file_handler.load_text_file(filename)
                if text:
                    ascii_art = self.generator.text_to_ascii(text)
                    print("\n" + "="*60)
                    print("ASCII ART FROM FILE:")
                    print("="*60)
                    print(ascii_art)
                    print("="*60)
            except Exception as e:
                print(f"Error loading file: {e}")

    def run(self):
        """Main application loop"""
        print("Welcome to Text-to-ASCII Art Generator!")
        
        while True:
            self.display_menu()
            choice = input("\nSelect an option (1-7): ").strip()
            
            if choice == '1':
                self.generate_art()
            elif choice == '2':
                self.list_fonts()
            elif choice == '3':
                self.save_to_file()
            elif choice == '4':
                self.load_from_file()
            elif choice == '5':
                self.change_font()
            elif choice == '6':
                self.preview_fonts()
            elif choice == '7':
                print("\nThank you for using Text-to-ASCII Art Generator!")
                sys.exit(0)
            else:
                print("Invalid option! Please select 1-7.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    app = TextToASCIIApp()
    app.run()