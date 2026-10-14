from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n = 1

# Build an equal superposition circuit
qc = QuantumCircuit(n, n)
qc.h(range(n))                 # Hadamard on every qubit
qc.measure(range(n), range(n))

# Run on local simulator
sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()
print(counts)