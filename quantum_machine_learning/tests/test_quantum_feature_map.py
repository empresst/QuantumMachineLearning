import unittest
from quantum_feature_map import create_feature_map
from qiskit import Aer, execute

class TestQuantumFeatureMap(unittest.TestCase):
    def test_create_feature_map(self):
        n_qubits = 2
        feature_map = create_feature_map(n_qubits)
        qc = feature_map.bind_parameters([0.1, 0.2])
        backend = Aer.get_backend('statevector_simulator')
        result = execute(qc, backend).result()
        statevector = result.get_statevector()
        
        # Assert that the statevector is not all zeros (indicating some transformation was applied)
        self.assertFalse(all(abs(amplitude) < 1e-6 for amplitude in statevector))

if __name__ == "__main__":
    unittest.main()
