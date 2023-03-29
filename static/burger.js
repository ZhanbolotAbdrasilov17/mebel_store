const body = document.querySelector('body')
const burger = document.querySelector('.burger')
const searchCard = document.querySelector('.search-card')
const burgerNav = document.querySelector('.burger-nav')

burger.addEventListener('click', () => {
  searchCard.classList.toggle('show')
  burgerNav.classList.toggle('show')
  // body.classList.toggle('overlay')
})