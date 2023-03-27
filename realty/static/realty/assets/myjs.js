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
//slider 2
/* шаблон */
(function(){
/* сохраняем в переменной doc обьект документа */	
let doc = document,
index = 1;
/* Определяем конструктор слайдера */	
let Slider = function(){
this.box = doc.querySelector('.wrape');
this.slidesBox = doc.querySelector('.lenta');
this.slides = doc.querySelectorAll('.contslide');
this.btns = doc.querySelectorAll('.slbtn');
/*https://developer.mozilla.org/ru/docs/Web/API/Element/clientWidth получаем значение ширины нашего главного контейнера*/
this.size = this.box.clientWidth;
/* вызываем методы в нутри конструктор*/
this.position();
this.carousel();
};
/* методы для конструктора*/

/* первый метод - смещаем на одно изображение в лево*/
Slider.prototype.position = function() {
let size = this.size;
this.slidesBox.style.transform = 'translateX('+(-index * size)+'px)';
}

/* назначение кнопок*/
Slider.prototype.carousel = function(){
let i, max = this.btns.length,
that = this;
/* запускаем цикл*/
for (i = 0; i< max; i+=1) {
/*по клику вызываем метод*/
that.btns[i].addEventListener('click', Slider[that.btns[i].id].bind(null, that));
}
}

/* методы предыдущий*/
Slider.prev = function(box){
box.slidesBox.style.transition = 'transform .3s ease-in-out';
let size = box.size;
/* stop slides prev in final*/
index <=0 ? false : index--;
box.slidesBox.style.transform = 'translateX('+(-index * size)+'px)';
box.jump();


};
/* методы следующий*/
Slider.next= function(box){
/* плавное перемещение*/
box.slidesBox.style.transition = 'transform .3s ease-in-out';
let max = box.slides.length;
let size = box.size;
/* stop slides next in final*/
index >= max-1? false : index++;
box.slidesBox.style.transform = 'translateX('+(-index * size)+'px)';
box.jump();
};
/* методы перекидывающий картинки*/
Slider.prototype.jump = function() {
let that = this;
var size = this.size;
this.slidesBox.addEventListener('transitionend' , ()=>{
that.slides[index].id === 'firstClone'? index=1 : index;
that.slides[index].id === 'lastClone'? index= that.slides.length -2 : index;

that.slidesBox.style.transition = 'none';
that.slidesBox.style.transform = 'translateX('+(-index * size)+'px)';

} );

}
new Slider();
})();

    
    
    
    
    
    
    

    
    
    
    
    
    
    
    