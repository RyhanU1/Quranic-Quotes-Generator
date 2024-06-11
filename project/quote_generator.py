import random

class Quote:
    def __init__(self, quote, reference):
        self.quote = quote
        self.reference = reference
    def __str__(self):
        return f"{self.quote} - {self.reference}"   

q1 = Quote('"So remember Me; I will remember you. And be grateful to Me and do not deny Me."', 'Surah Baqarah Verse 152')
q2 = Quote('"Indeed we belong to Allah (SWT), and indeed to Him we will return."', 'Surah Baqarah Verse 156')
q3 = Quote('"Allah (SWT) does not charge a soul except [with that within] its capacity."', 'Surah Baqarah Verse 286')
q4 = Quote('"Indeed, Allah (SWT) is my Lord and your Lord, so worship Him. That is the straight path."', 'Surah Baqarah Verse 51')
q5 = Quote('"Your ally is none but Allah (SWT) and [therefore] His Messenger and those who have believed - those who establish prayer and give zakah, and they bow [in worship]."', 'Surah Baqarah Verse 55')
q6 = Quote('"Allah (SWT) would not punish them while they seek forgiveness."', 'Surah Anfal Verse 33')
q7 = Quote('"All authority belongs to Him. And to Him you will all be returned."', 'Surah Baqarah Verse 88')
q7 = Quote('"And all of them are coming to Him on the Day of Resurrection alone."', 'Surah Maryam Verse 95')
q8 = Quote('"it is not eyes that are blinded, but blinded are the hearts"', 'Surah Al Haj 46')
q9 = Quote('"So be patient. Indeed, the promise of Allah (SWT) is truth."', 'Surah Ar-Rum Verse 60')
q10 = Quote('"His command is only when He intends a thing that He says to it, "Be", and it is."', 'Surah Yaseen Verse 82')
q11 = Quote('"And every soul will be fully compensated [for] what it did; and He is most knowing of what they do."', 'Surah Az-Zumar Verse 70')
q12 = Quote('"Call upon Me; I will respond to you."', 'Surah Ghafir Verse 60')
q13 = Quote('"But none is granted it except those who are patient"', 'Surah Fussilat Verse 35')
q14 = Quote('"Whoever does a good deed - it is for himself; and whoever does evil - it is against the self. Then to your Lord you will be returned."', 'Surah Jathiya Verse 15')
q15 = Quote('"[This] worldly life is only amusement and diversion. And if you believe and fear Allah (SWT), He will give you your rewards and not ask you for your properties."', 'Surah Muhammad Verse 36')
q16 = Quote('"And everything they did is in written records. And every small and great [thing] is inscribed."', 'Surah Qamar Verse 52-53')
q17 = Quote('"He is with you wherever you are."', 'Surah Hadid Verse 4')
q18 = Quote('"And whoever relies upon Allah (SWT) - then He is sufficient for him."', 'Surah At-Talaq Verse 3')
q19 = Quote('"Indeed, the Qur’an is a reminder"', 'Surah Muddathir Verse 14-15')
q20 = Quote('"And He found you lost and guided [you]"', 'Surah Ad-Duhaa Verse 7')
q21 = Quote('"For indeed, with hardship [will be] ease"', 'Surah Sharh Verse 5')
q22 = Quote('"Does he not know that Allah (SWT) sees?"', 'Surah Al Alaq Verse 14')
q23 = Quote('"Then as for one whose scales are heavy [with good deeds], He will be in a pleasant life. But as for one whose scales are light, His refuge will be an abyss."', "Surah Qari'ah Verse 6-9")
q24 = Quote('"Allah (SWT), the Eternal Refuge."', 'Surah Al Ikhlas Verse 2')
q25 = Quote('"The Lord of mankind."', 'Surah An-Nas Verse 3')


def generate_quote():
    quotes = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
          q11, q12, q13, q14, q15, q16, q17, q18, q19,
          q20, q21, q22, q23, q24, q25]

    return random.choice(quotes)

print(generate_quote())