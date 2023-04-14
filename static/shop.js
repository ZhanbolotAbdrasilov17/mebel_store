const arrows = document.querySelectorAll('.arrow_example_0')
const barsScrapper = document.querySelectorAll('.bars-scrapper')
const allCheckbox = document.querySelectorAll('.checkbox-container')
const blocks = document.querySelectorAll('.block-category')
const colors = document.querySelector('.colors')
const allFilter = document.querySelectorAll('.filter')

const counters = new Array(allFilter.length).fill(0)

console.log(barsScrapper)
console.log(counters)


let counter = 0

for (let i = 0; i < allFilter.length; i++) {
    allFilter[i].addEventListener('click', () => {
        counters[i]++
        console.log(counter)
        if (counters[i] % 2 === 0) {
            // allFilter[0].style.borderBottom = ''
            arrows[i].style.transform = 'rotate(-45deg)'
            barsScrapper[i].style.display = 'none'
        }
        if (counters[i] % 2) {
            // allFilter[0].style.borderBottom = '1px solid #e5e5e5'
            arrows[i].style.transform = 'rotate(135deg)'
            barsScrapper[i].style.display = 'flex'
    
        }
    })
}

// allFilter[0].addEventListener('click', () => {
//     counter++
//     console.log(counter)
//     if (counter % 2 === 0) {
//         // allFilter[0].style.borderBottom = ''
//         arrows[0].style.transform = 'rotate(-45deg)'
//         barsScrapper[0].style.display = 'none'
//     }
//     if (counter % 2) {
//         // allFilter[0].style.borderBottom = '1px solid #e5e5e5'
//         arrows[0].style.transform = 'rotate(135deg)'
//         barsScrapper[0].style.display = 'flex'

//     }
// })


// let counter2 = 0

// allFilter[1].addEventListener('click', () => {
//     counter2++
//     if (counter2 % 2 === 0 ) {
//         arrows[1].style.transform = 'rotate(-45deg)'
//         barsScrapper[1].style.display = 'none'
//     }
//     if (counter2 % 2) {
//         arrows[1].style.transform = 'rotate(135deg)'
//         barsScrapper[1].style.display = 'flex'
//     }
// })

// allFilter[2].addEventListener('click', () => {
//     counter2++
//     if (counter2 % 2 === 0 ) {
//         arrows[2].style.transform = 'rotate(-45deg)'
//         barsScrapper[2].style.display = 'none'
//     }
//     if (counter2 % 2) {
//         arrows[2].style.transform = 'rotate(135deg)'
//         barsScrapper[2].style.display = 'flex'
//     }
// })

