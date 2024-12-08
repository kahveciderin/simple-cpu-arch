import sys
import os.path


def parse_line(line):
    command = line.split()
    match command[0]:
        case "LDI":
            immediate = int_to_bin(command[1])
            reg = get_reg_bin(command[2])
            return f"0{reg}{immediate}0001"
        case "JIOZ":
            reg = get_reg_bin(command[1])
            addr = int_to_bin(command[2])
            return f"0{reg}{addr}0011"
        case "JROZ":
            reg = get_reg_bin(command[1])
            reg_l = get_reg_bin(command[2])
            reg_r = get_reg_bin(command[3])
            return f"0{reg}00{reg_r}{reg_l}1001"
        case "STO":
            reg = get_reg_bin(command[1])
            reg_l = get_reg_bin(command[2]) 
            reg_r = get_reg_bin(command[3])
            return f"0{reg}00{reg_r}{reg_l}0101"
        case "LPCU":
            reg = get_reg_bin(command[1])
            return f"1{reg}000000001101"
        case "LPCL":
            reg = get_reg_bin(command[1])
            return f"0{reg}000000001101"
        case "LOR":
            reg = get_reg_bin(command[1])
            reg_l = get_reg_bin(command[2])
            reg_r = get_reg_bin(command[3])
            return f"0{reg}00{reg_r}{reg_l}1011"
        case "LOD":
            reg = get_reg_bin(command[1])
            reg_l = get_reg_bin(command[2])
            reg_r = get_reg_bin(command[3])
            return f"0{reg}00{reg_r}{reg_l}0111"
        case "ADD":
            reg_l = get_reg_bin(command[1])
            reg_r = get_reg_bin(command[2])
            reg_out = get_reg_bin(command[3])
            return f"0{reg_out}00{reg_r}{reg_l}0000"
        case "SUB":
            reg_l = get_reg_bin(command[1])
            reg_r = get_reg_bin(command[2])
            reg_out = get_reg_bin(command[3])
            return f"0{reg_out}00{reg_r}{reg_l}0010"
        case "NOT":
            regIn = get_reg_bin(command[1])
            reg_out = get_reg_bin(command[2])
            return f"0{reg_out}00000{regIn}0100"
        case "AND":
            reg_l = get_reg_bin(command[1])
            reg_r = get_reg_bin(command[2])
            reg_out = get_reg_bin(command[3])
            return f"0{reg_out}00{reg_r}{reg_l}0110"
        case "OR":
            reg_l = get_reg_bin(command[1])
            reg_r = get_reg_bin(command[2])
            reg_out = get_reg_bin(command[3])
            return f"0{reg_out}00{reg_r}{reg_l}1000"
        case "XOR":
            reg_l = get_reg_bin(command[1])
            reg_r = get_reg_bin(command[2])
            reg_out = get_reg_bin(command[3])
            return f"0{reg_out}00{reg_r}{reg_l}1010"
        case "SHL":
            reg_l = get_reg_bin(command[1])
            reg_r = get_reg_bin(command[2])
            reg_out = get_reg_bin(command[3])
            return f"0{reg_out}00{reg_r}{reg_l}1100"
        case "SHR":
            reg_l = get_reg_bin(command[1])
            reg_r = get_reg_bin(command[2])
            reg_out = get_reg_bin(command[3])
            return f"0{reg_out}00{reg_r}{reg_l}1110"
        case "NOP":
            return "0000000000001000" # OR r0 r0 r0
        case ".byte":
            return f"{int_to_bin(command[1])}00000000"
        case ".word":
            return f"{int_to_bin(command[1], 16)}"
        case _:
            return ""


def get_reg_bin(reg):
    match reg:
        case "r0":
            return "000"
        case "r1":
            return "001"
        case "r2":
            return "010"
        case "r3":
            return "011"
        case "r4":
            return "100"
        case "r5":
            return "101"
        case "r6":
            return "110"
        case "r7":
            return "111"
        case _:
            print(f"Error on line {linenum} - invalid register!")
            exit()


def int_to_bin(num, lim=8):
    try:
        int(num, base=0)
    except ValueError:
        print(f"Error on line {linenum} - invalid integer!")
        exit()
    num = int(num, base=0)
    if num < 0:
        num = pow(2, lim) + num
    while num > (pow(2, lim) - 1):
        num = num - pow(2, lim)
    return str(bin(num)[2:].zfill(lim))


data = ""
linenum = 0
if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1], "r") as f:
        for line in f:
            if line.startswith(";"):
                continue
            if line == "":
                continue
            if line.isspace():
                continue
            linenum = linenum + 1
            data = data + parse_line(line) + "\n"
    data_split = data.split("\n")
    for i, line in enumerate(data_split):
        if line == "":
            continue

        line_upper = line[:8]
        line_lower = line[8:]
        line_upper = hex(int(line_upper, 2))[2:].zfill(2)
        line_lower = hex(int(line_lower, 2))[2:].zfill(2)

        print(f"{"" if i == 0 else ","}{line_lower},{line_upper}", end="")
