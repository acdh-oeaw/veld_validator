
print("module: validator")

def validate(veld=None):
    if veld is None:
        print("invalid")
    else:
        print(f"valid: {veld}")

if __name__ == "__main__":
    validate("from validator module")
