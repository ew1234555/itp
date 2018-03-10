from cx_Freeze import setup, Executable

setup(
    name = "sum",
    version = "1.0",
    description = "Freelance Parser",
    executables = [Executable("sum.py")], requires=['cx_Freeze']
)