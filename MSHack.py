import mshack
from time import sleep

mshack.set_save_dir("PDF")

print("""
### ### ### ### ### ### ### ### ### ### ### ###

      Music Score PDF Loader

### ### ### ### ### ### ### ### ### ### ### ### 
""")

while True:

    print("""
> Enter URL address of music sheet (example: https://musescore.com/user/30418467/scores/5575191)
> """, end='')

    url = input()

    path = None

    try:
        path = mshack.save_score(url)
    except Exception as e:
        print("> Error: ", "something went wrong while saving the score.")
        sleep(2)
        exit(1)

    if path == None:
        print("> Something went wrong...")
    else:
        print("> Successfully saved -> ", path)
    
    n = input("> Again (y/n)?")

    if n.lower() not in ['y', 'yes']:
        print("Bye!")
        sleep(2)