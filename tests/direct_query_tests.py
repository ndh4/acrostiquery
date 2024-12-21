import unittest
import os

def is_as_expected(tester, input, expected_output):
    with os.popen("python3 ../scripts/main.py " + input) as o:
        output = o.read()
    output = output.strip()  # Remove leading spaces and LFs
    tester.assertEqual(output, expected_output)

class SearchTests(unittest.TestCase):
    def test_telestich(self):
        self.maxDiff = None
        input = '\'{"mode": "TELESTICH", "lang": "la", "term": "sim", "buflen": 3, "search_space": "lucan.bellum_civile.part.1.tess"}\''
        expected_output = """Searching...\n\n<luc. 1.4> cognatasque acies, et rupto foedere regni,
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
<luc. 1.514> ignauae liquere manus. cum pressus ab hoste

End of results for """ + input
        is_as_expected(self, input, expected_output)

    def test_acrostic(self):
        input = '\'{"mode": "ACROSTIC", "lang": "la", "term": "huq", "buflen": 3, "search_space": "lucan.bellum_civile.part.1.tess"}\''
        expected_output = """Searching...\n\n<luc. 1.11> ausoniis, umbraque erraret crassus inulta,
<luc. 1.12> bella geri placuit nullos habitura triumphos?
<luc. 1.13> heu quantum terrae potuit pelagique parari
<luc. 1.14> hoc, quem ciuiles hauserunt, sanguine, dextrae,
<luc. 1.15> unde uenit titan, et nox ubi sidera condit,
<luc. 1.16> quaque dies medius flagrantibus aestuat horis,
<luc. 1.17> et qua bruma, rigens ac nescia uere remitti,
<luc. 1.18> adstringit scythico glacialem frigore pontum!
<luc. 1.19> sub iuga iam seres, iam barbarus isset araxes,

End of results for """ + input
        is_as_expected(self, input, expected_output)

    def test_front_cutoff(self):
        input = '\'{"mode": "ACROSTIC", "lang": "la", "term": "ecst", "buflen": 1, "search_space": "prudentius.apotheosis"}\''
        expected_output = """Searching...\n\n<prud. apo.  . > 
<prud. apo. 1.1> est tria summa deus, trinum specimen, uigor unus.
<prud. apo. 1.2> corde patris genita est sapientia, filius ipse est;
<prud. apo. 1.3> sanctus ab aeterno subsistit spiritus ore.
<prud. apo. 1.4> tempore nec senior pater est, nec numine maior,
<prud. apo. 1.5> nam sapiens retro semper deus edidit ex se,

End of results for """ + input
        is_as_expected(self, input, expected_output)

    def test_capital_v(self):
        input = '\'{"mode": "ACROSTIC", "lang": "la", "term": "haecu", "buflen": 0, "search_space": "lucan"}\''
        expected_output = """Searching...\n\n<luc. 6.719> haec ubi fata caput spumantiaque ora leuauit,
<luc. 6.720> adspicit adstantem proiecti corporis umbram,
<luc. 6.721> exanimes artus inuisaque claustra timentem
<luc. 6.722> carceris antiqui. pauet ire in pectus apertum
<luc. 6.723> uisceraque, et ruptas letali uolnere fibras.

End of results for """ + input
        is_as_expected(self, input, expected_output)

    def test_capital_j(self):
        input = '\'{"mode": "ACROSTIC", "lang": "la", "term": "ieih", "buflen": 0, "search_space": "ambrose"}\''
        expected_output = """Searching...\n\n<ambrose. epistolae_variae. 51.8> iterum cum plebem numerari iussisset dauid, percussus est corde, et dixit ad dominum: peccaui uehementer, quod fecerim hoc uerbum, et nunc, domine, aufer iniquitatem serui tui, quod deliqui uehementer. et missus est iterum ad eum nathan propheta, qui ei trium optionem conditionum offerret, ut quam uellet, eligeret: famem tribus annis in terra, aut tribus mensibus fugere a facie inimicorum suorum, aut triduo mortem in terra. et respondit dauid: angustiae sunt tria haec uehementer; uerumtamen incidam in manu domini; quoniam multae misericordiae eius nimis: et in manus hominis non incidam. culpa autem erat, quoniam uoluit scire numerum totius plebis, quae secum erat: quod scire deo soli debuit reseruare.
<ambrose. epistolae_variae. 51.9> et cum, inquit, mors fieret in plebe, ipso primo die ad horam prandii cum uidisset dauid percutientem angelum in plebem, ait dauid: ego peccaui, et ego pastor malignum feci, et hic grex quid fecit? fiat manus tua in me, et in domum patris mei. itaque poenituit dominum, et iussit angelo ut parceret plebi, sacrificium autem offerret dauid; erant enim tunc sacrificia pro delictis, haec nunc sunt sacrificia poenitentiae. itaque ea humilitate acceptior deo factus est: non enim mirandum peccare hominem: sed illud reprehensibile, si non se cognoscat errasse, non humiliet deo.
<ambrose. epistolae_variae. 51.10> iob sanctus et ipse potens in saeculo, ait: peccatum meum non abscondi, sed coram plebe omni annuntiaui. ipsi immani regi saul dixit ionathas filius suus: noli peccare in seruum tuum dauid : et: ut quid peccas in sanguinem innocentem occidere dauid sine causa ? quia etsi rex erat, peccabat tamen, si occideret innocentem. denique etiam dauid cum iam regno potiretur, et audisset abner innocentem occisum a ioab duce militiae suae, ait: innocens sum ego et regnum meum amodo et usque in aeternum a sanguine abner filii ner ; et ieiunauit in dolore.
<ambrose. epistolae_variae. 51.11> haec ideo scripsi, non ut te confundam, sed ut regum exempla prouocent, ut tollas hoc peccatum de regno tuo: tolles autem humiliando deo animam tuam. homo es, et tibi uenit tentatio, uince eam. peccatum non tollitur nisi lacrymis et poenitentia. nec angelus potest, nec archangelus; dominus ipse, qui solus potest dicere: ego uobiscum sum ; si peccauerimus, nisi poenitentiam deferentibus non relaxat.

End of results for """ + input
        is_as_expected(self, input, expected_output)

    def test_capital_i(self):
        input = '\'{"mode": "ACROSTIC", "lang": "la", "term": "imeeeee", "buflen": 0, "search_space": "jerome"}\''
        expected_output = """Searching...\n\n<Vulgate Mark.8.1> in illis diebus iterum cum turba multa esset nec haberent quod manducarent conuocatis discipulis ait illis;
<Vulgate Mark.8.2> misereor super turba quia ecce iam triduo sustinent me nec habent quod manducent;
<Vulgate Mark.8.3> et si dimisero eos ieiunos in domum suam deficient in uia quidam enim ex eis de longe uenerunt;
<Vulgate Mark.8.4> et responderunt ei discipuli sui unde istos poterit quis hic saturare panibus in solitudine;
<Vulgate Mark.8.5> et interrogauit eos quot panes habetis qui dixerunt septem;
<Vulgate Mark.8.6> et praecepit turbae discumbere supra terram et accipiens septem panes gratias agens fregit et dabat discipulis suis ut adponerent et adposuerunt turbae;
<Vulgate Mark.8.7> et habebant pisciculos paucos et ipsos benedixit et iussit adponi;

<Vulgate Mark.15.46> ioseph autem mercatus sindonem et deponens eum inuoluit sindone et posuit eum in monumento quod erat excisum de petra et aduoluit lapidem ad ostium monumenti;
<Vulgate Mark.15.47> maria autem magdalene et maria ioseph aspiciebant ubi poneretur;
<Vulgate Mark.16.1> et cum transisset sabbatum maria magdalene et maria iacobi et salome emerunt aromata ut uenientes unguerent eum;
<Vulgate Mark.16.2> et ualde mane una sabbatorum ueniunt ad monumentum orto iam sole;
<Vulgate Mark.16.3> et dicebant ad inuicem quis reuoluet nobis lapidem ab ostio monumenti;
<Vulgate Mark.16.4> et respicientes uident reuolutum lapidem erat quippe magnus ualde;
<Vulgate Mark.16.5> et introeuntes in monumento uiderunt iuuenem sedentem in dextris coopertum stola candida et obstipuerunt;

End of results for """ + input
        is_as_expected(self, input, expected_output)

    def test_capital_u(self):
        input = '\'{"mode": "ACROSTIC", "lang": "la", "term": "uinas", "buflen": 0, "search_space": "juvencus.historia_evangelica"}\''
        expected_output = """Searching...\n\n<juvenc. hist. ev. 4.223> ut liceat miseris penetrare in limina laeta.
<juvenc. hist. ev. 4.224> illas non comitum sponsi cognoscere quisquam
<juvenc. hist. ev. 4.225> non ipse sponsus uoluit. uigilate timentes,
<juvenc. hist. ev. 4.226> aduentus uobis quia non est certior hora.
<juvenc. hist. ev. 4.227> sicut enim, longas cui contigit ire profecto

End of results for """ + input
        is_as_expected(self, input, expected_output)