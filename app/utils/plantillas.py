from fastapi.templating import Jinja2Templates
import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
project_root = os.path.dirname(base_dir)

templates = Jinja2Templates(directory=os.path.join(project_root, "frontend", "templates"))

static_dir = os.path.join(project_root, "frontend", "static")


