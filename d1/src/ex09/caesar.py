import sys

def caesar(text, shift, mode):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            if mode == "encode":
                result.append(chr((ord(ch) - base + shift) % 26 + base))
            else:
                result.append(chr((ord(ch) - base - shift) % 26 + base))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            if mode == "encode":
                result.append(chr((ord(ch) - base + shift) % 26 + base))
            else:
                result.append(chr((ord(ch) - base - shift) % 26 + base))
        elif ch.isalpha():
            raise Exception("The script does not support your language yet.")
        else:
            result.append(ch)
    return "".join(result)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise Exception("Invalid number of arguments.")

    mode = sys.argv[1]
    if mode not in ("encode", "decode"):
        raise Exception("First argument must be 'encode' or 'decode'.")

    text = sys.argv[2]
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be an integer.")

    print(caesar(text, shift, mode))
