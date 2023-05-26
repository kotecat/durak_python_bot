from enum import StrEnum, Enum


class Suits(StrEnum):
    DIAMOND: str = 'd'
    HEART: str = 'h'
    CLUB: str = 'c'
    SPADE: str = 's'


class SuitsIcons(StrEnum):
    DIAMOND: str = '♦'
    HEART: str = '♥'
    CLUB: str = '♣'
    SPADE: str = '♠'


class Values(StrEnum):
    SIX: str = '6'
    SEVEN: str = '7'
    EIGHT: str = '8'
    NINE: str = '9'
    TEN: str = '10'
    JACK: str = '11'
    QUEEN: str = '12'
    KING: str = '13'
    ACE: str = '14'


CARDS = {
    'normal': {

        '6_d': 'CAACAgIAAxkBAAEFh7pi9NRDcCPWuNKz0LC62J3TM7CGaAACSBkAAt0vkEtZKUcC8YvNVSkE',
        '6_h': 'CAACAgIAAxkBAAEFh7xi9NRHW5QWW57ahVFiia7U-tOqnAACcBoAAqKXkUt8KSkj0_TcSykE',
        '6_s': 'CAACAgIAAxkBAAEFh75i9NRJJtbQmNA46WT9efYpx9WKfQACaBkAAuB4kEsoq-mHBF0cfSkE',
        '6_c': 'CAACAgIAAxkBAAEFh8Bi9NRL8eKBGbuLnuRj9kIewx3GWwACXxgAApeHkEuEkh4VZ5D5pikE',
        '7_d': 'CAACAgIAAxkBAAEFh8Ji9NRNgs8WRsSbDcFuHGJ8UwGzlgACSxgAAjzkkEv2H2yZwOS8AykE',
        '7_h': 'CAACAgIAAxkBAAEFh8Ri9NRQmtQnIy4HakP4cRP2fJHggQACCh0AAkNPkUuMgbeJB8QtZSkE',
        '7_s': 'CAACAgIAAxkBAAEFh8Zi9NRTD2NXQMSaYbRJAjI_o8aj6AACmBgAAiLMkEvwRmGs89uMOSkE',
        '7_c': 'CAACAgIAAxkBAAEFh8hi9NRVnIQuQes1l4geYqAjKREe4QACNhoAAmtPkUuuNTy8bF5WZCkE',
        '8_d': 'CAACAgIAAxkBAAEFh8pi9NRXYxOnsPzHKY7rfNy2yytojgACWxwAAtovkUsEOsBe7iUVXCkE',
        '8_h': 'CAACAgIAAxkBAAEFh8xi9NRZAb3p64pBznUu8qtISdWAMAACzSAAAuD5kUv9OsRGCFvQXikE',
        '8_s': 'CAACAgIAAxkBAAEFh85i9NRkzD1BvDdyN2IqHrvz2KoTjwACyRkAAgI6kEs72AABgCogPvUpBA',
        '8_c': 'CAACAgIAAxkBAAEFh9Bi9NRlRYri3wLrGY6nLVkxsZjkiwACyxoAAldqkEsGrSeAQsVfYykE',
        '9_d': 'CAACAgIAAxkBAAEFh9Ji9NRxXp7h-eTAKmW0n3pk4pLybAAC5yEAAu46iEt0QBfZ06dupCkE',
        '9_h': 'CAACAgIAAxkBAAEFh9Ri9NRzvV-v7EjaJkpxBgjEra5slwACOiIAAmlPkUsnkziUUNYCTikE',
        '9_s': 'CAACAgIAAxkBAAEFh9Zi9NR1IFjx5FYCCtJ4cfi6_4R1BAACbRsAAjHQkEs9IRzo6zXMqCkE',
        '9_c': 'CAACAgIAAxkBAAEFh9hi9NR3ILP-djwy4wxEWDYbkZLfDwACZRcAAnIqkEuYPLo-fWuPpykE',
        '10_d': 'CAACAgIAAxkBAAEFh9pi9NR5Xc8a1jNfOrkjgdojTaZrAgAC7RkAAvYAAZFLEYujs-H8G08pBA',
        '10_h': 'CAACAgIAAxkBAAEFh9xi9NR7sWfTqcR1jHPWz8DhkXMsuQACvh4AAoqNkEvnmxW-psn3_ykE',
        '10_s': 'CAACAgIAAxkBAAEFh95i9NR9cOvtelPJKQ37gFE344Zb7AACAhgAAjFykEvucI5Uu8VhzSkE',
        '10_c': 'CAACAgIAAxkBAAEFh-Bi9NR_Ds_DTr8oB-j6V5yDbNxQYQAC8RcAAlt2kEsLB4_RxNZiMikE',
        '11_d': 'CAACAgIAAxkBAAEFh-Ji9NSDE3jOqxRzFwu4wRBObglVzAACZxoAAi-EkUvjmNzPHKjH4CkE',
        '11_h': 'CAACAgIAAxkBAAEFh-Ri9NSFmo85aj4HMA4rL1ENHWt8AAOoGgACBH2QS5DbEHeHZLAIKQQ',
        '11_s': 'CAACAgIAAxkBAAEFh-Zi9NSHVGIeCykQAgiIAddokQpW6AAC2iAAAvT0iUtqPKvCcotw3CkE',
        '11_c': 'CAACAgIAAxkBAAEFh-hi9NSJdct60d2A-wFohiRonVKjTQAChhgAAjeKkUsby2DUt33nvSkE',
        '12_d': 'CAACAgIAAxkBAAEFh-pi9NSMCA31-y00YWRtV37vQdBDwgACgBsAApizkEsP4CIvJSM4cCkE', 
        '12_h': 'CAACAgIAAxkBAAEFh-xi9NSOXvGYH7d4cnKVb8fbQai0jAACnBsAAs29kEvMP-sUeyPZbykE',
        '12_s': 'CAACAgIAAxkBAAEFh-5i9NSTA-UX5ypZGR6UyNZB0E7iNAAC4hkAAjtzkUv9hpsiVHyb8SkE',
        '12_c': 'CAACAgIAAxkBAAEFh_Bi9NSVZUpepjEPIQrZ3i-tEQ0IQQACyR4AAu0TkEs9V5X9ry0qQikE', 
        '13_d': 'CAACAgIAAxkBAAEFh_Ji9NSXRw0OoTIo6ezcIVuJqwXu7wACIRsAArMfkEt4klix5KChvCkE',
        '13_h': 'CAACAgIAAxkBAAEFh_Ri9NSZlqda8h32SJmmoA4VXDtWEQACoBgAAvm-kEs4O5tG-Q50NCkE',
        '13_s': 'CAACAgIAAxkBAAEFh_Zi9NSbngcScNQ6zbGhRgMcTTM5NwACAx4AAm7NkEsoKCMCEsqsDCkE',
        '13_c': 'CAACAgIAAxkBAAEFh_hi9NSeI0ptiFKhsDOQR2o0osEI9gAC5xkAAuQykUt5rU9Clop_mikE',
        '14_d': 'CAACAgIAAxkBAAEFh_pi9NSg3OB1jNmRgfYgfn0ShAeaTgACgBoAAsSPkEtz9vECRU66zCkE',
        '14_h': 'CAACAgIAAxkBAAEFh_xi9NSiSsQ0ZTXz6-asdk8AARVYNGkAAigYAAIzlZBLevH71o2Nx0cpBA',
        '14_s': 'CAACAgIAAxkBAAEFh_5i9NSkDOX7RFJxwnizpMJvNYXd1gACjhgAAvwykEs52kgirkO4wykE',
        '14_c': 'CAACAgIAAxkBAAEFiAABYvTUpqmeBSmSNsK4xhmFOD6FEsIAAlkbAAKZL5FLjJUz9nwr8VgpBA'
        
    },

    'grey': {

        '6_d': 'CAACAgIAAxkBAAEFiBBi9NqHcNNkKYjk1m0bdTuaq7lh5QAC_hoAAqa_qEuszrnsgJ1boikE',
        '6_h': 'CAACAgIAAxkBAAEFiBJi9NqOV3me6eWqlcIZ612yyu_LmgAChhoAAlyNqUuFywSFO6F3AikE',
        '6_s': 'CAACAgIAAxkBAAEFiBRi9Nqbz4jRnzvC5K6h0V8KZQeEUQACSR4AAsxEoEup7qQAAa0OH2EpBA',
        '6_c': 'CAACAgIAAxkBAAEFiBZi9NqeS0d2JvUq2_bUQ3G3L9wbXwACGxsAAsByoUuFecCUB49gDikE',
        '7_d': 'CAACAgIAAxkBAAEFiBhi9NqgzxIMNn1VurwQslR93Qbi3QACGB0AArBmoEsumubNOfkXcikE',
        '7_h': 'CAACAgIAAxkBAAEFiBpi9Nqj87NAtp0u-vpSHi9Dt8xocgACMxwAAvX-oUt0DrvCmdci0CkE',
        '7_s': 'CAACAgIAAxkBAAEFiBxi9NqlQx9Gg688zPNwLGsesx078wACqBYAArNPqEvwChIobOI7LSkE',
        '7_c': 'CAACAgIAAxkBAAEFiB5i9NqoDEWBj3voEOZ-dZxlBiTuVAAC6BcAAoLKqUuyA9iqiW9FIykE',
        '8_d': 'CAACAgIAAxkBAAEFiCBi9NqqjmA2HfGohRTphLmNMsQi-wACmxwAAj8JoUsFAT-QY-lhMykE',
        '8_h': 'CAACAgIAAxkBAAEFiCJi9Nqs5nlh7TBI7TqYQFZGpWmrfwAC-BoAAi2UoUt2GT2aOhBgzCkE',
        '8_s': 'CAACAgIAAxkBAAEFiCRi9Nqu4L7ajMZI_11PeniNNgABLgYAAgocAAKQ2aBLzjKWvpW1tzIpBA',
        '8_c': 'CAACAgIAAxkBAAEFiCZi9NqwNv75F-_elb37lP9wE9TRUAACZhYAArChqUvFaQnOdzwC-ikE',
        '9_d': 'CAACAgIAAxkBAAEFiChi9NqzWIAhllUzHV7HrXIVLUDkOwACbhcAAvlUqUufaj5KoflaoCkE',
        '9_h': 'CAACAgIAAxkBAAEFiCpi9Nq1lc_8ypetGa2nPnW3_MPpIgACMhsAAjdWoEtg6QdEEaYEjykE',
        '9_s': 'CAACAgIAAxkBAAEFiCxi9Nq5LTimmMqXQWG9RAtJVp5cRAACtyUAAgdVoEvl47XiKlIv2CkE',
        '9_c': 'CAACAgIAAxkBAAEFiC5i9Nq7b9fm8UIcBycLeGNYg2FCxAACZR8AAnoMqUu1uKL7XNxCpykE',
        '10_d': 'CAACAgIAAxkBAAEFiDBi9Nq9wsWAdBzQN3ZZEO9-7q8DsAACQR8AApudoEvimmKkdpFMPSkE',
        '10_h': 'CAACAgIAAxkBAAEFiDJi9Nq_yWJNn_Xnits55eNnrkPFzAAClBwAAlYOqUtLzcsn9Iv5tCkE',
        '10_s': 'CAACAgIAAxkBAAEFiDRi9NrBuK6EOvnR8r5DZrGJigU89gAC2hgAAsivqUvdizxDyNcV8CkE',
        '10_c': 'CAACAgIAAxkBAAEFiDZi9NrDxYxEkJqr6d1b3cu4CtGk7gAC2RsAAomaqUui8aHk6WAcTCkE',
        '11_d': 'CAACAgIAAxkBAAEFiDhi9NrGmE5gp4SHa14JkhLRVop04wACqhoAAjpVqUtUl2PLUDc2_ikE', 
        '11_h': 'CAACAgIAAxkBAAEFiDpi9NrItPquEFtY9e2UmnxiYqaHHAAC4h0AAq3qoEsnQuzWiSOSeikE',
        '11_s': 'CAACAgIAAxkBAAEFiDxi9NrKqk6AIH8ZsN65_buBprgGNgAClxoAAihWqEtayEvqarSRJykE',
        '11_c': 'CAACAgIAAxkBAAEFiD5i9NrNYPwDk24pP4Fx5uEPlFEybwACLhsAAsy-qUu2qc2O-IJL1ikE', 
        '12_d': 'CAACAgIAAxkBAAEFiEBi9NrPxBaP55_uDEH60eIwPnhaKwACPRkAAhEbqUuy3dWFgAQIsCkE',
        '12_h': 'CAACAgIAAxkBAAEFiEJi9NrRKRNDFxc-z_Xb8Ok77K85UwACeh8AAui1oEuaFM-qZJLJkCkE',
        '12_s': 'CAACAgIAAxkBAAEFiERi9NrTbqBUU3wFBFyN6HZUoDdp8wACjh4AAphyoEs0OfWEkdepzykE',
        '12_c': 'CAACAgIAAxkBAAEFiEZi9NrVYOhSuQg6a9yiq4zXsBiKdAACDRsAAj01qEvzhVIWy6sSnikE',
        '13_d': 'CAACAgIAAxkBAAEFiEhi9NrXq6nW6d-NQhdTm4cIrm8HFQACzR0AAhGUqEsohirrsm2GsSkE',
        '13_h': 'CAACAgIAAxkBAAEFiEpi9NrZd7nxmWcMLEfCpogO4PTBnAACAh0AAvhFqEsdbv-fsyOrFSkE',
        '13_s': 'CAACAgIAAxkBAAEFiExi9Nrb2VO9FkavmddISLkiOKLH1wACUhcAAhkwqEvpCx2aDHfqoCkE',
        '13_c': 'CAACAgIAAxkBAAEFiE5i9Nrd295bAAGZqTWQhEyZw_EFDBsAAlcXAAKn86lLz-N6vYXmf24pBA',
        '14_d': 'CAACAgIAAxkBAAEFiFBi9NrgOi4FotPfQu9dHR5de0DtqAACLR0AAuxVqUsILKHXwlmk5ikE',
        '14_h': 'CAACAgIAAxkBAAEFiFJi9NrjZXrcWyAxzkaI4A0dlCj6KwACexwAAqDKoUsc4FrTwDAyVCkE',
        '14_s': 'CAACAgIAAxkBAAEFiFRi9NrljbtxXnHLknbfzxAUVhDgQAACSxoAAqpYqEvo2zarsoYCcSkE',
        '14_c': 'CAACAgIAAxkBAAEFiFZi9NrnI4pVhl4qFSY6bo4MiqoK-wACLSEAAi0aqEu_Lb3QRikxoCkE'
        
    }  
}


