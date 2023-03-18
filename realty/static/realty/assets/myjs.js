//slider
let slideIndex = 1;
showSlides(slideIndex);
function nextSlide() {
showSlides(slideIndex += 1);
}
function previousSlide() {
showSlides(slideIndex -= 1);
}
function currentSlide(n) {
showSlides(slideIndex = n);
}
function showSlides(n) {
let i;
let slides = document.getElementsByClassName('item');
if (n > slides.length) {
slideIndex = 1;   
}
if (n < 1) {
slideIndex = slides.length;
}
for (let slide of slides ){
slide.style.display = 'none';
}
slides[slideIndex -1].style.display = 'block';
}
setInterval(function nextSlide() {
    showSlides(slideIndex += 1);
    },3000)
//header
//header
function myHeaderfix() {
    let scroll = window.scrollY;
    let scrollStart = 100;
    let myheader = document.querySelector('#myheader');
    let mybody = document.querySelector('body');
    const changeHeader = () =>  myheader.classList.add('fixhead');
    const changeBody = () => mybody.classList.add('mtbody');
    const removeHeader = () =>  myheader.classList.remove('fixhead');
    const removeBody = () => mybody.classList.remove('mtbody');

    window.addEventListener('scroll' , () =>{
        scroll = window.scrollY;
        if (scroll >= scrollStart) { changeHeader(), changeBody() }
        else{ removeHeader(), removeBody() }
    })
}
myHeaderfix();