import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        s1 = "ab"
        s2 = "eidbaooo"
        target = True
        a = Solution()
        self.assertEqual(a.checkInclusion(s1,s2),target)
    
    def test_two(self):
        s1 = "ab"
        s2 = "eidboaoo"
        target = False
        a = Solution()
        self.assertEqual(a.checkInclusion(s1,s2),target)

    def test_3(self):
        s1 = "adc"
        s2 = "dcda"
        target = True
        a = Solution()
        self.assertEqual(a.checkInclusion(s1,s2),target)

    def test_4(self):
        s1 = "voujinkwlkydjrmbehskvlulpwmdczrzefahwvyakbzjvawxzhqztqswqghubeqhzyuyufiwxqxtyefgxteihyprxbwdykssxadcybtcverkzifjlheqwnpfeckywhusbmqktjhjjsodaqzdsghhaysoilhlqfbgobbwztiouplfeborkkqpqrrcizyazsttjjyaonwsqcbmmafafsvqofypdxcxsjqufxpxokkqftvneezbpidaqdwiprzztzlhdnyxjzpfplrwksetmdjsoskolwammzedrgwbttgjiznopuuwbqqwlyhrpzrapujnyufljiuwjaanikjsfaohejygudydnlaiczmokjqzkxxdsaexxlddypwgfopyruqvfvawqhxvwwmkiekvkkmojunjzxwiqkigohuwtlqhotzrbhpbvxpczmsqjlhmwbfyzlhlpjeawcxkracgjqmcdmtbzvssvgnuhwroxgoihlgbaxmmakzxxsyvscycylsbaaemmsrifqfcssdhzguueblxomruathvmybhgenytgddikaaogkwssdibperbodtlerrnkrdqicgnzwfxaoeqmfovjfetzrvpcsgpeeytxpbtefkwjgmuydmebhxwafemwlncgkwayljyatmmanmpfakwdnmvjqppuknagllcoyixpykxmvykfrfrwmiitxwvzwgiikzwhyhekgsyqivdizzpemotanlmtofjlcilwntqwwumgamtwszhfwcicqeqbxlpaotqfrgbehfcooooreeztiznxevlnkhqhtoeabvuzaxyslvtvelysgashucyvocysscbacshieepypttkkgbyebsrlbyrbsdadnunzzkwbyzspxucoblwmkmtnsatssazxwivfzwifiecrwofdbcaazxdofglusktgrjivedhokzdvdhtreingnglymhujlxrakfesmtemxildrpxazibxxndxctkpvupwisazhbkitwmbejzhzvafhtaisvjjvzyivmdghrmduheifbvwwjypbcxflesxswzybfaauzklcmjfzvcwulzemnaozqvprubrdzotggqkbwfjbsiyacsqyrnqdthyhemowcbxdapfuoohskvnyjehjzvyrzgkjeenfxurfalblwaklfevbgeiniihdcgaskpaqkxakrxwtklffhfvgoetfxuvpjtstdhcuithgsgdtqwuqbwjdjxctttmfrhkliyaylsdvwzyrtwenotyfourzhkqidkzmoqfbpwnodcyjnsbksbqymnvuvudsqwfnykavdpnyszbwofjxdjfhihztefusfvjcrgmoehigqsqhhkfcaumjgxzjhinydrbgapdrnzxcljdjzlwfliwhbcvoajviehzpdvxvigvaxtlctrtsctcaizxghlukazxjahjpmhwbcdcqdmvdadsluekbwwhzxrqwopdcecvpryeljmwzjotlapnunnpslbkehezwztlcauadepikdljsunxisiajtiqtdazgtizxmnilfrvhmyojdddxzsuzfychpysdsicakzctydwuwfkehxnfijhnwvwxaundogctgqcuuqpbetoqhwvgrqslrlvtlqvzuqmllvcpuikqrqfivfcfjvfohzfmvkyqbcahaarcyacidsfdobrbgclxkuijwdaaxpdtjbzudxegdijfecmmobkqeioogpthtdpvuzjqciiyfikvgzbpozxpksgnfgmrfqqcufjuangtaayzrqnhhgcxrjgroqltxwzammhoxfcykalbsutmwptspfcriqbhsxhjjhqyayquztgpsjvxbctfzskvqnsaiprqqtfzlelkgthqfpbwyjxiddryedqejhjrmzadkzdcpcekvuyyvhwqgadsgrdvukdypufnotfutbnnvfntzqgglgbfxtbhzczzfhcyvfidpcpchysdbzoeodexitmbuksjbyffpxgvpwfpqkeccxpjweokjpxvtsutezxyqpbsxekeacpxqbuhjcbrmprgisuuxoxehopkhmaqojxvodzblpiegmjtrhbijhvrogimhdfzoxpnofyujwqqzarheceiiirmuflxhcfjxqmadisviqjfzkmccnydksegmnwfdxxbngudcwthnbhockycjnzolwpxfkljmffqjoljsqcorbciunavkgfubnjamqspijnoabmyjlrtkefaiceufpffvwnygcxwrthyqerjedqyvpwtezyrvojztrxcxqqywebiqxcmnzuavbnpdyigtsyeojvubqhvetoocfifxqqczmnhmbxcxoxfdmjopbalqrivjkcayonnolylghzkajbxnxzwmnfsszryatbdhlhmoobxkxrwiwuezhujdpvqhohuevcmmjufkbzqriivpxvgvvjyvaipoewijpptjgpzsetuywcnfljssallxikayhjrjyedrlyboracgykaooieezeeubbrzsvuovdprsjifpihmuwwrgjhufsdwwbhhrloolxencdaiwhwrmsaqyamuwmicdzoisnydtfnzwrwpbpwbxzmmtxtxufolxchlealeslcyiweakaoysvijfzmninpmbzeazbjvdyojoyalopdmpdstsymgksuacwsppdmnkiluwoqylyedzzsyhgpxfwyaldfabbstonesihlypcouswkfcywnrggzzkamrtedxyzivuystgiuospvywhqqezjcbnhwzvsoqsbcvccsdhakxcbffrimyiuobwszvccwcdmzknqkicshubettbrvutlhhheuqyjblhvrbabwresreuuzwaeqgaflvcbjmzbenfoekgigcgxawvgnhofkoibvapouamuywgxhivfcchfqiecpltnnebwhgenmnujcrotnrzzrntsrceqaubpcqggoqkzvqnyigbwotnxgehpvcioyevbfqbqodkjsxrkoseytzhhzdymdftgsssibzroetdvhlxsfvqnqwhtyeldmjqdpctdzxkgqkcfmsxanilktehbwcwtaixi"
        s2 = "oqupbcqazvlehlzjyamwlmpybilihvokonzhgqiyomtdxcfcjrvyvzbftvxhcntsavnfumzzozxwpzllomceexaxmablfcluylwwgxzzcrfbusucsdaqlfztvxbwyaygucnowcvvwukhghyzbbwmgvdtcqdvwgulezccmcdmkkftwzodzpnmxxkgmlclgitebyjmferxpnerphcvpvrypnyhvnazizzrmqlpjgkoucmyqdzbwpewgduarfrulybyrokbztghpxojkxespppqpqgnnxacqtzebeogoswbwitciuvqdrlpohhfsgsjhbtgxlegvkovpzdjabojfojubbuabdagjppdtuaevynopbeawkyfevuutdczkxwkkvuiabnkgnscyquirognkzkeeelfmjyljljiozzswkkcxqsajbitjscsnrdzpiuaatkvbfhufaowbdmtydklapdbwlxvxfmoagutecttrbdogxhlrzxbtqqnyzludvwenlrbqehfjkgkcbtnknxcpexgyrkjvfdygoyfzjlceirvhlqrxjgrqxwezwhgnhkrisazhwhzhqdywuorxgmnhbippzuvbarblpbnwznvwnwhmxotwxeadpdcpjelkxopwmizuqctxhoxxrdyaxbvzhrcdtsaaxzehxroqupdigxzdrpbkztvxpnjbnscxvcqxkgfaocyhjqkyxwyogbeoekjepufascoyohlbebqypwvfgvwynfwcpoazzowvbvawvrxovsebibgcuiegpclatcxfiydvpxbolcmwlmwsvryaicjdirggfqykoezcrvzcgcnppdswmxjizjxgvxsitnwbhpfhpvcnliaofdfpwiwylrlaawqljqzpgymhhoygtieqnmujcacvxgzawjvofxsohkmoahshwmgwdarcgbginnrtfekniliwkqxbobcwusprjgasjbppiofeexhgiuxcbhysqpmacufvzjcpbxpdldbvtwpszpwaabqbrhwuczdluybcaelvuhurjwoblkoclsnqpjosgivwiynczedalhpksdibfvuhzcolormvxsbeokfvsbogoubdtzrupvehtdqmewxddjmlnsikxfxudmjqcqhsxlfcxqmgzafpszejwunccnrqmlnuumlxemmrvluioeaqspsvfrbyjjcmlvchjhcvyqzoeqobjeinxdzzwiyinmirkzqndcpmmjpejujfgtcftmccsoarfxvjtdczpvfbgluqvpynqtqmsfpngqeyiimseuldmnjnnwtpuwyggdlybuvpoxfyayhovxzhtlbmsldorjckmywsmigdocgbpbysjrpnxpzafxvbzciasldrtbjsiygspavhalsdvecanlmcmihcmyebtciayyvugavrpcvnjernmaqxusslswgrqauuerjbswsppvsbyffltivkoqkacscyryboknnhbstpmffhvnbznevcmolwvsusmowvybevlyksceaokcnymmgfmmetsacabcsinnqltrxsdnqfseaziyvbecfbacwqimrdgrdwpxrsusmwnervyedswloinjzxfphuvtkvujknlizsxgqoiotniuflvufiftskingufhgvqewvjqbhpyuhgzidoloeibxzwagkpffzotyprkmzajvuahrevwuanmzrqiaoedmdiaghxuslncxunbudftxwipuzihldhcjndwtzqirbwjpqqpckxaweteotuoqtxjsrfzdbwriihvbtnlbtttlnvivfyhetdlvrkqvjqscclmaifqqrgkcegwpzffhfywfaireqazvtkqinfnkzzdhdxdjjnpzyqowacsjhmfrnowekxhnoesupsnatiivxtjphzdonrbvbyrlljyjwyjqkndvskaffacxzcwyfgnpgbrxyqpnwjwvixnjvjykagehbsyxwjvvtlhhxjtqejinhiuejjvnbomyolslaacwcnasyavbcvpiqjldhqenlsmesoauvwekeooaqtlfgtyfgettakefpeknxwmgpxpkkmksfdvrgofgnwgsgadnjwmaltbguxgkajsukrujbrgzpdqxgehheqgniwxvlzdpnmvffxtoiznttsspvrufkkpfhlyenaotplkkfwvojtjnyzitnhnebwthecknkpeevctgtxbbbmmrxdzyeuatgctejpnuljsuoosqhdtpmcbhpmzzbdvhphvurbvurfjbtcoxenxprlodvqgyyooougpnyqqcsauflkbzyatregubqyeemntuilwfbcozptqwszgaueuomxhhrotdqeelblnbmwmhfdbqvtalgfwcxlruqjuxjepurpqkwuxnlajjrfnugtexgdiyxocfeqrmlrrfggbxywbrrmhrablneshhdpxpggkmzfnwdcrkrybzwxngplkvftxjgxfgiuuomvusihtndwmfxialvoujinkwlkydjrmbehskvlulppmdczrzefahwvyakbzjvawxzhqztqswqghubeqhzyuyufiwxmxtyefgxteihyprxbwdykssxadcybtcverkzifjlheqwnpfeckywhusbmqktjhjjsodaqzdsghhaysoilhlqfbgobbwztiouplfeborkkqpqrrcizyazsnmjjyaonwsqcbmmafafsvqofypdxcxsjqufxpxokkqftvneezbpidaqdwiprzztzlhdnyxjzpfplrwksetmdjsoskolwammzedrgwbttgjiznopuuwbqqwlyhrpzrapujnyufljiuwjaanikjsfaohejygudydnlaiczmokjqzkxxdsaexxlddypwgfopyauqvfvawqhxvwwmkiekvkkmojunjzxwiqkigohuwtlqhotzrbhpbvxpczmsqjlhmwbfyzlhlpjeawcxkracgjqmcdmtbzvssvgnuhwroxgoihlgbaxmmakzxxsyvscycylsbaaemmsrifqfcssdhzguueblxomruathvmybhgenytgddikaaogkwssdibperbodtberrnkrdqicgnzwfxaoaqmfovjfetzrvpcsgpeeytxpbtefkwjgmuydmebhxwafemwlncgkwayljaatmmanmpfekwdtmvjqppuknagllcoyixpykxmvykfrfrwmiitxwvzwgiikzwhyhekgsyqivdizzwemotanlmtofjlcilwntqwwumgamtwszhfwcicqeqbxlpaotqfrgbehfcooooteeztiznxevlnkhqhtoerbvuzaxyslvtvelysgashucyvocysscbacshieepypttkkgbyebsrlbyrbsdadnunzzkwbyzspxecoblwmkmtnsatssazxwivfzwifiucrwofdbcaazxdofglusktgrjivedhokzdvdhtreingnglymhujlxrakfesmtetxildrpxazibxxndxctkpvuzwisazhbkitwmbejzhzvafhtaisvjjvzyivmdghrmduheifbvwwjypbcxflesxswzybfayuzklcmjfzvcwuazemnaozqvprubrdzotggqkbwfjbsiyacsqyrnqdthyhemowcbxdapfuoohskvnyjehjzvyrzskjeenfxurfalblwaklfevbgeiniihdcgaskpaqkxakrxwtklffhfvgoetfxuvpjrstdhcuithgsgdtqwuqbwjdjxctttmfrhkliyaylsdowzyrtwenotyfourzhkqidkzmoqfbpwnodcyjnsbksbqymnvuvudsqwfnykavdpnyszbwofjxdjfhihztefusfvjcrgmoehigqsqhhkfcauqjgxzjhinydrbgapdrnzxcljdjzlwfliwhbcvosjviehzpdvxvigvaxtlctrtsctcaizxghlukazxjahjpmhwbcdcqdmvdadsluekbwwhzxrqwopdcecvpryeljmwzjotlapnunnpslbkehepwztlcauadepikdljsunxisiajtiqtdazgtizxmnilfrvhmyojdddxzsuzfychpysdsiczkzctydwuwfkehxnfijhnwvwxaundogctgqcuuqpbewoqhwvgrqslrlvtlqvzuqmllvcpuikqrqdivfcfjvfohzfmvkyqbcahaarcyacidsfdobrbgclxkuijwdaaxpdtjbzudxegdijfecmmobbqeioogpthtdpvuzjqciiyfikvgzbpozxpksgnfgmrfqqcufjulngtaayzrqnhhgcxrjgroqltxwzammhoxfcykalbsutmwptspfcriqbhsxhjjhqyayquztgpsjvxbctfzskvqnsaiprqqtfzlelkgthqfpbwyjxiddryedqejhjrmzadkzdcpcekvuyyvhwqgadsgmdvukdypufnotfutlnnvfntzqzglgbfxtbhzczzfhcyvfidpcpchzsdbzoeodexitmbuksjbyffpxgvptfpqkeccxpjweokjpxvtsutezxyqpbsxekeacpxqbuhjcbrmprgisuuxoxehopkhmaqojxvodzblpiegmjtrhbijhvrogimhdfzoxpnofyujwqqzarheceiiirmuflxhcfjxqmadisviqjfzkmccnydksegmnwfdxxbngudcwthnbhockycjnzolwpxfkljmffqjoljsqcorbciunavkgfubnjamqspijnoabmyjlrtkefaiceufpffvwnygcxwrthyqerjedqyvpwtezyrvvjztrxcxqqywebiqbcmnzuavbnpdyigtsyeojvubqhvetoocfifxqqczmnhmbxcxoxfdmjopxalqrivjkcayonnolylghzkajbxnxzwmnfsszryatbdhlhmoobxkxrwiwuezhujdpvqhohuevcmmjufkbzqriivpxvgvvjyvaipoewijpptjgpzsetuywcnfljssallxikayhjrjyedrlyboracgykaooieegeeubbrzsvuovdprsjifpihmuwwrgjhufsdwwbhhrloolxencdaiwhwrmsaqyamuwmicdzoignydtfnzwrwpbpwbxzmmtxtxufolxchlealeslcyiweakaoysvijfzmninpmbzeazbjvdyojoyalopdmpdstsymgksuacwsppdmnkiluwoqylyedzzsyhgpxfwyaldfabbstonesihlypcouswkfcywnrggzzkamrtedxyzivuystgiuospvywhqqezjcbnhwyvsoqsbcvccadhakxcbffrimyiuobwszvccwcdmzknqkicshubettbrvutlhhheuqyjblhvrbabwresreuuzwaeqgaflvcbjmzbenfoekgigcgxawvgnhofkoikvapouamuywgxhivfcchfqiecpltnnebwhgenrnujcrotnrzzrntsrceqaubpcqggoqkzvqnyigbwotnxgehpvcioyevbfqbqodkjsxrkoseytzhhzdymfftgsssibaroetdvhlxsfvqnqwhtyeldmjqdpctdzxkgqkcfmsxanilktehbwcwtaixiefnhewlzmfeefpldmeptjjshxebbwrbmhrmybddxovkszadbyeqvrxncffozgozdrro"
        target = True
        a = Solution()
        self.assertEqual(a.checkInclusion(s1,s2),target)


unittest.main()

#[-1,0,3,5,9,12]
#9