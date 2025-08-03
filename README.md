# Text-to-ASCII Art Generator

A Python application for converting text into ASCII art with multiple fonts, file management, and advanced features.

## Features

- **Multiple Font Support**: Choose from dozens of ASCII art fonts
- **File Operations**: Save and load ASCII art and text files
- **Batch Processing**: Generate multiple ASCII arts at once
- **Export Options**: Save as TXT, HTML, or JSON with metadata
- **Font Management**: Browse, preview, and manage available fonts
- **Text Processing**: Clean and validate input text
- **Backup System**: Create backups of your ASCII art collection

## Installation

1. **Clone or download the project files**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python main.py
   ```

## Requirements

- Python 3.6 or higher
- pyfiglet library (automatically installed with requirements.txt)

## File Structure

```
text-to-ascii-generator/
├── main.py              # Main application entry point
├── ascii_generator.py   # Core ASCII generation functionality
├── font_manager.py      # Font discovery and management
├── file_handler.py      # File input/output operations
├── utils.py            # Utility functions and helpers
├── requirements.txt    # Project dependencies
├── README.md          # This documentation file
└── ascii_output/      # Directory for saved ASCII art (created automatically)
```

## Usage

### Basic Usage

1. Run the application: `python main.py`
2. Select option 1 to generate ASCII art
3. Enter your text when prompted
4. View the generated ASCII art

### Advanced Features

#### Font Management
- **List Fonts**: View all available fonts
- **Change Font**: Select a different font for generation
- **Preview Fonts**: See how text looks in different fonts

#### File Operations
- **Save ASCII Art**: Save generated art to text files
- **Load Text**: Load text from files for conversion
- **Export HTML**: Create web-ready HTML files with styling
- **Batch Save**: Save multiple ASCII arts in one file

#### Menu Options

1. **Generate ASCII Art** - Convert text to ASCII art
2. **List Available Fonts** - Show all available fonts
3. **Save ASCII Art to File** - Save generated art
4. **Load Text from File** - Load text from file
5. **Change Font** - Select different font
6. **Preview All Fonts** - Preview text in all fonts
7. **Exit** - Close the application

## Examples

### Simple Text Conversion
```
Input: "Hello"
Output:
 _   _      _ _       
| | | | ___| | | ___  
| |_| |/ _ \ | |/ _ \ 
|  _  |  __/ | | (_) |
|_| |_|\___|_|_|\___/ 
```

### Different Fonts
The application supports multiple fonts including:
- standard (default)
- slant
- block
- bubble
- digital
- lean
- script
- shadow
- And many more!

## File Output

Generated ASCII art is saved in the `ascii_output/` directory with:
- Timestamp in filename
- Header with generation information
- Original text and font information (in metadata files)

## Error Handling

The application includes robust error handling for:
- Missing fonts (falls back to built-in patterns)
- File operation errors
- Invalid input text
- System compatibility issues

## Fallback Mode

If the pyfiglet library is not available, the application automatically switches to fallback mode using built-in ASCII patterns for basic functionality.

## Customization

### Adding Custom Fonts
If using pyfiglet, additional fonts can be installed system-wide and will be automatically detected.

### Modifying Output
Edit the file_handler.py to customize:
- Output directory location
- File naming conventions
- HTML styling
- Metadata format

## Troubleshooting

### Common Issues

1. **"Font not found" error**
   - Make sure pyfiglet is installed
   - Check available fonts with option 2

2. **File save errors**
   - Ensure write permissions in the project directory
   - Check disk space availability

3. **Display issues**
   - Use a monospace font in your terminal
   - Ensure terminal supports UTF-8 encoding

### System Compatibility

- **Windows**: Fully supported
- **macOS**: Fully supported  
- **Linux**: Fully supported

## Contributing

This project is designed to be educational and easily extensible. Feel free to:
- Add new fonts
- Improve the user interface
- Add new export formats
- Enhance error handling

## License

This project is provided as-is for educational purposes. The pyfiglet library has its own license terms.

## Version History

- **v1.0.0**: Initial release with core functionality
  - Basic ASCII art generation
  - Multiple font support
  - File save/load operations
  - Font management system
  - HTML export capability
  - Comprehensive error handling