import webbrowser
print("Smart Multi-Browser Search Assistant ")
print("Search across multiple browsers instantly!\n")
query = input("Enter your search query: ")
search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
browsers = {
    "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe %s",
    "brave": "C:\Users\bewar\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe%s",
    "firefox": "C:/Program Files/Mozilla Firefox/firefox.exe %s",
    "edge": "C:/Program Files/Microsoft/Edge/Application/msedge.exe %s"
}
print("\nChoose an option:")
print("1. Open in all browsers")
print("2. Choose specific browser")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    print("\nOpening in all browsers...")
    for name, path in browsers.items():
        try:
            webbrowser.get(path).open(search_url)
            print(f" Opened in {name.title()}")
        except:
            print(f"⚠ {name.title()} not found on this system.")
elif choice == "2":
    print("\nAvailable browsers:")
    for name in browsers:
        print(f"- {name.title()}")
    selected = input("Enter browser name: ").lower()
    if selected in browsers:
        try:
            webbrowser.get(browsers[selected]).open(search_url)
            print(f" Opened in {selected.title()}")
        except:
            print(f"{selected.title()} not found on this system.")
    else:
        print("Invalid browser name.")
else:
    print("Invalid choice. Please run again.")