from qiskit.circuit.library import ZZFeatureMap

def create_feature_map(n_qubits, depth=2):
    feature_map = ZZFeatureMap(feature_dimension=n_qubits, reps=depth, entanglement='linear')
    return feature_map

if __name__ == "__main__":
    n_qubits = 2
    feature_map = create_feature_map(n_qubits)
    print(feature_map)