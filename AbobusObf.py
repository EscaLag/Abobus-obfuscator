# -*- coding: utf-8 -*-

from os import getcwd, system
from base64 import b64decode
from random import shuffle, choice, randint
from os.path import isfile, isdir
import subprocess

logo = '''
   █████  ██████   ██████  ██████  ██    ██ ███████ 
  ██   ██ ██   ██ ██  ████ ██   ██ ██    ██ ██      
  ███████ ██████  ██ ██ ██ ██████  ██    ██ ███████ 
  ██   ██ ██   ██ ████  ██ ██   ██ ██    ██      ██ 
  ██   ██ ██████   ██████  ██████   ██████  ███████ 
'''

####################################
#            settings:             #
status_random_at           = True
status_random_semicolon    = True
status_random_space        = False #possible crashes
status_random_chunk        = True
status_random_if           = True
status_obf_charagter       = True
status_random_newline      = False #possible crashes
status_cleaning_comments   = True 
status_lower_upper_character = True
status_china_symbol        = False
####################################

def random_at(content: str):
    content = content.split('\n')
    res = ''
    for i in content:
        line = i
        if len(line) > 1 and line[0] != ' ' and line[0] != '@' and line[0] != ')' and ':A' not in line and ';SE^T' not in line:
            if randint(0,1) == 1:
                if randint(0, 10) < 7 and line[0] != ':':
                    line = '@@' + line
                else:
                    line = '@' + line
        res += line + '\n'
    return res

def random_semicolon(content: str):
    content = content.split('\n')
    res = ''
    for i in content:
        line = i
        if len(line) > 1 and line[0] != ' ' and line[0] != ')' and ':A' not in line and ';SE^T' not in line:
            if randint(0,1) == 1:
                if randint(0, 10) >= 8 and line[0] != ':' and '@:' not in line:
                    line = '; ;' + line
                elif randint(0, 10) >= 6 and line[0] != ':' and '@:' not in line:
                    line = ';@;' + line
                elif line[0] != ':' and '@:' not in line:
                    line = ';' + line
        res += line + '\n'
    return res

def anti_detect(content: str):
    obf1 = list('ﭲسﺖﮚﮱﮕﯔتﮢﯤﺼكﻁﺹﭫ﷽◯')
    obf2 = ['ヾ(⌐■_■)ノ', '(◕‿◕)', '(⊙ω⊙)', '┌( ಠ_ಠ)┘']
    obf3 = list('此訊息已被神秘魔法保護凡人是無法複製貼上這行文字的')
    result = list(content)
    result.insert(randint(1, len(result) - 1), '^')
    ms = randint(1,3)
    for _ in range(2 if len(result) < 5 else 3):
        if ms == 1:
            result.insert(randint(1, len(result) - 1), "%" + easy_anti_detect(''.join([str(choice(obf1)) for _ in range(6)]) + "%"))
        elif ms == 2:
            result.insert(randint(1, len(result) - 1), "%" + easy_anti_detect(''.join([str(choice(obf2)) for _ in range(6)]) + "%"))
        elif ms == 3:
            result.insert(randint(1, len(result) - 1), "%" + easy_anti_detect(''.join([str(choice(obf3)) for _ in range(6)]) + "%"))
    result = ''.join(result)
    return result

def easy_anti_detect(random_goto: str):
    goto = list(random_goto)
    goto.insert(randint(1, len(goto) - 1), '^')
    return ''.join(goto)


# обфусцирует символы в переменную
def obf_charagter(content: str):
    alphabet = ['J', 'g', 'i', 'g', 't', 'G', 'X', 'z', 's', 'w', 'b', 'h', 'm', 'u', 'S', 'H', 'I', 'O', 'A', '2', '3', '0']
    shuffle(alphabet)
    alphabetv2 = ['C', '\\\\', '\\\\', 'U', 's', 'e', 'r', 's', '\\\\', 'P', 'u', 'b', 'l', 'i', 'c']
    result = []
    content = content.split('\n')
    for _a in range(len(content)):
        temp_content = content[_a]
        if temp_content != '':
            if temp_content[0] == ':':
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
                    if i in alphabet and status == False:
                        _res = f"%‎ඞ‎:~{alphabet.index(i)},1%"
                        temp_result += _res
                    elif i in alphabetv2 and status == False:
                        _res = f"%public:~{alphabetv2.index(i)},1%"
                        temp_result += _res
                    else:
                        temp_result += i

                result.append(temp_result)
    result = '\n'.join(result)
    return f"""{anti_detect('set')} ‎ඞ‎={anti_detect(''.join(str(sym) for sym in alphabet))}\n{result}"""

