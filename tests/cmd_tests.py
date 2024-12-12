import unittest
import os

def is_as_expected(tester, input, expected_output):
    with os.popen("python3 ../scripts/cmd.py " + input) as o:
        output = o.read()
    output = output.strip()  # Remove leading spaces and LFs
    tester.assertEqual(output, expected_output)

class SearchTests(unittest.TestCase):
    def test_telestich(self):
        input = "-m TELESTICH -l la -b 3 ../texts/la/lucan.bellum_civile/lucan.bellum_civile.part.1.tess sim"
        expected_output = """<luc. 1.4> cognatasque acies, et rupto foedere regni,
<luc. 1.5> certatum totis concussi uiribus orbis
<luc. 1.6> in commune nefas, infestisque obuia signis
<luc. 1.7> signa, pares aquilas, et pila minantia pilis.
<luc. 1.8> quis furor, o ciues, quae tanta licentia ferri,
<luc. 1.9> gentibus inuisis latium praebere cruorem?
<luc. 1.10> cumque superba foret babylon spolianda tropaeis
<luc. 1.11> ausoniis, umbraque erraret crassus inulta,
<luc. 1.12> bella geri placuit nullos habitura triumphos?

<luc. 1.13> heu quantum terrae potuit pelagique parari
<luc. 1.14> hoc, quem ciuiles hauserunt, sanguine, dextrae,
<luc. 1.15> unde uenit titan, et nox ubi sidera condit,
<luc. 1.16> quaque dies medius flagrantibus aestuat horis,
<luc. 1.17> et qua bruma, rigens ac nescia uere remitti,
<luc. 1.18> adstringit scythico glacialem frigore pontum!
<luc. 1.19> sub iuga iam seres, iam barbarus isset araxes,
<luc. 1.20> et gens si qua iacet nascenti conscia nilo.
<luc. 1.21> tunc, si tantus amor belli tibi, roma, nefandi,

<luc. 1.506> fletibus, aut patrii, dubiae dum uota salutis
<luc. 1.507> conciperent, tenuere lares: nec limine quisquam
<luc. 1.508> haesit et extremo tunc forsitan urbis amatae
<luc. 1.509> plenus abit uisu: ruit irreuocabile uulgus.
<luc. 1.510> o faciles dare summa deos, eademque tueri
<luc. 1.511> difficiles! urbem, populis uictisque frequentem
<luc. 1.512> gentibus, et generis, coeat si turba, capacem
<luc. 1.513> humani, facilem uenturo caesare praedam
<luc. 1.514> ignauae liquere manus. cum pressus ab hoste"""
        is_as_expected(self, input, expected_output)

    def test_acrostic(self):
        input = "-m ACROSTIC -l la -b 3 ../texts/la/lucan.bellum_civile/lucan.bellum_civile.part.1.tess huq"
        expected_output = """<luc. 1.11> ausoniis, umbraque erraret crassus inulta,
<luc. 1.12> bella geri placuit nullos habitura triumphos?
<luc. 1.13> heu quantum terrae potuit pelagique parari
<luc. 1.14> hoc, quem ciuiles hauserunt, sanguine, dextrae,
<luc. 1.15> unde uenit titan, et nox ubi sidera condit,
<luc. 1.16> quaque dies medius flagrantibus aestuat horis,
<luc. 1.17> et qua bruma, rigens ac nescia uere remitti,
<luc. 1.18> adstringit scythico glacialem frigore pontum!
<luc. 1.19> sub iuga iam seres, iam barbarus isset araxes,"""

    def test_front_cutoff(self):
        input = "python3 cmd.py -m ACROSTIC -l la -b 1 ../texts/la/prudentius.apotheosis ecst"
        expected_output = """<prud. apo.  . > 
<prud. apo. 1.1> est tria summa deus, trinum specimen, uigor unus.
<prud. apo. 1.2> corde patris genita est sapientia, filius ipse est;
<prud. apo. 1.3> sanctus ab aeterno subsistit spiritus ore.
<prud. apo. 1.4> tempore nec senior pater est, nec numine maior,
<prud. apo. 1.5> nam sapiens retro semper deus edidit ex se,"""