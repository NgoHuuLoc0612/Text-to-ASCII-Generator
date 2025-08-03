#!/usr/bin/env python3
"""
Font Manager Module
Handles font discovery, validation, and management for ASCII art generation
"""

try:
    import pyfiglet
    PYFIGLET_AVAILABLE = True
except ImportError:
    PYFIGLET_AVAILABLE = False

import os

class FontManager:
    def __init__(self):
        self.available_fonts = self._discover_fonts()
        self.fallback_fonts = ['standard', 'block', 'bubble', 'digital', 'lean']

    def _discover_fonts(self):
        """Discover all available fonts on the system"""
        if PYFIGLET_AVAILABLE:
            try:
                return pyfiglet.FigletFont.getFonts()
            except:
                return self.fallback_fonts
        else:
            return self.fallback_fonts

    def get_available_fonts(self):
        """Return list of available fonts"""
        return sorted(self.available_fonts)

    def is_font_available(self, font_name):
        """Check if a specific font is available"""
        return font_name in self.available_fonts

    def get_font_info(self, font_name):
        """Get information about a specific font"""
        if not self.is_font_available(font_name):
            return None
        
        info = {
            'name': font_name,
            'available': True,
            'type': 'pyfiglet' if PYFIGLET_AVAILABLE else 'fallback'
        }
        
        if PYFIGLET_AVAILABLE:
            try:
                fig = pyfiglet.Figlet(font=font_name)
                sample = fig.renderText('Abc')
                info['sample'] = sample
                info['height'] = len(sample.split('\n'))
            except:
                info['sample'] = 'Error generating sample'
                info['height'] = 0
        else:
            info['sample'] = 'Built-in fallback font'
            info['height'] = 5
        
        return info

    def get_popular_fonts(self):
        """Return a list of popular/recommended fonts"""
        popular = [
            'standard', 'slant', 'block', 'bubble', 'digital',
            'lean', 'mini', 'script', 'shadow', 'small'
        ]
        
        # Filter to only include available fonts
        available_popular = [font for font in popular if self.is_font_available(font)]
        
        # If no popular fonts are available, return first few available fonts
        if not available_popular:
            return self.get_available_fonts()[:10]
        
        return available_popular

    def search_fonts(self, keyword):
        """Search for fonts containing a specific keyword"""
        keyword = keyword.lower()
        matching_fonts = []
        
        for font in self.available_fonts:
            if keyword in font.lower():
                matching_fonts.append(font)
        
        return sorted(matching_fonts)

    def get_font_categories(self):
        """Categorize fonts by style/type"""
        categories = {
            'standard': [],
            'block': [],
            'script': [],
            'digital': [],
            'small': [],
            'decorative': [],
            'other': []
        }
        
        for font in self.available_fonts:
            font_lower = font.lower()
            
            if 'block' in font_lower or 'big' in font_lower:
                categories['block'].append(font)
            elif 'script' in font_lower or 'cursive' in font_lower:
                categories['script'].append(font)
            elif 'digital' in font_lower or 'lcd' in font_lower:
                categories['digital'].append(font)
            elif 'small' in font_lower or 'mini' in font_lower or 'tiny' in font_lower:
                categories['small'].append(font)
            elif any(word in font_lower for word in ['shadow', 'outline', 'border', 'star']):
                categories['decorative'].append(font)
            elif font in ['standard', 'lean']:
                categories['standard'].append(font)
            else:
                categories['other'].append(font)
        
        # Remove empty categories
        return {k: v for k, v in categories.items() if v}

    def validate_font(self, font_name):
        """Validate if a font works properly"""
        if not self.is_font_available(font_name):
            return False, "Font not found"
        
        if PYFIGLET_AVAILABLE:
            try:
                fig = pyfiglet.Figlet(font=font_name)
                test_output = fig.renderText('Test')
                if not test_output.strip():
                    return False, "Font produces empty output"
                return True, "Font is valid"
            except Exception as e:
                return False, f"Font validation error: {str(e)}"
        else:
            return True, "Font is valid (fallback mode)"

    def get_font_sample(self, font_name, sample_text="Sample"):
        """Generate a sample of text using the specified font"""
        if not self.is_font_available(font_name):
            return None
        
        if PYFIGLET_AVAILABLE:
            try:
                fig = pyfiglet.Figlet(font=font_name)
                return fig.renderText(sample_text)
            except:
                return f"Error generating sample for {font_name}"
        else:
            return f"Fallback font sample: {sample_text}"

    def compare_fonts(self, font_list, sample_text="ABC"):
        """Compare multiple fonts side by side"""
        if not font_list:
            return "No fonts to compare"
        
        comparison = []
        
        for font in font_list:
            if self.is_font_available(font):
                sample = self.get_font_sample(font, sample_text)
                comparison.append(f"=== {font} ===")
                comparison.append(sample if sample else "Error generating sample")
                comparison.append("")  # Empty line for separation
            else:
                comparison.append(f"=== {font} ===")
                comparison.append("Font not available")
                comparison.append("")
        
        return "\n".join(comparison)

    def get_random_font(self):
        """Get a random font from available fonts"""
        import random
        if self.available_fonts:
            return random.choice(self.available_fonts)
        return 'standard'

    def export_font_list(self, filename="fonts.txt"):
        """Export list of available fonts to a file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("Available ASCII Fonts\n")
                f.write("=" * 30 + "\n\n")
                
                for i, font in enumerate(self.get_available_fonts(), 1):
                    f.write(f"{i:3d}. {font}\n")
                
                f.write(f"\nTotal fonts: {len(self.available_fonts)}\n")
            
            return True, f"Font list exported to {filename}"
        except Exception as e:
            return False, f"Error exporting font list: {str(e)}"

    def get_font_stats(self):
        """Get statistics about available fonts"""
        total_fonts = len(self.available_fonts)
        categories = self.get_font_categories()
        
        stats = {
            'total_fonts': total_fonts,
            'pyfiglet_available': PYFIGLET_AVAILABLE,
            'categories': {cat: len(fonts) for cat, fonts in categories.items()},
            'popular_fonts_available': len(self.get_popular_fonts())
        }
        
        return stats