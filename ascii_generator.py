#!/usr/bin/env python3
"""
ASCII Art Generator Core Module
Handles the main text-to-ASCII conversion functionality
"""

try:
    import pyfiglet
    PYFIGLET_AVAILABLE = True
except ImportError:
    PYFIGLET_AVAILABLE = False

class ASCIIGenerator:
    def __init__(self):
        self.current_font = 'standard'
        self.fallback_patterns = self._load_fallback_patterns()
        
    def _load_fallback_patterns(self):
        """Load basic ASCII patterns for fallback when pyfiglet is not available"""
        return {
            'A': ['  A  ', ' A A ', 'AAAAA', 'A   A', 'A   A'],
            'B': ['BBBB ', 'B   B', 'BBBB ', 'B   B', 'BBBB '],
            'C': [' CCC ', 'C   C', 'C    ', 'C   C', ' CCC '],
            'D': ['DDD  ', 'D  D ', 'D   D', 'D  D ', 'DDD  '],
            'E': ['EEEEE', 'E    ', 'EEE  ', 'E    ', 'EEEEE'],
            'F': ['FFFFF', 'F    ', 'FFF  ', 'F    ', 'F    '],
            'G': [' GGG ', 'G   G', 'G  GG', 'G   G', ' GGG '],
            'H': ['H   H', 'H   H', 'HHHHH', 'H   H', 'H   H'],
            'I': ['IIIII', '  I  ', '  I  ', '  I  ', 'IIIII'],
            'J': ['JJJJJ', '    J', '    J', 'J   J', ' JJJ '],
            'K': ['K   K', 'K  K ', 'KKK  ', 'K  K ', 'K   K'],
            'L': ['L    ', 'L    ', 'L    ', 'L    ', 'LLLLL'],
            'M': ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M'],
            'N': ['N   N', 'NN  N', 'N N N', 'N  NN', 'N   N'],
            'O': [' OOO ', 'O   O', 'O   O', 'O   O', ' OOO '],
            'P': ['PPPP ', 'P   P', 'PPPP ', 'P    ', 'P    '],
            'Q': [' QQQ ', 'Q   Q', 'Q   Q', 'Q  QQ', ' QQQQ'],
            'R': ['RRRR ', 'R   R', 'RRRR ', 'R  R ', 'R   R'],
            'S': [' SSS ', 'S   S', ' SSS ', '    S', 'SSSS '],
            'T': ['TTTTT', '  T  ', '  T  ', '  T  ', '  T  '],
            'U': ['U   U', 'U   U', 'U   U', 'U   U', ' UUU '],
            'V': ['V   V', 'V   V', 'V   V', ' V V ', '  V  '],
            'W': ['W   W', 'W   W', 'W W W', 'WW WW', 'W   W'],
            'X': ['X   X', ' X X ', '  X  ', ' X X ', 'X   X'],
            'Y': ['Y   Y', ' Y Y ', '  Y  ', '  Y  ', '  Y  '],
            'Z': ['ZZZZZ', '   Z ', '  Z  ', ' Z   ', 'ZZZZZ'],
            ' ': ['     ', '     ', '     ', '     ', '     '],
            '!': ['  !  ', '  !  ', '  !  ', '     ', '  !  '],
            '?': [' ??? ', '?   ?', '   ? ', '     ', '  ?  '],
            '.': ['     ', '     ', '     ', '     ', '  .  '],
            ',': ['     ', '     ', '     ', '  ,  ', ' ,   '],
            '0': [' 000 ', '0   0', '0   0', '0   0', ' 000 '],
            '1': ['  1  ', ' 11  ', '  1  ', '  1  ', '11111'],
            '2': [' 222 ', '2   2', '   2 ', '  2  ', '22222'],
            '3': [' 333 ', '3   3', '  33 ', '3   3', ' 333 '],
            '4': ['4   4', '4   4', '44444', '    4', '    4'],
            '5': ['55555', '5    ', '5555 ', '    5', '5555 '],
            '6': [' 666 ', '6    ', '6666 ', '6   6', ' 666 '],
            '7': ['77777', '    7', '   7 ', '  7  ', ' 7   '],
            '8': [' 888 ', '8   8', ' 888 ', '8   8', ' 888 '],
            '9': [' 999 ', '9   9', ' 9999', '    9', ' 999 ']
        }

    def text_to_ascii(self, text):
        """Convert text to ASCII art"""
        if PYFIGLET_AVAILABLE:
            try:
                return self._generate_with_pyfiglet(text)
            except:
                return self._generate_fallback(text)
        else:
            return self._generate_fallback(text)

    def _generate_with_pyfiglet(self, text):
        """Generate ASCII art using pyfiglet library"""
        fig = pyfiglet.Figlet(font=self.current_font)
        return fig.renderText(text)

    def _generate_fallback(self, text):
        """Generate ASCII art using built-in patterns"""
        text = text.upper()
        lines = ['', '', '', '', '']
        
        for char in text:
            if char in self.fallback_patterns:
                pattern = self.fallback_patterns[char]
                for i in range(5):
                    lines[i] += pattern[i] + ' '
            else:
                # Unknown character - use question mark pattern
                pattern = self.fallback_patterns.get('?', ['?????'] * 5)
                for i in range(5):
                    lines[i] += pattern[i] + ' '
        
        return '\n'.join(lines)

    def set_font(self, font_name):
        """Set the current font for ASCII generation"""
        if PYFIGLET_AVAILABLE:
            try:
                # Test if font is valid
                pyfiglet.Figlet(font=font_name)
                self.current_font = font_name
                return True
            except:
                return False
        else:
            # Fallback mode - accept any font name but use built-in patterns
            self.current_font = font_name
            return True

    def get_current_font(self):
        """Get the currently selected font"""
        return self.current_font

    def get_text_width(self, text):
        """Calculate the width of ASCII art for given text"""
        if PYFIGLET_AVAILABLE:
            try:
                fig = pyfiglet.Figlet(font=self.current_font)
                ascii_art = fig.renderText(text)
                lines = ascii_art.split('\n')
                return max(len(line) for line in lines if line.strip())
            except:
                return len(text) * 6  # Fallback width calculation
        else:
            return len(text) * 6  # Each character is about 6 chars wide in fallback

    def get_text_height(self, text):
        """Calculate the height of ASCII art for given text"""
        if PYFIGLET_AVAILABLE:
            try:
                fig = pyfiglet.Figlet(font=self.current_font)
                ascii_art = fig.renderText(text)
                return len([line for line in ascii_art.split('\n') if line.strip()])
            except:
                return 5  # Fallback height
        else:
            return 5  # Fallback patterns are 5 lines high

    def create_border(self, ascii_art, border_char='*'):
        """Add a border around ASCII art"""
        lines = ascii_art.split('\n')
        if not lines:
            return ascii_art
        
        # Find the maximum width
        max_width = max(len(line) for line in lines)
        
        # Create top border
        top_border = border_char * (max_width + 4)
        
        # Create bordered lines
        bordered_lines = [top_border]
        for line in lines:
            padded_line = line.ljust(max_width)
            bordered_lines.append(f"{border_char} {padded_line} {border_char}")
        bordered_lines.append(top_border)
        
        return '\n'.join(bordered_lines)

    def center_text(self, ascii_art, width):
        """Center ASCII art within a given width"""
        lines = ascii_art.split('\n')
        centered_lines = []
        
        for line in lines:
            if len(line) < width:
                padding = (width - len(line)) // 2
                centered_line = ' ' * padding + line
                centered_lines.append(centered_line)
            else:
                centered_lines.append(line)
        
        return '\n'.join(centered_lines)