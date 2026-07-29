## Password-Manager
A simple local password manager built with Tkinter. It stores your credentials (website, email/username and password) in a JSON file and allows you to retrieve easily.

## Features  
- Logo Display – Shows a branded logo at the top.  
- Add Credentials – Enter a website, your email/username, and a password.  
- Generate Strong Passwords – Click the Generate Password button to create a random password containing letters, numbers, and symbols – instantly inserted into the password field.  
- Search Saved Entries – Enter a website name and click Search to retrieve the associated email and password.  
- Local Storage – All data is saved to a data.json file in the same directory.  
- Simple GUI – Clean and intuitive interface using Tkinter.

## Getting Started  
Prerequisites  
- Python 3.x (with Tkinter – usually bundled with Python)

Installation  
1. Clone or download this repository.  
2. Ensure you have Python installed.  
3. Place logo image (logo.png) in the project folder – the script looks for it by default.

## Usage  
1. Add a new password  
   · Fill in the Website, Email/Username, and Password fields.  
   · Click Add to save the entry to data.json.
2. Generate a random password  
   · Click the Generate Password button – a strong password will be created and filled into the password entry.  
3. Search for saved credentials.  
   · Enter the website name in the Website field.  
   · Click Search – if found, the email and password will be shown.  

## File Structure  
```
.
├── main.py   # Main application script  
└── logo.png  # logo image (icons8.com/icon/wOIqJRXQc1Jn/lock
```

## License  
This project is open source and available under the MIT License.