const active_pic = document.getElementById('active_pic')
const active_title = document.getElementById('active_title')

document.addEventListener('DOMContentLoaded', function () {
    const gallery = document.querySelectorAll('.gallery__isle');

    gallery.forEach(function (div) {
      div.addEventListener('click', function () {
        const pic = div.querySelector('img').src
        const title = div.querySelector('.gallery_title').innerHTML

        active_pic.src = pic
        active_pic.style.minHeight = "70%"
        active_pic.style.maxHeight = "70%"

        active_title.innerHTML = title

        gallery.forEach(function (element) {
          element.classList.remove('active');
        });
        div.classList.add('active');

      });
    });
  });