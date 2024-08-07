# app/styles.py

# Define a consistent color scheme inspired by the technology sector for dark mode
colors = {
    'background': '#041424',   # Dark background
    'text': '#F8F9FA',         # Light text
    'primary': '#007BFF',      # Blue
    'secondary': '#6C757D',    # Gray
    'success': '#28A745',      # Green
    'info': '#17A2B8',         # Light Blue
    'warning': '#FFC107',      # Yellow
    'danger': '#DC3545',       # Red
    'light': '#343A40',        # Light Gray for dark mode elements
    'dark': '#041424',         # Dark Gray for text elements
}

# Sidebar styles for dark mode
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",  # Adjusted width
    "padding": "2rem 1rem",
    "background-color": colors['light'],
    "color": colors['text']
}

# Content styles for dark mode
CONTENT_STYLE = {
    "margin-left": "20rem",  # Adjusted margin
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": colors['background'],
    "color": colors['text']
}