#рандомные красные линии
def random_newline(content: str):
    content = content.split('\n')
    result = ''
    for i in content:
        result += i + '\n' * randint(0, 10)
    return result

def random_space(content: str):
    content = content.split('\n')
    res = ''
    for i in content:
        res += f"{' ' * randint(70,300)} {i}\n"
    return res



def lower_upper_character(content: str, antidetect: bool):
    temp = ''
    for a in content:
        temp += a.upper() if randint(1,4) == 1 else a
    return temp if antidetect == False else easy_anti_detect(temp)

def random_chunk(content: str):
    content = content.split('\n')
    obf = ["i", "l"]
    #obf = ['ﭲ', 'س', 'ﺖ', 'ﮚ', 'ﮱ', 'ﮕ', 'ﯔ', 'ت', 'ﮢ', 'ﯤ', 'ﺼ', 'ك', 'ﻁ', 'ﺹ', 'ﭫ']
    res = ''
    random_chunk = []
    for _ in range(11):
        random_chunk.append(anti_detect(choice(obf) + choice(obf) + choice(obf) + choice(obf) + choice(obf)) + '>nul 2>&1 || ')
    for i in content:
        line = i
        if len(line) > 1 and line[0] != ' ' and line[0] != ')':
            if randint(0,1) == 1:
                if randint(0, 10) <= 5 and line[0] != ':'  and line[0] != ')' and line[0] != '(' and '@:' not in line and '@@:' not in line and ';SE^T' not in line:
                    line = choice(random_chunk) + line
        res += line + '\n'
    return res

def random_if(content :str, name_file :str):
    obf = ["i", "l"]
    content = content.split('\n')
    random_ifs = ['if 1 EQU 0 (@exit) else ', 'if 1 EQU 1 ', 'if 5 LsS 10 ', f'if exist %{name_file}% ', 'for /l %%y in (1,1,1) do ']
    result = []
    for i in range(len(content)):
        cont = content[i]
        if cont.lower().startswith('(') or cont.lower().startswith(')'):
            result.append(cont)
        elif cont.lower().startswith(':'):
            result.append(f':{easy_anti_detect(cont[1:])}  {anti_detect("".join([str(choice(obf)) for _ in range(11)]))}   {anti_detect("".join([str(choice(obf)) for _ in range(11)]))}\n')
        else:
            result.append(choice(random_ifs) + cont)
    
    return '\n'.join(result)

def cleaning_comments(content :str):
    content = content.split('\n')
    result = []
    for i in range(len(content)):
        cont = content[i]
        if cont.lower().startswith('::') or cont.lower().startswith('rem'):
            pass
        else:
            result.append(cont)
    return '\n'.join(result)    

