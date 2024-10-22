# Task-Tracker
Task Tracker program from https://roadmap.sh/projects/task-tracker for people who want to learn python basics form me


# Quick start

- Install package with `pip install git+https://github.com/Cooperos/Task-Tracker-CLI`
- Run in console `task-cli -h` to see help info. You can add `-h` flag to all arguments to see description.

if you are having trobles with using `task-cli` command try setting up PYTHONPATH with `export PYTHONPATH="$HOME/path/to/project/src:$PYTHONPATH"` in Linux and `set PYTHONPATH=C:\path\to\project\src;%PYTHONPATH%` in Windows

# Usage examples
```bash
task-cli add "Make homework"
# Task added successfully (ID: 4)

task-cli delete 2
# Task 2 deleted successfully

task-cli list
# +------+---------------+-------------+----------------------------+----------------------------+
# |   ID | Description   | Status      | Created At                 | Updated At                 |
# +======+===============+=============+============================+============================+
# |    1 | First task    | in-progress | 2024-10-23T02:16:04.472142 | 2024-10-23T02:17:01.249714 |
# +------+---------------+-------------+----------------------------+----------------------------+
# |    3 | Go to sleep   | todo        | 2024-10-23T02:16:19.607030 | 2024-10-23T02:16:19.607046 |
# +------+---------------+-------------+----------------------------+----------------------------+
# |    4 | Make homework | done        | 2024-10-23T02:16:38.964371 | 2024-10-23T02:17:13.417137 |
# +------+---------------+-------------+----------------------------+----------------------------+
```