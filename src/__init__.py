import os
import sys
from weather_dashboard import main

# Ensure the working directory is the project root, not src
if __name__ == "__main__":
    # Adjust sys.path to include the project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    # Change working directory to project root
    os.chdir(project_root)
    main()
