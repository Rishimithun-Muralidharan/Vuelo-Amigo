/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 300,
    // reset: true
});

sr.reveal('.leftside_titles, .rightside_content, .footer__container');
sr.reveal('.footer__info', {delay: 400});
sr.reveal('.sidebar, .seller_info, .poster', {origin: 'left'});
sr.reveal('.recent_acivity_bar, .states_info_card', {origin: 'right'});
// sr.reveal('.recent_acivity_bar', {origin: 'bottom'})