# Missing Scientists Finder

A Python application that searches the internet for information about missing scientists.

## Description

This application helps find information about missing or lost scientists by searching multiple web sources including:
- Wikipedia
- Google News
- General web search results

## Requirements

- Python 3.8+
- Internet connection for web searches

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YofuneNushi/missing-scientists.git
cd missing-scientists
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

Then enter the name of the scientist you want to search for:
```
=============================================================
Missing Scientists Finder
=============================================================

Enter scientist name or 'quit' to exit: Nikola Tesla
```

The application will search multiple sources and display results organized by source.

## Features

- **Multi-source search**: Searches Wikipedia, Google News, and general web results
- **Clean output**: Results are formatted and organized by source
- **Error handling**: Gracefully handles network errors and timeouts
- **Interactive interface**: Easy-to-use command-line interface

## Project Structure

```
missing-scientists/
├── main.py              # Main entry point
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── app/
    ├── __init__.py     # Package initialization
    ├── searcher.py     # Web search implementation
    └── formatter.py    # Output formatting
```

## How It Works

1. **Searcher Module** (`searcher.py`):
   - Implements `MissingScientistsFinder` class
   - Searches Wikipedia API for scientist information
   - Searches Google News for recent news
   - Performs general web searches
   - Handles timeouts and errors gracefully

2. **Formatter Module** (`formatter.py`):
   - Formats search results in a readable way
   - Groups results by source
   - Displays title, snippet, and URL for each result

3. **Main Application** (`main.py`):
   - Interactive command-line interface
   - Handles user input
   - Displays results to the user

## Future Enhancements

- Add database to cache search results
- Add filtering options (date range, source type, etc.)
- Export results to JSON/CSV format
- Add more search sources (academic databases, etc.)
- Add sentiment analysis for news results
- Create a web interface using Flask or Django

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