DECK = {
    '24': 'CAACAgIAAxkBAAEFiGZi9N7ml8OK63WgrpmMHTRgGig5_QACajEAAurFqUvJj2venJlh-ykE',
    '23': 'CAACAgIAAxkBAAEFiGhi9N7o92kNdMXkhb2UfweSEGlbXwACdhoAAjgEqUtL9be3AAFMnG8pBA',
    '22': 'CAACAgIAAxkBAAEFiGpi9N7sooqZzKtCZW89_Sv_aKV-5QAC7BgAAi9XqUtZt-xqgqKIJykE',
    '21': 'CAACAgIAAxkBAAEFiGxi9N7yUll7W7ZmTgpooIkCIUL1fAACjhwAAgoFoUs1flPjxcdFnykE',
    '20': 'CAACAgIAAxkBAAEFiG5i9N70gKs1K9kWn-QHAhY8662FaAACgiEAAm8pqEsEMqtOrCBGfykE',
    '19': 'CAACAgIAAxkBAAEFiHBi9N73eDqFJvn5OOXSVfy6UJiTrwACuRwAAobcqEsR6nxQkLIIzSkE',
    '18': 'CAACAgIAAxkBAAEFiHJi9N76c_u64pxf5eaGlb9fkr1WBgAC4yAAAojvoUu2abq95MiYwSkE',
    '17': 'CAACAgIAAxkBAAEFiHRi9N77ow6i_0sZoHBM0ObjLVCQtAACKhoAApbGqUshQpVhJK8zXCkE',
    '16': 'CAACAgIAAxkBAAEFiHZi9N7-Mw0Jy8WJhMFIX1RBGZFN5QACxxkAAq-QqEuNUGFC3PkrHCkE',
    '15': 'CAACAgIAAxkBAAEFiHhi9N8AATKFDzMiVcMjf_XzuZfpqi4AAtkdAAJ1F6FLTqgSwiJAEgIpBA',
    '14': 'CAACAgIAAxkBAAEFiHpi9N8P-kCdlohIccffAkZh1bCgmgAC8xoAAvZPqUthA7mOz0a2eikE',
    '13': 'CAACAgIAAxkBAAEFiHxi9N8RnWrBV0zj9kKCNj0P3qaOVwACcxwAAgv-oEu-N3v6rXvnkSkE',
    '12': 'CAACAgIAAxkBAAEFiH5i9N8VqDKMFhYJXfuaXOJgEboNwwACPRoAAt_CqEsUZjTKvkygaykE',
    '11': 'CAACAgIAAxkBAAEFiIBi9N8adBXRIEPJNcdbiRlxvEwgZgACKyAAAjkVoEuqnZg977o_hCkE',
    '10': 'CAACAgIAAxkBAAEFiIJi9N8d54Lgw6Vo2p9q9BjqV_9MzwACpxgAArDUqEspPQWzJNBpfSkE',
    '9': 'CAACAgIAAxkBAAEFiIRi9N8eqh2_Le9O6muNrZFaXCBb1wACFhwAAhVkqUvqmhH7Y0ldMykE',
    '8': 'CAACAgIAAxkBAAEFiIZi9N8h-zxgl-3snGe7VuMn2MZ_GwACPhsAAhAaoUt_B5QuBqQXrykE',
    '7': 'CAACAgIAAxkBAAEFiIhi9N8jXSfVin1IjP05aoks0PL7kAACthgAAjqNqUuVGexlQC53oSkE',
    '6': 'CAACAgIAAxkBAAEFiIpi9N8lU1OU-1pLUcsvSYHLSzV89gACux0AAm2dqEs6JkjsXDcYNikE',
    '5': 'CAACAgIAAxkBAAEFiIxi9N8ojcOMVjjzQpUYEZ6SA9xeGgACFhwAAny7qEs8fWmbYcuIOykE',
    '4': 'CAACAgIAAxkBAAEFiI5i9N8qyEvAuwPivPPeeySTD2xhQwACxSQAAi5ToUs8oWopzG9drSkE',
    '3': 'CAACAgIAAxkBAAEFiJBi9N8tcMFseyK4lswN-2zWnR0s6wACLxsAAiKvqUubqRWLS5k_cSkE',
    '2': 'CAACAgIAAxkBAAEFiJJi9N8vRPRbcpVSssdeMaMylKGvZAACgB8AAumuoEsHvMBNK8vmDykE',
    '1': 'CAACAgIAAxkBAAEFiJRi9N8yv7HbZ-1qGyWPRvw2BIRdHgACaRwAAoG2qEtzwGDgXspCrCkE',
    '0': 'CAACAgIAAxkBAAEFiJZi9N80NlE-7XBC8xgcL3pAWM1wGgACahsAAoAvqUsv_wNGhQ7GKCkE'
}

