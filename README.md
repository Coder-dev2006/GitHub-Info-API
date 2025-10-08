#  GitHub Info API
GitHub foydalanuvchi ma’lumotlarini olish uchun yozilgan oddiy REST API.
API Flask yordamida yaratilgan va GitHub’ning ochiq API’sidan ma’lumotlarni oladi.
U foydalanuvchi nomi, bio, repositorylar soni, kuzatuvchilar (followers) va boshqa ma’lumotlarni JSON formatda qaytaradi.

#  Xususiyatlar
GitHub foydalanuvchi ma’lumotlarini JSON formatda chiqaradi
Flask va Requests kutubxonalari asosida ishlaydi
Oddiy, tez va portfolio uchun mos loyiha
Har qanday GitHub username bilan ishlaydi

#  O‘rnatish
Repozitoriyani klonla:
git clone https://github.com/Coder-dev2006/github-info-api.git
cd github-info-api

# Zarur kutubxonalarni o‘rnat:
pip install flask requests

# Dastur faylini ishga tushir:
python github_api.py

#  Foydalanish
Brauzerda yoki Postman’da och:
http://127.0.0.1:5000/profile

# Namuna chiqishi:
{
  "username": "Coder-dev2006",
  "name": "Fayziyev Samandar",
  "bio": "Python developer | Backend, data analysis, automation & bots",
  "public_repos": 10,
  "followers": 5,
  "following": 2,
  "github_url": "https://github.com/Coder-dev2006"
}

#  Foydalanilgantexnologiyalar
 Python 3
 Flask
 Requests
 GitHub API

#  Muallif
Fayziyev Samandar
 GitHub: Coder-dev2006
#  Litsenziya
Ushbu loyiha MIT litsenziyasi ostida tarqatiladi.
Erkin o‘zgartirib, foydalanishingiz mumkin.
