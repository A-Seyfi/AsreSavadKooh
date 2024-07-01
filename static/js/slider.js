const  slide_container = document.getElementById('slide_container')
const slide = document.querySelectorAll('.slide').length

let translate = 100 / slide
let value = 100 / slide

slide_container.style.width = `${slide * 50 + 1}%`

setInterval(() => {
   slide_container.style.transform = `translateX(-${value}%)`
   value += translate
   if(value == translate * 3){
      value = 0
   }
}, 1800);