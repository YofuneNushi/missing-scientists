"""Output formatting module for search results"""

from typing import List, Dict, Any


def format_results(results: List[Dict[str, Any]]) -> None:
    """
    Format and display search results in a readable way
    
    Args:
        results: List of search result dictionaries
    """
    if not results:
        print("No results found.")
        return
    
    print(f"Found {len(results)} result(s):\n")
    
    # Group results by source
    by_source = {}
    for result in results:
        source = result.get('source', 'Unknown')
        if source not in by_source:
            by_source[source] = []
        by_source[source].append(result)
    
    # Display results grouped by source
    for source, items in by_source.items():
        print(f"\n{'=' * 60}")
        print(f"From {source}:")
        print('=' * 60)
        
        for i, item in enumerate(items, 1):
            print(f"\n[{i}] {item.get('title', 'No title')}")
            print(f"    Snippet: {item.get('snippet', 'No description available')[:150]}...")
            print(f"    URL: {item.get('url', 'No URL available')}")
    
    print(f"\n{'=' * 60}\n")
