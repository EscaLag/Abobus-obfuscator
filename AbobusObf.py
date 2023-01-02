# -*- coding: utf-8 -*-

from os import system
from os.path import isfile
from random import shuffle, choice, randint

logo = '''
   █████  ██████   ██████  ██████  ██    ██ ███████ 
  ██   ██ ██   ██ ██  ████ ██   ██ ██    ██ ██      
  ███████ ██████  ██ ██ ██ ██████  ██    ██ ███████  v2
  ██   ██ ██   ██ ████  ██ ██   ██ ██    ██      ██ 
  ██   ██ ██████   ██████  ██████   ██████  ███████ 
'''

####################################
#            settings:             #
class status:
    random_at                 = True
    random_semicolon          = True
    random_space              = False #possible crashes
    random_if                 = True
    code_obfuscation          = True
    random_newline            = False #possible crashes
    cleaning_comments         = True 
    lower_upper_character     = True
    function_name_obfuscation = False #this can break the argument system
    china_symbol              = True
####################################


def random_at(content: str) -> str:
    content = content.split('\n')
    result = ''
    for line in content:
        if len(line) > 1 and not line.startswith(' ') and not line.startswith('\t') and not line.startswith('@') and not line.startswith(')') and not line.startswith(';SE^T'):
            if randint(0, 10) < 6 and line[0] != ':':
                line = '@@' + line
            else:
                line = '@' + line
        result += line + '\n'
    return result

def random_semicolon(content: str) -> str:
    content = content.split('\n')
    result = ''
    for line in content:
        if len(line) > 1 and line[0] != ' ' and line[0] != ')' and ':A' not in line and ';SE^T' not in line:
            if randint(0,1) == 1:
                if randint(0, 10) >= 8 and line[0] != ':' and '@:' not in line:
                    line = '; ;' + line
                elif randint(0, 10) >= 6 and line[0] != ':' and '@:' not in line:
                    line = ';@;' + line
                elif line[0] != ':' and '@:' not in line:
                    line = ';' + line
        result += line + '\n'
    return result

def anti_detect(content: str) -> str:
    obf1 = list('ﭲسﺖﮚﮱﮕﯔتﮢﯤﺼكﻁﺹﭫ﷽◯')
    obf2 = ['ヾ(⌐■_■)ノ', '(◕‿◕)', '(⊙ω⊙)', '┌( ಠ_ಠ)┘']
    obf3 = list('此訊息已被神秘魔法保護凡人是無法複製貼上這行文字的')
    result = list(content)
    result.insert(randint(1, len(result) - 1), '^')
    rand = randint(1,3)
    for _ in range(2 if len(result) < 5 else 3):
        if rand == 1:
            result.insert(randint(1, len(result) - 1), "%" + easy_anti_detect(''.join([str(choice(obf1)) for _ in range(6)]) + "%"))
        elif rand == 2:
            result.insert(randint(1, len(result) - 1), "%" + easy_anti_detect(''.join([str(choice(obf2)) for _ in range(6)]) + "%"))
        elif rand == 3:
            result.insert(randint(1, len(result) - 1), "%" + easy_anti_detect(''.join([str(choice(obf3)) for _ in range(6)]) + "%"))
    result = ''.join(result)
    return result

def easy_anti_detect(content: str) -> str:
    word = list(content)
    word.insert(randint(1, len(word)-1), '^')
    return ''.join(word)

def substring_generation() -> dict:
    alphabet = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ @=")
    virable_name = list("阿贝色德饿艾豆贝尔维埃克斯爱耻")
    subsrtings = {}
    for _ in range(5):
        shuffle(alphabet)
        subsrtings["".join(choice(virable_name) for _ in range(4))] = "".join(alphabet)
    return subsrtings  

