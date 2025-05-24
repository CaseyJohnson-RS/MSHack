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
    > """)

    url = input()

    path = mshack.save_score(url)

    if path == None:
        print("> Something went wrong...")
    else:
        print("> Successfully saved -> ", path)
    
    n = input("> Again (y/n)?")

    if n.lower() not in ['y', 'yes']:
        print("Bye!")
        sleep(2)