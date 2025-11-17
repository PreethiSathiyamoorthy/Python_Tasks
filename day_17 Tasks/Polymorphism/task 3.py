# Class for India
class India:
    def __init__(self):
        self.name = "India"   # Describe the Country name in constructor

    def capital(self):
        return "New Delhi"    # Describe the capital in capital function

    def language(self):
        return "Hindi (and many regional languages)"  # Describe the language in language function


# Class for USA
class USA:
    def __init__(self):
        self.name = "USA"

    def capital(self):
        return "Washington, D.C."

    def language(self):
        return "English"


# Class for UK
class UK:
    def __init__(self):
        self.name = "United Kingdom"

    def capital(self):
        return "London"

    def language(self):
        return "English"
obj1 = India()
obj2 = USA()
obj3 = UK()

# Print details for India
print("Country Name:", obj1.name)
print("Capital:", obj1.capital())
print("Language:", obj1.language())
print("-" * 10)

# Print details for USA
print("Country Name:", obj2.name)
print("Capital:", obj2.capital())
print("Language:", obj2.language())
print("-" * 10)

# Print details for UK
print("Country Name:", obj3.name)
print("Capital:", obj3.capital())
print("Language:", obj3.language())
