


let targetCard = null;                       // store the element itself
const ovM = document.getElementById('mOverlay');
const shM = document.getElementById('mSheet');

// OPEN bottom‑sheet
document.querySelectorAll('.m-card__more').forEach(btn=>{
  btn.addEventListener('click', e=>{
    targetCard = e.currentTarget.closest('.m-card');   // the exact card
    ovM.classList.add('show');
    shM.classList.add('show');
  });
});

// CLOSE bottom‑sheet
const closeSheet = () => {
  ovM.classList.remove('show');
  shM.classList.remove('show');
  targetCard = null;
};
ovM.addEventListener('click', closeSheet);

// REMOVE action
document.getElementById('mRemove').addEventListener('click', () => {
  if (targetCard) targetCard.remove();       // removes only that card
  closeSheet();
});

  
  /* DESKTOP delete */
  document.querySelectorAll('.d-item__del').forEach(b=>b.addEventListener('click',e=>{
    e.currentTarget.closest('.d-item').remove();
  }));
  
  /* shared */
  function addToCart(id){alert(`Added ${id} to cart (demo)`);}