def substring_obfuscation(subsrtings: dict) -> list:
    obf_substrings = []
    i = 0
    alphabet = ['C', '\\\\', '\\\\', 'U', 's', 'e', 'r', 's', '\\\\', 'P', 'u', 'b', 'l', 'i', 'c']
    for key, source in subsrtings.items():
        if i != 1:
            previous_key = key
            previous_source = source
            first_source = ''
            for a in f'set "{key}={previous_source}"':
                if a in alphabet:
                    first_source += f'%public:~{alphabet.index(a)},1%'
                else:
                    first_source += a
            obf_substrings.append(first_source)
            i += 1
            continue
        result = ''
        for a in source:
            result += f'%{previous_key}:~{previous_source.find(a)},1%'
        set_ = ''
        for a in "@set":
            set_ += f'%{previous_key}:~{previous_source.find(a)},1%'
        equal = f'%{previous_key}:~{previous_source.find("=")},1%'

        obf_substrings.append(f'{set_} "{key}{equal}{result}"')
        previous_key, previous_source = key, source
    return obf_substrings

def code_obfuscation(content: str, subsrtings: dict) -> str:
    keys = []
    values = []
    result = []
    for i in subsrtings.values(): values.append(i)
    for i in subsrtings.keys(): keys.append(i)
    content = content.split('\n')
    for _a in range(len(content)):
        temp_content = content[_a]
        if temp_content != '':
            if temp_content.startswith(':'):
                result.append(temp_content)
            else:
                temp_result = ''
                status = False
                for i in temp_content:
                    if status == False and i == '%' or i == '!':
                        status = True
                        temp_result += '%' if i == '%' else '!'
                        continue
                    if status == True and i == '%' or i == '!':
                        status = False
                    score = randint(0, len(values)-1)
                    value = values[score]
                    if i in value and status == False:
                        temp_result += f'%{keys[score]}:~{value.find(i)},1%'
                    else:
                        temp_result += i
            result.append(temp_result)
    return '\n'.join(result)

def random_newline(content: str) -> str:
    content = content.split('\n')
    for i in range(5):
        content.insert(randint(0,len(content)), ''.join('\n' * randint(1,10)))
    return '\n'.join(i for i in content)

def random_space(content: str) -> str:
    content = content.split('\n')
    result = ''
    for i in content:
        if not ':' in i[:5]:
            result += f"{' ' * randint(70,300)} {i}\n"
        else:
            result += i+'\n'
    return result

def lower_upper_character(content: str, antidetect: bool) -> str:
    result = ''
    for a in content:
        result += a.upper() if randint(1,3) == 1 else a
    return result if antidetect == False else easy_anti_detect(result)

def random_if(content :str, name_file :str) -> str:
    content = content.split('\n')
    random_ifs = [f'if {randint(1,50)} EQU 0 (@exit) else ', f'if 1 EQU 1 ', f'if {randint(0,100)} LsS {randint(101,150)} ',
                f'if {anti_detect("exist")} %{name_file}% ', f'for /l %%y in ({"1 1 1" if randint(1,2) == 1 else "1,1,1"}) do ']
    result = []
    for i in range(len(content)):
        cont = content[i]
        if cont.startswith('(') or cont.startswith(')') or cont.startswith(':'):
            result.append(cont)
        else:
            result.append(choice(random_ifs) + cont)
    return '\n'.join(result)

def function_name_obfuscation(content :str) -> str:
    obf = ["i", "l"]
    result = []
    content = content.split('\n')
    for line in content:
        if len(line) > 1 and line[0] == ':':
            if len(line[1:]) != 1:
                result.append(f':{easy_anti_detect(line[1:])}  {anti_detect("".join([str(choice(obf)) for _ in range(11)]))}   {anti_detect("".join([str(choice(obf)) for _ in range(11)]))}')
            else:
                result.append(f':{line[1:]}  {anti_detect("".join([str(choice(obf)) for _ in range(11)]))}   {anti_detect("".join([str(choice(obf)) for _ in range(11)]))}')
        else:
            result.append(line)
    return '\n'.join(result)

