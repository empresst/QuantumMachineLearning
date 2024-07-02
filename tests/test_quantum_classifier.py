import unittest
from quantum_classifier import create_variational_classifier
from quantum_feature_map import create_feature_map
from qiskit_machine_learning.datasets import ad_hoc_data
from qiskit import Aer
from qiskit.utils import QuantumInstance
from sklearn.metrics import accuracy_score
import numpy as np

class TestQuantumClassifier(unittest.TestCase):
    def test_vqc(self):
        n_samples = 20
        feature_dim = 2

        feature_map = create_feature_map(feature_dim)
        vqc = create_variational_classifier(feature_map, feature_dim)

        training_data, training_labels, test_data, test_labels = ad_hoc_data(training_size=n_samples, test_size=n_samples, n=feature_dim, gap=0.3, one_hot=False)

        backend = Aer.get_backend('qasm_simulator')
        quantum_instance = QuantumInstance(backend, shots=1024)
        vqc.fit(training_data, training_labels, quantum_instance=quantum_instance)

        predictions = vqc.predict(test_data)
        accuracy = accuracy_score(test_labels, np.argmax(predictions, axis=1))
        
        # Assert that the accuracy is above a reasonable threshold (e.g., 50%)
        self.assertTrue(accuracy > 0.5)

if __name__ == "__main__":
    unittest.main()
