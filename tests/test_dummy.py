from iapucp_metrix.analyzer import Analyzer


def test_dummy():
    texts = [
        "El sol se escondió tras el horizonte, tiñendo el cielo de tonos naranjas y rosados. Una brisa suave movía las hojas, susurrando la promesa de una noche tranquila.\n\nEn la tranquila biblioteca, el polvo flotaba a través de los rayos de luz. Las filas de libros se erguían como centinelas silenciosos, cada uno guardando un mundo esperando ser explorado."
    ]
    analyzer = Analyzer()

    docs = analyzer.analyze(texts)
    for doc in docs:
        print(doc._.coh_metrix_indices)
        for verb in doc._.verbs:
            print("Verb", verb.text, verb._.tag, verb._.tag_)
        assert doc._.coh_metrix_indices["DESPC"] == 2
