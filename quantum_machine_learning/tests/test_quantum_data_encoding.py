import unittest
from quantum_data_encoding import encode_data
from qiskit import Aer, execute

class TestQuantumDataEncoding(unittest.TestCase):
    def test_encode_data(self):
        data = [0.1, 0.4, 0.7, 0.9]
        qc = encode_data(data)
        backend = Aer.get_backend('statevector_simulator')
        result = execute(qc, backend).result()
        statevector = result.get_statevector()
        
        # Assert that the statevector is not all zeros (indicating some rotation was applied)
        self.assertFalse(all(abs(amplitude) < 1e-6 for amplitude in statevector))
        
if __name__ == "__main__":
    unittest.main()
