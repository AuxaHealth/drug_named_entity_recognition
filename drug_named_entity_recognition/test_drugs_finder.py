import unittest

from drug_named_entity_recognition.drugs_finder import find_drugs


class TestDrugsFinder(unittest.TestCase):
    def test_drugs_1(self):
        drugs = find_drugs("i bought some Sertraline".split(" "))

        self.assertEqual(1, len(drugs))
        self.assertEqual("Sertraline", drugs[0][0]["name"])

    def test_drugs_lowercase(self):
        drugs = find_drugs("i bought some sertraline".split(" "))

        self.assertEqual(0, len(drugs))

    def test_drugs_synonym(self):
        drugs = find_drugs("i bought some Zoloft".split(" "))

        self.assertEqual(1, len(drugs))
        self.assertEqual("Sertraline", drugs[0][0]["name"])

    def test_drugs_synonym_lc(self):
        drugs = find_drugs("i bought some zoloft".split(" "))

        self.assertEqual(0, len(drugs))

    def test_generic_lc(self):
        drugs = find_drugs("i bought some penicillin".split(" "))

        self.assertEqual(2, len(drugs))
        self.assertEqual("Phenoxymethylpenicillin", drugs[0][0]["name"])

    def test_two_word_drug(self):
        drugs = find_drugs("i bought some Amphotericin B".split(" "))

        self.assertEqual(1, len(drugs))
        self.assertEqual("Amphotericin B", drugs[0][0]["name"])

    def test_hemlibra(self):
        drugs = find_drugs("i bought some HEMLIBRA".split(" "))

        self.assertEqual(1, len(drugs))
        self.assertEqual("Emicizumab", drugs[0][0]["name"])

    # tests if the pipe in the Wikipedia works
    def test_adderall(self):
        drugs = find_drugs("i bought some Adderall".split(" "))

        self.assertEqual(1, len(drugs))
        self.assertEqual("Amphetamine", drugs[0][0]["name"])

    # tests the pipe in NHS
    def test_simvador(self):
        drugs = find_drugs("i bought some Simvador".split(" "))

        self.assertEqual(1, len(drugs))
        self.assertEqual("Simvastatin", drugs[0][0]["name"])

    # test medline plus
    def test_ofirmev(self):
        drugs = find_drugs("i bought some Ofirmev".split(" "))

        self.assertEqual(1, len(drugs))
        self.assertEqual("Acetaminophen", drugs[0][0]["name"])

    # test mesh
    def test_flovent(self):
        drugs = find_drugs("i bought some Flovent".split(" "))

        self.assertEqual(1, len(drugs))

        # should be returning "Flixotide"
        has_flixotide = False
        for synonym in drugs[0][0]["synonyms"]:
            if synonym == "Flixotide":
                has_flixotide = True
                break
        self.assertEqual(has_flixotide, True)
        return