SUIT = {
    'd': 'CAACAgIAAxkBAAEFiFhi9N6WsmoVGiVCARK0PaEPy1hxIwACEh4AAnTOqEtb-7pItmYVoSkE',
    'h': 'CAACAgIAAxkBAAEFiFpi9N6Zq1VuvqptUTttNQv3aAre9gACSxoAAgnnqEvn34S0p9V4fSkE',
    's': 'CAACAgIAAxkBAAEFiFxi9N6bYVzGDq8wbRH75_4ZblK7sAACchkAAiZkqEuIdmKBktgSYikE',
    'c': 'CAACAgIAAxkBAAEFiF5i9N6ePrpgsVNpA7xD904tUTCjWQACyhoAAlehqUvmgY-dQGLnSikE'
}

SPECIAL = {
    'draw': 'CAACAgIAAxkBAAEFiGBi9N6gipaKIexU7cVWyxcci2juyAACSx0AArAMqEt3c1jfI8dsHikE',
    'info': 'CAACAgIAAxkBAAEFiGJi9N6jciaNRdy38VMYNHz4D0YK5AACZBsAAmDwqEu-hHLMRVEnoCkE',
    'pass': 'CAACAgQAAxkBAAEFk5pi-zwMMpsz63hBqxPNa1-5DcaeEwACzgIAAl9XmQAB3nO8ol7EhmMpBA'
}


STICKERS = {
    **CARDS,
    **DECK,
    **SUIT,
    **SPECIAL
}


class Card:
    """ This is Card :> """

    def __init__(self, value: Values, suit: Suits) -> None:
        self.value: Values = value
        self.suit: Suits = suit

    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return f"{self.value}_{self.suit}"
    
    def __eq__(self, other) -> bool:
        return repr(self) == repr(other)
    
    def __lt__(self, other) -> bool:
        return repr(self) > repr(other)
    

def from_str(string: str):
    value, suit = string.split('_')
    return Card(value, suit)