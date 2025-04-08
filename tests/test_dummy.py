from iapucp_metrix.analyzer import Analyzer


def test_dummy():
    texts = ["Este es un texto de prueba. Otra sentencia."]
    analyzer = Analyzer()

    docs = analyzer.analyze(texts)
    for doc in docs:
        print(doc._.coh_metrix_indices)
        assert doc._.coh_metrix_indices["DESPC"] == 1

