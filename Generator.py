import random
import array

#maksimumşifre uzunluğu
MAX_LEN = 12

# şifre kombinasyonu için gerekli olan tüm karakterleri eklyoruz
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 
					'r', 's', 't', 'u', 'v',   'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 
					'R', 'S', 'T', 'U', 'V',  'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

# tüm  karakterleri birleştiriyoruz
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# karakterlerden rastgele seçimyapıyoruz
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

# random  seçilen karakterleri birleştiriyoruz
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol


#rastgele şifremizi oluşturmaya başlıyoruz
for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(COMBINED_LIST)
#geçici   şifreyi array haline dönüştürüyoruz
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)

#array halindeki şifreyi  normal haline dönderiyoruz
password = ""
for x in temp_pass_list:
		password = password + x
		
# şifreyi görüntülüyoruz
print(password)
