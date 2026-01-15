from file_management import ensure_file_exist
from const import DB_NAME
from db_class import *
import sqlite3

CONNECTOR: sqlite3.Connection
CURSOR: sqlite3.Cursor

db_path = ensure_file_exist(DB_NAME)
CONNECTOR = sqlite3.connect(db_path)
CURSOR = CONNECTOR.cursor()

def get_project_count() -> int:
    """
    :return: Number of projects
    """
    req = CURSOR.execute('SELECT count(projects.num) AS count FROM projects;')
    return req.fetchone()[0]

def get_n_project(n: int) -> Project|None:
    """
    :param n: Number of the search projects
    :return: tuple of "num", "title", "desc", "progress" in that oder
    """
    req = CURSOR.execute('SELECT "num", "title", "desc", "progress", "status", "icon" FROM projects ORDER BY num DESC LIMIT 1 OFFSET ?', [n])
    r = req.fetchone()
    if not r:
        return None
    num, title, desc, progress, status, icon = r
    return Project(num, title, desc, progress, status, icon)

def add_project(project: Project):
    """
    :param project: The project to add
    :return: nothing
    """
    args = (project.title, project.desc, project.progress, project.status, project.icon)
    CURSOR.execute('INSERT INTO projects ("title", "desc", "progress", "status", "icon") VALUES (?,?,?,?,?);', args)
    CONNECTOR.commit()

def get_project_num(title: str) -> int|None:
    args = [title]
    CURSOR.execute('SELECT num FROM projects WHERE title=? LIMIT 1;', args)
    r = CURSOR.fetchone()
    if not r:
        return None
    return r[0]

def get_project_by_num(num: int) -> Project|None:
    args = [num]
    CURSOR.execute('SELECT "num", "title", "desc", "progress", "status", "icon" FROM projects WHERE num=? LIMIT 1;', args)
    r = CURSOR.fetchone()
    if not r:
        return None
    num, title, desc, progress, status, icon = r
    return Project(num, title, desc, progress, status, icon)

def update_project(project: Project):
    args = (project.title, project.desc, project.progress, project.status, project.icon, project.num)
    CURSOR.execute('UPDATE projects SET title=?, desc=?, progress=?, status=?, icon=? WHERE num=?', args)
    CONNECTOR.commit()

def delete_project(project: Project):
    args = (project.num, )
    CURSOR.execute('DELETE FROM documentation WHERE project_num=?;', args)
    CURSOR.execute('DELETE FROM task WHERE project_num=?;', args)
    CURSOR.execute('DELETE FROM projects WHERE num=?;', args)
    CONNECTOR.commit()

# --- TASKS ---

def get_task_count(num_project: int, show_done: int) -> int:
    args = (num_project, show_done)
    CURSOR.execute('SELECT count(*) FROM task WHERE project_num=? AND status>=?;', args)
    return int(CURSOR.fetchone()[0])

def get_task_by_num(num: int) -> Task|None:
    args = (num,)
    CURSOR.execute('SELECT "num", "project_num", "title", "content", "status" FROM task WHERE num=?;', args)
    r = CURSOR.fetchone()
    if not r:
        return None
    num, project_num, title, content, status = r
    return Task(num, project_num, title, content, status)

def get_n_tasks_from(project_num: int, n:int, show_done: int) -> Task|None:
    args = (project_num,show_done, n )
    CURSOR.execute('SELECT "num", "project_num", "title", "content", "status" FROM task WHERE project_num=? AND status>=? ORDER BY num LIMIT 1 OFFSET ?;', args)
    r = CURSOR.fetchone()
    if not r:
        return None
    num, project_num, title, content, status = r
    return Task(num, project_num, title, content, status)

def update_task(task_num: int, title=None, content=None, status=None):
    args = (title, content, status, task_num)
    CURSOR.execute("""
    UPDATE task SET title=coalesce(?, title), content=coalesce(?, content), status=coalesce(?, status) WHERE num=?;
    """, args)
    CONNECTOR.commit()

def create_task(project_num:int):
    CURSOR.execute('INSERT INTO task (title, content, project_num, status) VALUES ("New Task", "issue/taks/todo", ?, 1);', (project_num,))
    CONNECTOR.commit()

def get_index_of_last_task(project_num:int) -> int|None:
    args = (project_num, project_num)
    CURSOR.execute("""SELECT COUNT(*) - 1
FROM task
WHERE project_num = ?
  AND num <= (
      SELECT MAX(num)
      FROM task
      WHERE project_num = ?
  );
""", args)
    r = CURSOR.fetchone()
    if not r:
        return None
    return r[0]

def delete_task(num:int):
    CURSOR.execute('DELETE FROM task WHERE num=?;', (num,))
    CONNECTOR.commit()

def get_doc_count(project_num:int) -> int:
    args = (project_num,)
    CURSOR.execute('SELECT count(*) FROM documentation WHERE project_num=?;', args)
    return int(CURSOR.fetchone()[0])

def get_doc_by_num(num: int) -> Doc|None:
    args = (num,)
    CURSOR.execute('SELECT "num", "project_num", "title", "content" FROM documentation WHERE num=?;', args)
    r = CURSOR.fetchone()
    if not r:
        return None
    num, project_num, title, content = r
    return Doc(num, project_num, title, content)

def get_n_docs_from(project_num:int, n:int) -> Doc|None:
    args = (project_num,n)
    CURSOR.execute('SELECT "num", "project_num", "title", "content" FROM documentation WHERE project_num=? ORDER BY num LIMIT 1 OFFSET ?;', args)
    r = CURSOR.fetchone()
    if not r:
        return None
    num, project_num, title, content = r
    return Doc(num, project_num, title, content)

def update_doc(doc_num: int, title=None, content=None):
    args = (title, content, doc_num)
    CURSOR.execute('UPDATE documentation SET title=coalesce(?, title), content=coalesce(?, content) WHERE num=?;', args)
    CONNECTOR.commit()

def delete_doc(doc_num:int):
    CURSOR.execute('DELETE FROM documentation WHERE num=?;', (doc_num, ))
    CONNECTOR.commit()

def add_doc(project_num:int):
    CURSOR.execute('INSERT INTO documentation(project_num, title) VALUES (?, "New doc");', (project_num,))
    CONNECTOR.commit()

if __name__ == '__main__':
    pass
    """c = get_project_count()
    print("Nombre de projects : ", c)
    for n in range(c):
        project = get_project_num(n)
        print("project n°", n, get_n_project(n).title)
    print("num de boldo : ", get_project_num("train"))"""
