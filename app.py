from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WebmasterProIT</title>

<style>
*{
margin:0;
padding:0;
box-sizing:border-box;
scroll-behavior:smooth;
}

body{
font-family:Segoe UI,sans-serif;
background:#0f172a;
color:white;
overflow-x:hidden;
}

nav{
position:fixed;
top:0;
width:100%;
background:rgba(0,0,0,.8);
backdrop-filter:blur(10px);
padding:20px;
z-index:1000;
}

nav .container{
display:flex;
justify-content:space-between;
align-items:center;
max-width:1200px;
margin:auto;
}

.logo{
font-size:28px;
font-weight:bold;
color:#60a5fa;
}

nav ul{
display:flex;
list-style:none;
gap:25px;
}

nav a{
color:white;
text-decoration:none;
}

.hero{
height:100vh;
display:flex;
align-items:center;
justify-content:center;
text-align:center;
padding:20px;
background:linear-gradient(135deg,#2563eb,#7c3aed,#ec4899);
background-size:400% 400%;
animation:bg 10s infinite;
}

@keyframes bg{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.hero h1{
font-size:80px;
margin-bottom:20px;
}

.hero p{
font-size:24px;
max-width:900px;
margin:auto;
margin-bottom:30px;
}

.btn{
display:inline-block;
padding:18px 35px;
background:white;
color:#2563eb;
text-decoration:none;
border-radius:15px;
font-weight:bold;
transition:.3s;
}

.btn:hover{
transform:scale(1.1);
}

section{
padding:120px 20px;
}

.container{
max-width:1200px;
margin:auto;
}

h2{
font-size:50px;
text-align:center;
margin-bottom:60px;
}

.cards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
gap:25px;
}

.card{
background:#1e293b;
padding:30px;
border-radius:20px;
transition:.4s;
}

.card:hover{
transform:translateY(-10px);
box-shadow:0 0 30px rgba(96,165,250,.4);
}

.card h3{
margin-bottom:15px;
font-size:28px;
}

.stats{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:25px;
text-align:center;
}

.stat{
background:#1e293b;
padding:40px;
border-radius:20px;
}

.stat h3{
font-size:60px;
color:#60a5fa;
}

.pricing{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
gap:30px;
}

.price{
background:#1e293b;
padding:40px;
border-radius:20px;
text-align:center;
}

.price h3{
font-size:35px;
}

.price .money{
font-size:60px;
margin:20px 0;
color:#60a5fa;
}

.price p{
margin:10px 0;
}

.testimonial{
background:#1e293b;
padding:30px;
border-radius:20px;
}

form{
max-width:700px;
margin:auto;
}

input,textarea{
width:100%;
padding:18px;
margin:12px 0;
border:none;
border-radius:12px;
}

button{
width:100%;
padding:18px;
background:#2563eb;
border:none;
border-radius:12px;
color:white;
font-size:20px;
cursor:pointer;
}

footer{
background:#020617;
padding:60px 20px;
text-align:center;
}

footer h3{
font-size:30px;
margin-bottom:20px;
}

.about{
font-size:22px;
line-height:1.8;
text-align:center;
max-width:1000px;
margin:auto;
}

@media(max-width:768px){
.hero h1{
font-size:45px;
}
.hero p{
font-size:18px;
}
nav ul{
display:none;
}
}
</style>
</head>
<body>

<nav>
<div class="container">
<div class="logo">WebmasterProIT</div>

<ul>
<li><a href="#services">Услуги</a></li>
<li><a href="#about">О нас</a></li>
<li><a href="#portfolio">Портфолио</a></li>
<li><a href="#pricing">Цены</a></li>
<li><a href="#contact">Контакты</a></li>
</ul>
</div>
</nav>

<section class="hero">
<div>
<h1>WebmasterProIT</h1>
<p>
Создаем мощные сайты для бизнеса, магазинов и компаний.
Современный дизайн, высокая скорость и максимальная конверсия.
</p>

<a href="#contact" class="btn">Заказать сайт</a>
</div>
</section>

<section id="services">
<div class="container">

<h2>Наши услуги</h2>

<div class="cards">

<div class="card">
<h3>Лендинг</h3>
<p>Продающие страницы для рекламы и бизнеса.</p>
</div>

<div class="card">
<h3>Корпоративный сайт</h3>
<p>Полноценное представление компании в интернете.</p>
</div>

<div class="card">
<h3>Интернет-магазин</h3>
<p>Онлайн продажи с корзиной и оплатой.</p>
</div>

<div class="card">
<h3>SEO</h3>
<p>Продвижение сайта в поисковых системах.</p>
</div>

<div class="card">
<h3>Поддержка</h3>
<p>Обновления и сопровождение проектов.</p>
</div>

<div class="card">
<h3>Редизайн</h3>
<p>Обновление старых сайтов до современного уровня.</p>
</div>

</div>
</div>
</section>

<section id="about">
<div class="container">

<h2>О компании</h2>

<p class="about">
WebmasterProIT — современная веб-студия по разработке сайтов.
Мы создаем быстрые, красивые и эффективные проекты,
которые помогают бизнесу привлекать клиентов и увеличивать прибыль.
Наша цель — делать сайты мирового уровня по доступной цене.
</p>

</div>
</section>

<section>
<div class="container">

<h2>Статистика</h2>

<div class="stats">

<div class="stat">
<h3>150+</h3>
<p>Созданных сайтов</p>
</div>

<div class="stat">
<h3>98%</h3>
<p>Довольных клиентов</p>
</div>

<div class="stat">
<h3>24/7</h3>
<p>Поддержка</p>
</div>

<div class="stat">
<h3>5★</h3>
<p>Средняя оценка</p>
</div>

</div>

</div>
</section>

<section id="portfolio">
<div class="container">

<h2>Портфолио</h2>

<div class="cards">

<div class="card">
<h3>Строительная компания</h3>
<p>Корпоративный сайт под ключ.</p>
</div>

<div class="card">
<h3>Магазин одежды</h3>
<p>Интернет-магазин с каталогом товаров.</p>
</div>

<div class="card">
<h3>Юридические услуги</h3>
<p>Лендинг для привлечения клиентов.</p>
</div>

<div class="card">
<h3>Кафе и рестораны</h3>
<p>Сайт с онлайн бронированием.</p>
</div>

<div class="card">
<h3>Автосервис</h3>
<p>Продвижение услуг ремонта авто.</p>
</div>

<div class="card">
<h3>IT компания</h3>
<p>Премиальный корпоративный сайт.</p>
</div>

</div>

</div>
</section>

<section id="pricing">
<div class="container">

<h2>Тарифы</h2>

<div class="pricing">

<div class="price">
<h3>START</h3>
<div class="money">$100</div>
<p>Лендинг</p>
<p>Адаптивный дизайн</p>
<p>Форма заявки</p>
</div>

<div class="price">
<h3>BUSINESS</h3>
<div class="money">$300</div>
<p>До 10 страниц</p>
<p>SEO настройка</p>
<p>Админ панель</p>
</div>

<div class="price">
<h3>PREMIUM</h3>
<div class="money">$700</div>
<p>Уникальный дизайн</p>
<p>Интернет-магазин</p>
<p>Поддержка</p>
</div>

</div>

</div>
</section>

<section>
<div class="container">

<h2>Отзывы</h2>

<div class="cards">

<div class="testimonial">
⭐⭐⭐⭐⭐<br><br>
Сайт сделали быстро и качественно.
</div>

<div class="testimonial">
⭐⭐⭐⭐⭐<br><br>
Очень понравился дизайн и поддержка.
</div>

<div class="testimonial">
⭐⭐⭐⭐⭐<br><br>
После запуска сайта стало больше клиентов.
</div>

</div>

</div>
</section>

<section id="contact">
<div class="container">

<h2>Связаться с нами</h2>

<form>
<input type="text" placeholder="Ваше имя">
<input type="email" placeholder="Email">
<textarea rows="6" placeholder="Опишите проект"></textarea>
<button>Отправить заявку</button>
</form>

</div>
</section>

<footer>
<h3>WebmasterProIT</h3>
<p>Создаем сайты нового поколения</p>
<br>
<p>© 2026 WebmasterProIT. Все права защищены.</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)