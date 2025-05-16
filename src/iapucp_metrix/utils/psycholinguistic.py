from importlib.resources import files

import pandas as pd


class PsycholinguisticBank:
    """
    Dataset of psycholinguistic ratings, contains concreteness, imageability, familiarity, valence and arousal.
    """

    def __init__(self):
        models_dir = files("iapucp_metrix.models")
        espal_path = str(models_dir / "espal.csv")
        stadthagen_path = str(models_dir / "stadthagen.csv")

        self.espal_df = pd.read_csv(espal_path)
        self.stadthagen_df = pd.read_csv(stadthagen_path)

    def get_ratings(self, word: str) -> dict:
        ratings = {}
        espal_ratings = self.espal_df[self.espal_df["word"] == word.lower()]
        stadthagen_ratings = self.stadthagen_df[
            self.stadthagen_df["word"] == word.lower()
        ]

        if len(espal_ratings) != 0:
            ratings["concreteness"] = espal_ratings["concreteness"].values[0]
            ratings["imageability"] = espal_ratings["imageability"].values[0]
            ratings["familiarity"] = espal_ratings["familiarity"].values[0]
        if len(stadthagen_ratings) != 0:
            ratings["valence"] = stadthagen_ratings["valence"].values[0]
            ratings["arousal"] = stadthagen_ratings["arousal"].values[0]

        return ratings


PSY_BANK = PsycholinguisticBank()
