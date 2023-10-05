import dis
import marshal
with open('hidden_4.pyc', 'rb') as f:
    code = marshal.load(f)
names = []
for instruction in code['co_code']:
    if instruction.opname == 'STORE_NAME' and not instruction.argval.startswith('__'):
        names.append(instruction.argval)
names.sort()
for name in names:
    print(name)
