from src.codegenerator import codegenerator

print(codegenerator.code())

for i in range(0, 100):
    print(f"{i}.{codegenerator.code(20)}")
