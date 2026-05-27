"""Web searcher module for finding information about missing scientists"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class MissingScientistsFinder:
    """Searches for information about missing scientists from the web"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        # Multiple search sources
        self.sources = [
            self._search_wikipedia,
            self._search_google_news,
            self._search_general_web
        ]
    
    def search(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for information about a missing scientist
        
        Args:
            query: Name of the scientist to search for
            
        Returns:
            List of results with information about the missing scientist
        """
        results = []
        
        for source_func in self.sources:
            try:
                source_results = source_func(query)
                if source_results:
                    results.extend(source_results)
            except Exception as e:
                logger.debug(f"Error in {source_func.__name__}: {e}")
        
        return results
    
    def _search_wikipedia(self, query: str) -> List[Dict[str, Any]]:
        """
        Search Wikipedia for information about the scientist
        
        Args:
            query: Name of the scientist
            
        Returns:
            List of results from Wikipedia
        """
        results = []
        try:
            url = "https://en.wikipedia.org/w/api.php"
            params = {
                'action': 'query',
                'list': 'search',
                'srsearch': f"{query} missing scientist",
                'srnamespace': 0,
                'srlimit': 5,
                'format': 'json'
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            for item in data.get('query', {}).get('search', []):
                results.append({
                    'source': 'Wikipedia',
                    'title': item['title'],
                    'snippet': item['snippet'].replace('<span class="searchmatch">', '').replace('</span>', ''),
                    'url': f"https://en.wikipedia.org/wiki/{item['title'].replace(' ', '_')}"
                })
        except Exception as e:
            logger.debug(f"Wikipedia search error: {e}")
        
        return results
    
    def _search_google_news(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for news about missing scientists
        
        Args:
            query: Name of the scientist
            
        Returns:
            List of news results
        """
        results = []
        try:
            url = f"https://news.google.com/search"
            params = {
                'q': f"{query} missing scientist"
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            # Parse news headlines if available
            articles = soup.find_all('article')
            
            for article in articles[:3]:
                try:
                    headline = article.find('h3')
                    if headline:
                        results.append({
                            'source': 'Google News',
                            'title': headline.get_text(),
                            'snippet': 'Breaking news about missing scientists',
                            'url': article.find('a')['href'] if article.find('a') else 'N/A'
                        })
                except:
                    pass
        except Exception as e:
            logger.debug(f"Google News search error: {e}")
        
        return results
    
    def _search_general_web(self, query: str) -> List[Dict[str, Any]]:
        """
        General web search for missing scientist information
        
        Args:
            query: Name of the scientist
            
        Returns:
            List of web results
        """
        results = []
        try:
            # Using a simple web search approach
            url = "https://www.google.com/search"
            params = {
                'q': f"\"{query}\" missing scientist"
            }
            
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            search_results = soup.find_all('div', class_='g')
            
            for result in search_results[:3]:
                try:
                    link = result.find('a')
                    title_elem = result.find('h3')
                    snippet_elem = result.find('div', class_='VwiC3b')
                    
                    if link and title_elem:
                        results.append({
                            'source': 'Web Search',
                            'title': title_elem.get_text(),
                            'snippet': snippet_elem.get_text() if snippet_elem else 'No description available',
                            'url': link['href']
                        })
                except:
                    pass
        except Exception as e:
            logger.debug(f"Web search error: {e}")
        
        return results
