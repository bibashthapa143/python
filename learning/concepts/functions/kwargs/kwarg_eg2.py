# Example 2: build a settings dictionary with flexible options
def configure(**settings):
    print("Applying settings:")
    for key, value in settings.items():
        print(f" - {key} = {value}")

configure(theme="dark", font_size=14)
configure(theme="light")   # works fine with fewer settings too
