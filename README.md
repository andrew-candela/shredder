
# Shredder

Reduce the size of your database by dropping some percentage of it.

## How does it work?

If you mark a table for shredding, Shredder will hash the primary key
field, mod it by N, and delete the bottom X percent of records.

If a table marked for shredding contains the foreign key of another table,
then Shredder will delete the corresponding records in that child table.
Shredder will discover dependencies and delete records as needed.

## But my data is fancy

If you have a cycle in FK constraints, in a link table for example,
you can address the tables specifically in the config.
