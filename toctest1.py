
from AutomaPy import TuringMachine

tm = TuringMachine()

tm.addState('A', {'0': ('A', '0', 'R'), '1': ('B', '0', 'R'), '_': ('B', '_', 'L')}, initial_state=True, final_state=True)
tm.addState('B', {'0': ('B', '0', 'R'), '1': ('A', '0', 'R'), '_': ('A', '_', 'L')})

print(tm.turingMachineEvenOnes("")) # True (because 0 is even number)
print(tm.turingMachineEvenOnes("1")) # False
print(tm.turingMachineEvenOnes("1111")) # True
