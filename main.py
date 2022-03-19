from Infrastructure.repo import DepartmentRepository
from ui.console import DepUI

repo = DepartmentRepository()
ui = DepUI(repo)
ui.start()
