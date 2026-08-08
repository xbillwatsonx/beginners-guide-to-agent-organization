# Prompt 05: Before You Create A Folder

Use this whenever your agent wants to create a new durable folder.

```text
Before creating a new folder, please stop and answer these questions.

1. What exactly are you trying to store?
2. Is this temporary or durable?
3. Which existing folders did you check first?
4. Why do the existing homes not fit?
5. What folder name do you propose?
6. Where exactly would it live?
7. What belongs in it?
8. What does not belong in it?
9. Should this new folder be added to DIRECTORY_ATLAS.md?
10. Do you need my approval before creating it?
11. What does the Path Resolution Preflight report as the expanded absolute path?
12. Does it report a duplicated segment, unresolved variable, missing parent, unexpected symlink, or established equivalent root?

Run `python3 path-resolution-preflight.py '<requested-path>'` with the requested path quoted. Do not create the folder until you have answered, the preflight is clear, and I have approved if the folder is durable, top-level, sensitive, suspicious, or unclear.

After creating it, run `python3 path-resolution-preflight.py --verify-existing '<absolute-destination>'` and report the verified absolute destination.
```
