import webbrowser

def run():
    url = "http://localhost:3000/canvas/b66e70f9-2fe2-40b4-bc92-cfb59c0f46d6"
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(url)

# Call the run() function to open the browser immediately
