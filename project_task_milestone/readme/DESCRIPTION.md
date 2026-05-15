This module is kept as a compatibility bridge for databases where
`project_task_milestone` was installed before migrating to Odoo 19.0.

Its former behavior is now covered by Odoo core Project: tasks already have a
milestone field, milestones expose their related tasks, and the standard task
views/searches include milestone support.
