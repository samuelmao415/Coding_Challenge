paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
paragraph = "a, a, a, a, b,b,b,c, c"
paragraph = " a."
import re
import collections
paragraph = "j. t? T. z! R, v, F' x! L; l! W. M; S. y? r! n; O. q; I? h; w. t; y; X? y, p. k! k, h, J, r? w! U! V; j' u; R! z. s. T' k. P? M' I' j! y. P, T! e; X. w? M! Y, X; G; d, X? S' F, K? V, r' v, v, D, w, K! S? Q! N. n. V. v. t? t' x! u. j; m; n! F, V' Y! h; c! V, v, X' X' t? n; N' r; x. W' P? W; p' q, S' X, J; R. x; z; z! G, U; m. P; o. P! Y; I, I' l' J? h; Q; s? U, q, x. J, T! o. z, N, L; u, w! u, S. Y! V; S? y' E! O; p' X, w. p' M, h! R; t? K? Y' z? T? w; u. q' R, q, T. R? I. R! t, X, s? u; z. u, Y, n' U; m; p? g' P? y' v, o? K? R. Q? I! c, X, x. r' u! m' y. t. W; x! K? B. v; m, k; k' x; Z! U! p. U? Q, t, u' E' n? S' w. y; W, x? r. p! Y? q, Y. t, Z' V, S. q; W. Z, z? x! k, I. n; x? z; V? s! g, U; E' m! Z? y' x? V! t, F. Z? Y' S! z, Y' T? x? v? o! l; d; G' L. L, Z? q. w' r? U! E, H. C, Q! O? w! s? w' D. R, Y? u. w, N. Z? h. M? o, B, g, Z! t! l, W? z, o? z, q! O? u, N; o' o? V; S! z; q! q. o, t! q! w! Z? Z? w, F? O' N' U' p? r' J' L; S. M; g' V. i, P, v, v, f; W? L, y! i' z; L? w. v, s! P?"
banned = ["m","q","e","l","c","i","z","j","g","t","w","v","h","p","d","b","a","r","x","n"]
mostCommonWord(paragraph, banned)

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.replace('!',' ')
        paragraph = paragraph.replace('?',' ')
        paragraph = paragraph.replace(',',' ')
        paragraph = paragraph.replace(';',' ')
        paragraph = paragraph.replace('.',' ')
        paragraph = paragraph.replace('  ',' ')
        paragraph = paragraph.rstrip()
        paragraph = paragraph.lstrip()
        paragraph = paragraph.lower()



        paragraph_list = paragraph.split(' ')

        words_to_analyze = set(paragraph_list) - set(banned)
        paragraph_dict = dict.fromkeys(set(words_to_analyze) , 0)

        for w in paragraph_list:
            if paragraph_dict.get(w) != None:
                paragraph_dict[w] += 1

        sorted_dict = sorted(paragraph_dict.items(), key= lambda x:x[1])
        #print(sorted_dict)
        print(paragraph_list)
        output = sorted_dict[-1][0]

        return(output)
