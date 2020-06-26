def create_message_cube(Message,cube_width,cube_lines): #''cube_lines'' is cube's height
    length = len(str(Message))
    print('-'*cube_width)
    for i in range(cube_lines):
        if abs(cube_lines//2) == i:
            if Is_CN_Word(Message):
                print('=', ' '*abs(cube_width//2 - 3 -  length),\
                f'{Message}', ' '*abs(cube_width//2 - 3 - length),'=')
            elif not Is_CN_Word(Message):
                print('=', ' '*abs(cube_width//2 - 3 -  length//2),\
                f'{Message}', ' '*abs(cube_width//2 - 3 - length//2),'=')
        else:
            print('=',' '*(cube_width - 4),'=')
    print('-'*cube_width)


def Is_CN_Word(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True     #Is CN word
    return False            #Is EN word or number