def cleaning_comments(content :str) -> str:
    content = content.split('\n')
    result = []
    for i in range(len(content)):
        cont = content[i]
        if not cont.lower().startswith('::') or not cont.lower().startswith('rem'):
            result.append(cont)
    return '\n'.join(result)  

def password_generate(lengt: int) -> str:
    #all these 3 characters are completely different
    сhar = ["o", "ο", "о"]
    return ''.join(choice(сhar) for i in range(lengt))


def main() -> None:
    print(logo)
    file = input(r'Drag your Batch file: ').replace('\\', '/').replace('"', '') # this replacement to work correctly with the file
    if not isfile(file):
        print("This file does not exist!")

    subsrtings = substring_generation()
    obf_substrings = substring_obfuscation(subsrtings) 

    content = open(file, 'rb').read().decode("utf-8")
    
    #clearing empty cells in a list
    content = content.split('\r\n')
    content = list(filter(None, content))
    content = '\n'.join(content)
    
    name_file = ''.join([str(choice(["i", "l"])) for _ in range(11)])
    
    if status.cleaning_comments == True:
        content = cleaning_comments(content)
    
    if status.code_obfuscation == True:
        content = code_obfuscation(content, subsrtings)
    
    if status.random_if == True:
       content = random_if(content, name_file)
    if status.function_name_obfuscation == True:
        content = function_name_obfuscation(content)
    
    password = password_generate(lengt=5)
    defense = f'''(@{anti_detect('chcp.com')} {easy_anti_detect('437')})>nul&@{anti_detect('echo')} {anti_detect('off')}&{anti_detect('cls')}&&{anti_detect('set')} {anti_detect(name_file)}=%0&{anti_detect('set')} 𝧽= c'''
    # anti-logged system, it will not be possible to log the script. Logging example: script-obf.bat > 1.log
    #f'''@{anti_detect('echo')} {anti_detect('ABOBUS')} {anti_detect('OBFUSCATION')} {anti_detect('PROTECTION🛡')}&cls&if "%~1" EQU "{password}" (@{anti_detect('goto')} {anti_detect('ABOBUS')}-{anti_detect('OBFUSCATOR')}) else (@{anti_detect('start')} {easy_anti_detect('cmd')} /C "call %0 {password}")&{anti_detect('exit')}''' +\
    
    defense += '''
:ABOBUS-OBFUSCATOR\n
;SE^T "__author__=EscaLag"
;SE^T "__github__=github.com/EscaLag/Abobus-obfuscator"\n\n'''

    protects = [
        # echo trap, if you add "echo" at the beginning of this line, it spams and exits the script
        f'''@{anti_detect('find')} >nul 2>&1&&for /l %%c in (.)do (@{anti_detect('echo')} {anti_detect('ABOBUS')} {anti_detect('OBFUSCATION')})||@{anti_detect('exit')}''',
        f'''@{anti_detect('find')} >nul 2>&1&&for /l %%c in (.)do (@{anti_detect('echo')} {anti_detect('ABOBUS')} {anti_detect('OBFUSCATION')})||@{anti_detect('exit')}''',
        # checking for the existence of variables
        f'''@{anti_detect('set')} /a ‎+=1 >nul &for /l %%i in ({'1 1 1' if randint(1,2) == 1 else '1,1,1'}) do for %%a in ( {anti_detect(name_file)} {anti_detect('__author__')} {anti_detect('__github__')})do if {anti_detect('not')} {anti_detect('defined')} %%a {anti_detect('exit')}''',
        # checking the script for the existence of words from the black list
        f'''@{anti_detect('set')} /a ‎+=1 >nul &for %%a in ( {anti_detect('set')} {anti_detect('goto')} {anti_detect('echo')} {anti_detect('pause')} )do @{anti_detect('findstr')} /L /I %%a %{name_file}%&&{anti_detect('exit')}''',
        # one more echo trap
        f'''{anti_detect('set')} b=1 >nul 2>&1 & if {anti_detect('not')} {anti_detect('defined')} b (@{anti_detect('echo')} =D&@{anti_detect('pause')}&@{anti_detect("exit")})''',
        # check for echo status, if @echo on then exit the script
        f'''{anti_detect('echo')}>tmp&@for /f "tokens=3" %%i in ('{anti_detect("type")} tmp')do if "%%i" EQU "on." (@{anti_detect("exit")}) else (@{anti_detect("del")} /f/q tmp)''',
    ]
    shuffle(protects)
    protest = []
    for i in range(len(protects) + len(obf_substrings)):
        try:
            protest.append(protects[i])
            protest.append(obf_substrings[i])
        except IndexError:pass
    # checking if all checks have been completed
    protest.append(f'if %‎% NEq 2 {anti_detect("exit")}')
    protest.append(f'''{anti_detect('echo')}>tmp&for /f "tokens=3" %%i in ('{anti_detect("type")} tmp')do if "%%i" EQU "on." ({anti_detect("exit")}) else ({anti_detect("del")} /f/q tmp)''')
    defense += '\n'.join(protest) + '\n'

    if status.china_symbol == True:
        # check for error level, utf-16 special bytes give an error to the console, if this error is not present, then the protection of china characters has been removed
        defense = f'{anti_detect("echo")} {anti_detect("off")}&for /l %%i in ({"1 1 1" if randint(1,2) == 1 else "1,1,1"})do (for /l %%i in ({"1 1 1" if randint(1,2) == 1 else "1,1,1"})do (if %errorlevel% EQU 0 {anti_detect("exit")}))\n' + defense
    content = '\n'.join(list(filter(None, content.split('\n'))))
    defense += content + '\n'
    result = defense 
    
    if status.random_newline == True:
        result = random_newline(result)
    if status.lower_upper_character == True:
        temp = []
        for line in result.split('\n'):
            line = line.replace('off',     anti_detect(lower_upper_character('off', False)))
            line = line.replace('do ',        lower_upper_character('do ', False))
            line = line.replace('in',        lower_upper_character('in', False))
            line = line.replace('if',        lower_upper_character('if', False if randint(0,1) == 1 else True))
            line = line.replace('nul',       lower_upper_character('nul', True))
            line = line.replace('EQU',       anti_detect(lower_upper_character('EQU', False)))
            line = line.replace('NEq',       anti_detect(lower_upper_character('NEq', False)))
            line = line.replace('call',      anti_detect(lower_upper_character('call ', True)))
            line = line.replace('echo',      anti_detect(lower_upper_character('echo', True)))
            line = line.replace('public',    lower_upper_character('public', False))
            line = line.replace(name_file,   lower_upper_character(name_file, False))
            line = line.replace('errorlevel', lower_upper_character('errorlevel', False))
            line = line.replace('for',       anti_detect(lower_upper_character('for', False)))
            line = line.replace('set ',    anti_detect(lower_upper_character('set ', False)))
            temp.append(line)
        result = '\n'.join(str(syn) for syn in temp)

    if status.random_at == True:
        result = random_at(result)
    if status.random_semicolon == True:
        result = random_semicolon(result)
    if status.random_space == True:
        result = random_space(result)

    
    name = file[:-4]+'-obf'
    with open(name+'.bat', 'w', encoding="utf-8", errors='ignore') as f:
    	f.write(result)

    if status.china_symbol == True:
        utf16_bytes = ['FE', 'FE', 'FF']
        shuffle(utf16_bytes)
        utf16_bytes.insert(0, 'FF')
        result = result.encode()
        with open(name+'.bat', 'wb') as f:
                f.write(bytes.fromhex("".join(utf16_bytes))+ b">nul 2>&1 &cls\n" + result)
    print('\nsuccessful!')
    try:
        system('pause >nul')
    except:pass

if __name__ == '__main__':
    main()