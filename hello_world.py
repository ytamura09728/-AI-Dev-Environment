# Step 1: Define the HTML content with a writable line at the start
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
"""

# Step 2: Write the HTML content to a file
with open("hello_world.html", "w") as file:
    file.write(html_content)

# Display success message
print("HTML file 'hello_world.html' created successfully!")
