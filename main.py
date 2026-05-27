#!/usr/bin/env python3
"""
Missing Scientists Finder - Search for information about missing scientists
"""

import sys
from app.searcher import MissingScientistsFinder
from app.formatter import format_results


def main():
    """Main entry point for the application"""
    finder = MissingScientistsFinder()
    
    print("=" * 60)
    print("Missing Scientists Finder")
    print("=" * 60)
    print()
    
    while True:
        try:
            query = input("Enter scientist name or 'quit' to exit: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not query:
                print("Please enter a valid name.\n")
                continue
            
            print(f"\nSearching for information about {query}...\n")
            results = finder.search(query)
            
            if results:
                format_results(results)
            else:
                print(f"No information found for '{query}'.\n")
        
        except KeyboardInterrupt:
            print("\n\nExiting...")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
