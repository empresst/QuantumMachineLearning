from qiskit_aer import Aer, execute
from qiskit.circuit.library import RealAmplitudes, ZZFeatureMap
from qiskit_machine_learning.algorithms import VQC
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit.utils import QuantumInstance
from qiskit_machine_learning.datasets import ad_hoc_data, breast_cancer
from sklearn.metrics import accuracy_score
import numpy as np

def create_variational_classifier(feature_map, n_qubits):
    var_form = RealAmplitudes(n_qubits, reps=3)
    vqc = VQC(feature_map=feature_map, var_form=var_form)
    return vqc

def main():
    seed = 1376
    n_samples = 20
    feature_dim = 2

    # Experiment with different feature maps
    feature_maps = [
        ZZFeatureMap(feature_dimension=feature_dim, reps=2, entanglement='linear'),
        RealAmplitudes(feature_dim, reps=2),
    ]

    for feature_map in feature_maps:
        vqc = create_variational_classifier(feature_map, feature_dim)
        
        # Use ad_hoc_data and breast_cancer datasets
        datasets = [
            ("Ad Hoc Data", *ad_hoc_data(training_size=n_samples, test_size=n_samples, n=feature_dim, gap=0.3, one_hot=False)),
            ("Breast Cancer Data", *breast_cancer(training_size=n_samples, test_size=n_samples, n=feature_dim, plot_data=False, one_hot=False)),
        ]
        
        for name, training_data, training_labels, test_data, test_labels in datasets:
            backend = Aer.get_backend('qasm_simulator')
            quantum_instance = QuantumInstance(backend, shots=1024, seed_simulator=seed, seed_transpiler=seed)
            vqc.fit(training_data, training_labels, quantum_instance=quantum_instance)

            predictions = vqc.predict(test_data)
            accuracy = accuracy_score(test_labels, np.argmax(predictions, axis=1))
            print(f'Feature Map: {type(feature_map).__name__}, Dataset: {name}, Accuracy: {accuracy}')

if __name__ == "__main__":
    main()
