# RAW DATA
Maybe the script will keep some useless data in here.
Like not found or empty pages.

easy way to remove, using shell by following:
```bash
rm $(ls -l | grep -E 'staff\W+1\s' | grep -o '\d*$')
```
> **Warning**
> Please make sure you know what are you doing. 
> Any kind of damage to your computer will not be relative to the developer.
