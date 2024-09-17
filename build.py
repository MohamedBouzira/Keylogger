import os
import subprocess
import sys

def build_executable(script_name, output_name):
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller is not installed. Please install it using 'pip install pyinstaller'.")
        sys.exit(1)
    
    # Define PyInstaller command
    command = [
        'pyinstaller',
        '--onefile',
        '--noconsole',
        '--name', output_name,
        script_name
    ]
    
    print(f"Building executable from {script_name}...")
    
    # Run PyInstaller command
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Check for errors
    if result.returncode != 0:
        print("Error building executable:")
        print(result.stderr)
        sys.exit(1)
    
    print("Build successful!")
    print(f"Executable can be found in the 'dist' directory.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python build.py <script_name.py> <output_name>")
        sys.exit(1)
    
    script_name = sys.argv[1]
    output_name = sys.argv[2]
    
    build_executable(script_name, output_name)
