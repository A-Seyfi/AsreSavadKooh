const DL_mode = document.getElementById('DL_mode')
const DL_btn = document.getElementById('DL_btn')
const DL_status = document.getElementById('DL_status')
const body_color = document.querySelectorAll('.body_color')
const main_color = document.querySelectorAll('.main_color')
const content_color1 = document.querySelectorAll('.content_color1')
const content_color2 = document.querySelectorAll('.content_color2')
const color_b = document.querySelectorAll('.color_b')
let num = 1

DL_mode.addEventListener(('click'), ()=>{
    num += 1
    if(num > 2){
        num = 1
    }

    if(num == 2){
        DL_mode.style.backgroundColor = 'black'
        DL_btn.style.backgroundColor = 'white'
        DL_btn.style.marginLeft = '26px'
        setTimeout(()=>{
            body_color.forEach(body_color => {
                body_color.style.backgroundColor = '#464646'
            });

            main_color.forEach(main_color => {
                main_color.style.backgroundColor = '#373737'
            });

            content_color1.forEach(content_color1 => {
                content_color1.style.backgroundColor = '#278EA5'
            });

            content_color2.forEach(content_color2 => {
                content_color2.style.backgroundColor = '#3e57ba'
            });

            color_b.forEach(color_b => {
                color_b.style.color = 'white'
            });
            
            DL_status.src = "/static/images/dark.png"
        }, 200)
    }
    else{
        DL_mode.style.backgroundColor = 'white'
        DL_btn.style.backgroundColor = 'black'
        DL_btn.style.marginLeft = '3px'
        setTimeout(()=>{
            body_color.forEach(body_color => {
                body_color.style.backgroundColor = '#f7f2e0'
            });

            main_color.forEach(main_color => {
                main_color.style.backgroundColor = '#E5E1DA'
            });

            content_color1.forEach(content_color1 => {
                content_color1.style.backgroundColor = '#3e57ba'
            });

            content_color2.forEach(content_color2 => {
                content_color2.style.backgroundColor = '#5570de'
            });

            color_b.forEach(color_b => {
                color_b.style.color = 'black'
            });

            DL_status.src = "/static/images/light.png"
        }, 200)
    }
    
})