const btnMobile = document.getElementById('btn-mobile');

function toggleMenu(){
  const nav = document.querySelector('#nav');
  nav.classList.add('active');
}

btnMobile.addEventListener('click', toggleMenu);