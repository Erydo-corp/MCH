const back= document.querySelector('#back');
const next= document.querySelector('#next');

const photos=['voluntr.png','2 карточка вся.svg'];
let i=0;

next.addEventListener ('click', ()=> {
    i++;
    document.querySelector('#pictures').src=photos[i];
    if (i>photos.length-1) {i=0};
})

back.addEventListener ('click', ()=> {
    i--;
    document.querySelector('#pictures').src=photos[i];
    if (i<0) {i=photos.length-1}
})