def main():
    global status_random_at, status_random_space, status_obf_charagter, status_random_newline, status_lower_upper_character, status_random_if, status_cleaning_comments
    print(logo)
    file = input('Drag your Batch file: ')
    if not file.strip() or not isfile(file):
        exit("This file does not exist!")


    content = open(file, 'rb').read().decode("utf-8")
    
    #очистка от пустых ячеек
    content = content.split('\r\n')
    content = list(filter(None, content))
    
    obf = ["i", "l"]
    name_file = ''.join([str(choice(obf)) for _ in range(11)])
    
    content.append('exit')
    content = '\n'.join(content)
    if status_cleaning_comments == True:
        content = cleaning_comments(content)
    if status_obf_charagter == True:
        content = obf_charagter(content)
    if status_random_if == True:
       content = random_if(content, name_file)
    #content = content.split('\n')


    result = f'''{anti_detect('@echo')} {anti_detect('off')}&{anti_detect('set')} /a ‎=1 >nul&{anti_detect('cls')}&&{anti_detect('set')} {anti_detect(name_file)}=%0\n
;SE^T __author__=EscaLag
;SE^T __github__=LINK\n
{anti_detect('find')} >nul 2>&1&&for /l %%c in (.)do ({anti_detect('echo')} {anti_detect('ABOBUS')} {anti_detect('OBFUSCATION')})||{anti_detect('exit')}
{anti_detect('set')} /a ‎+=1 >nul &for /l %%i in (1 1 1) do for %%a in ( {anti_detect(name_file)} {anti_detect('__author__')} {anti_detect('__github__')})do if {anti_detect('not')} {anti_detect('defined')} %%a {anti_detect('exit')}
{anti_detect('set')} /a ‎+=1 >nul &for %%a in ( {anti_detect('set')} {anti_detect('goto')} {anti_detect('echo')} {anti_detect('pause')})do {anti_detect('findstr')} /L /I %%a %{name_file}%&&{anti_detect('exit')}
{anti_detect('set')} /a ‎+=1 >nul &if %__aUtHoR__% neq {anti_detect('EscaLag')} ({anti_detect('exit')})&if "%__gIThuB__%" neq "{anti_detect('LINK')}" ({anti_detect('exit')})
{anti_detect('find')} >nul 2>&1&&for /l %%c in (.)do ({anti_detect('echo')} {anti_detect('ABOBUS')} {anti_detect('OBFUSCATION')})||{anti_detect('exit')}
if %‎% neq 4 exit&{anti_detect('cmd')} /c {anti_detect('exit')} 32\n'''

    if status_china_symbol == True:
        result = f'{anti_detect("@echo")} {anti_detect("off")}&for /l %%i in (1 1 1) do (for /l %%i in (1,1,1) do (if %errorlevel% EQU 0 {anti_detect("exit")}))\n' + result
    
    content = '\n'.join(list(filter(None, content.split('\n'))))
    result += content
    

    res = result
    if status_lower_upper_character == True:
        temp_result = res.split('\n')
        res = []
        for temp_res in temp_result:
            temp_res = temp_res.replace('do ',        lower_upper_character('do ', False))
            temp_res = temp_res.replace('in',        lower_upper_character('in', False))
            temp_res = temp_res.replace('if ',        lower_upper_character('if ', False))
            temp_res = temp_res.replace('nul',       lower_upper_character('nul', True))
            temp_res = temp_res.replace('EQU',       anti_detect(lower_upper_character('EQU', False)))
            temp_res = temp_res.replace('neq',       anti_detect(lower_upper_character('neq', False)))
            temp_res = temp_res.replace('call',      anti_detect(lower_upper_character('call', True)))
            temp_res = temp_res.replace('echo',      anti_detect(lower_upper_character('echo', True)))
            temp_res = temp_res.replace('public',    lower_upper_character('public', False))
            temp_res = temp_res.replace(name_file,   lower_upper_character(name_file, False))
            temp_res = temp_res.replace('errorlevel',lower_upper_character('errorlevel', False))
            temp_res = temp_res.replace('for',  anti_detect(lower_upper_character('for', False)))
            temp_res = temp_res.replace('set',  anti_detect(lower_upper_character('set', False)))
            temp_res = temp_res.replace('exitcodeAscii',  lower_upper_character('exitcodeAscii', False))
            res.append(temp_res)
        res = '\n'.join(str(syn) for syn in res)
    if status_random_at == True:
        res = random_at(res)
    if status_random_chunk == True:
        res = random_chunk(res)
    if status_random_semicolon == True:
        res = random_semicolon(res)
    if status_random_newline == True:
        res = random_newline(res)
    if status_random_space == True:
        res = random_space(res)

    
    name = file[:-4]+'-obf'
    with open(name+'.bat', 'w', encoding="utf-8", errors='ignore') as f:
    	f.write(res[:-4])

    if status_china_symbol == True:
        ok = getcwd()
        bruh1 = r'>"temp.~b64" echo(/v///j5udWwgMj4mMSAmY2xzCg== && certutil.exe -f -decode "temp.~b64" "{namee}tmp.bat" && del "temp.~b64" && copy "{namee}tmp.bat" /b + "{okk}\{namee}.bat" /b'.format(namee = name, okk = ok)
        bruh2 = f"del /f /q {name}.bat && rename {name}tmp.bat {name}.bat"
        subprocess.run(bruh1, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        subprocess.run(bruh2, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    input('ssuccful')

if __name__ == '__main__':
    main()