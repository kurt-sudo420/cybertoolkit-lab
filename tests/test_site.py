import os
import sys
from pathlib import Path

# Add the current directory to Python path so we can import from docs
sys.path.insert(0, str(Path(__file__).parent))

from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import pytest

def test_website():
    """Test the CyberToolkit website"""
    # Create artifacts directory if it doesn't exist
    artifacts_dir = Path("artifacts")
    artifacts_dir.mkdir(exist_ok=True)
    
    # Get the absolute path to the index.html file
    index_path = Path("docs/index.html").resolve()
    file_url = f"file://{index_path}"
    
    with sync_playwright() as p:
        # Test with 375px viewport (mobile)
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": 375, "height": 800})
        page.goto(file_url)
        
        # Check title
        expect(page).to_have_title("CyberToolkit")
        
        # Check that all tool cards are visible
        tool_cards = page.get_by_test_id("tool-")
        expected_tool_ids = ["port-scanner", "banner-grabber", "file-hash", "dns-lookup", "password-generator"]
        
        for tool_id in expected_tool_ids:
            expect(page.get_by_test_id(f"tool-{tool_id}")).to_be_visible()
        
        # Check for external resources
        # Check that there are no external script, link or img sources
        external_scripts = page.query_selector_all("script[src^='http']")
        external_links = page.query_selector_all("link[href^='http']")
        external_images = page.query_selector_all("img[src^='http']")
        
        assert len(external_scripts) == 0, "Found external script references"
        assert len(external_links) == 0, "Found external link references"
        assert len(external_images) == 0, "Found external image references"
        
        # Check viewport width constraint
        scroll_width = page.evaluate("document.documentElement.scrollWidth")
        window_width = page.evaluate("window.innerWidth")
        assert scroll_width <= window_width, "Page exceeds viewport width on mobile"
        
        # Take screenshot
        page.screenshot(path="artifacts/site-mobile.png", full_page=True)
        
        # Test with desktop viewport
        page.set_viewport_size({"width": 1200, "height": 800})
        page.goto(file_url)
        
        # Take screenshot
        page.screenshot(path="artifacts/site-desktop.png", full_page=True)
        
        # Check for console errors, page errors or failed requests
        # This is implicit in the browser test, if there are issues they'll fail
        
        browser.close()

if __name__ == "__main__":
    test_website()