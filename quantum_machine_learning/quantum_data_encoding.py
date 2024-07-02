from qiskit import QuantumCircuit
import numpy as np

def encode_data(data):
    n_qubits = int(np.ceil(np.log2(len(data))))
    qc = QuantumCircuit(n_qubits)

    for i, value in enumerate(data):
        binary_string = format(i, '0{}b'.format(n_qubits))
        for qubit, bit in enumerate(binary_string):
            if bit == '1':
                qc.x(qubit)
        qc.ry(value, range(n_qubits))
        for qubit, bit in enumerate(binary_string):
            if bit == '1':
                qc.x(qubit)

    return qc

if __name__ == "__main__":
    data = [0.1, 0.4, 0.7, 0.9]
    qc = encode_data(data)
    print(qc)

