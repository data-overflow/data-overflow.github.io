AOS.init(); var navigation = document.getElementById('navigation'); $('a').addClass('hover-underline-animation')
$(document).ready(function () { $('#nav-icon').click(function () { $(this).toggleClass('open'); }); }); $('#nav-icon').click(function () { navigation.classList.toggle('hide'); })
$('#navigation ul li a').click(function () { navigation.classList.toggle('hide'); $('#nav-icon').toggleClass('open'); })
$('#profile-pic').click(function () {
    var pp = document.getElementById("profile-pic").firstElementChild; if (pp.src.match("me2")) { pp.src = "./assets/me.jpg"; }
    else { pp.src = "./assets/me2.jpg"; }
})
document.querySelectorAll('a[href^="#"]').forEach(anchor => { anchor.addEventListener('click', function (e) { e.preventDefault(); document.querySelector(this.getAttribute('href')).scrollIntoView({ behavior: 'smooth' }); }); }); window.addEventListener("scroll", function () { document.getElementById("home").style.backgroundPositionY = (10 + this.scrollY * 0.2).toString() + "%"; document.getElementById("bg-layer-1").style.backgroundPositionY = (this.scrollY * 0.07 - 20).toString() + "%"; document.getElementById("bg-layer-2").style.backgroundPositionY = (this.scrollY * 0.066).toString() + "%"; document.getElementById("bg-layer-3").style.backgroundPositionY = (this.scrollY * 0.033).toString() + "%"; }); var TxtType = function (el, toRotate, period) { this.toRotate = toRotate; this.el = el; this.loopNum = 0; this.period = parseInt(period, 10) || 2000; this.txt = ''; this.tick(); this.isDeleting = false; }; TxtType.prototype.tick = function () {
    var i = this.loopNum % this.toRotate.length; var fullTxt = this.toRotate[i]; if (this.isDeleting) { this.txt = fullTxt.substring(0, this.txt.length - 1); } else { this.txt = fullTxt.substring(0, this.txt.length + 1); }
    this.el.innerHTML = '<span class="wrap">' + this.txt + '</span>'; var that = this; var delta = 180 - Math.random() * 100; if (this.isDeleting) { delta /= 2; }
    if (!this.isDeleting && this.txt === fullTxt) { delta = this.period; this.isDeleting = true; } else if (this.isDeleting && this.txt === '') { this.isDeleting = false; this.loopNum++; delta = 500; }
    setTimeout(function () { that.tick(); }, delta);
}; window.onload = function () {
    var elements = document.getElementsByClassName('typewrite'); for (var i = 0; i < elements.length; i++) { var toRotate = elements[i].getAttribute('data-type'); var period = elements[i].getAttribute('data-period'); if (toRotate) { new TxtType(elements[i], JSON.parse(toRotate), period); } }
    var css = document.createElement("style"); css.innerHTML = ".typewrite > .wrap { border-right: 0.08em solid #fff}"; document.body.appendChild(css);
};